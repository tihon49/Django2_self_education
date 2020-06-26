from datetime import datetime

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
    def get(self, request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        context = {'categoryes': category_list,
                   'post': post}
        return render(request, 'blog/post_detail.html', context)


class CategoryView(View):
    '''Вывод статей категории'''
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        post = list(Post.objects.filter(category=category))
        return render(request, 'blog/post_list.html', {'posts': post})