# from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snacks
from django.urls import reverse_lazy


# Create your views here.
class SnackListView(ListView):
    template_name='snacks_list.html'
    model=Snacks

class SnackDetailView(DetailView):
    template_name='snacks_detail.html'
    model=Snacks

class SnackCreatView(CreateView):
    template_name='create_list.html'
    model=Snacks
    fields=["title","description","purchaser"]

class SnackUpdateView(UpdateView):
    template_name='update_list.html'
    model=Snacks
    fields=["title","description","purchaser"]
    
class SnackDeleteView(DeleteView):
    template_name='delete_list.html'
    model=Snacks
    success_url=reverse_lazy("snacks_list")