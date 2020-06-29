from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from blog.models import Category, Post


class HomeView(View):
    '''главная страница'''
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        context = {'categoryes': category_list,
                   'post_list': post_list}
        return render(request, 'blog/home.html', context)


class PostDetailView(View):
    '''Вывод полной статьи'''
    def get(self, request, **kwargs):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=kwargs.get('slug'))
        context = {'categoryes': category_list,
                   'post': post}
        return render(request, post.template, context)


class CategoryView(View):
    '''Вывод статей'''
    def get(self, request, category_slug=None, tag_slug=None):
        posts = []
        # по категории
        if category_slug is not None:
            posts = Post.objects.filter(category__slug=category_slug,
                                        category__published=True,
                                        published=True)
        # по тегу
        elif tag_slug is not None:
            posts = Post.objects.filter(tags__slug=tag_slug,
                                        published=True)
        if posts.exists():
            template = posts.first().get_category_template()
        else:
            template = 'blog/post_list.html'
        return render(request, template, {'posts': posts})
