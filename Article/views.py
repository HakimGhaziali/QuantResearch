from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post


class ArticleList(ListView):

    model = Post
    context_object_name = 'Article_list'
    template_name = 'article/article_list.html'


class ArtileDetail(DetailView):
    
    model = Post
    context_object_name = 'Article_detail'
    template_name = 'article/article_detail.html'