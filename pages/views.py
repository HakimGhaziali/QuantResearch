from django.shortcuts import render

# Create your views here.




from django.views.generic import ListView
from Article.models import Post


class HomeView(ListView):

    template_name = 'home.html'
    model = Post
    