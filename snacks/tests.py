from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snacks


class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snacks.objects.create(
            title="Apple", description=1, purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Apple")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "Apple")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(self.snack.description, 1)

    def test_snack_list_view(self):
        response = self.client.get(reverse("snacks_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Apple")
        self.assertTemplateUsed(response, "snacks_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snacks_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser:tester")
        self.assertTemplateUsed(response, "snacks_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("create_list"),
            {
                "title":"Rake",
                "description":"2",
                "purchaser":self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("snacks_detail", args="2"))
        self.assertContains(response, "Rake")



    def test_snacks_update_view_redirect(self):
        response = self.client.post(
            reverse("update_list", args="1"),
            {"title": "Updated title","description":"3","purchaser":self.user.id}
        )

        self.assertRedirects(response, reverse("snacks_detail", args="1"))

    def test_snacks_delete_view(self):
        response = self.client.get(reverse("delete_list", args="1"))
        self.assertEqual(response.status_code, 200)