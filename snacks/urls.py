from django.urls import path
from .views import SnackListView,SnackDetailView,SnackUpdateView,SnackCreatView,SnackDeleteView

urlpatterns=[
    path("",SnackListView.as_view(),name="snacks_list"),
    path("<int:pk>/",SnackDetailView.as_view(),name="snacks_detail"),
    path("<int:pk>/update/",SnackUpdateView.as_view(),name="update_list"),
    path("create/",SnackCreatView.as_view(),name="create_list"),
    path("<int:pk>/delete/",SnackDeleteView.as_view(),name="delete_list"),

]