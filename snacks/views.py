from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snack


# Create your views here.
class SnackListView(ListView):
    template_name = "snack-list.html"
    model = Snack
    context_object_name = 'candy_snacks'


class SnackDetailView(DetailView):
    template_name = "snack-detail.html"
    model = Snack