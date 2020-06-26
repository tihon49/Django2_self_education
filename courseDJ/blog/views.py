from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from blog.models import Category, Post, Tag


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
        return render(request, post.template, context)


class CategoryView(View):
    '''Вывод статей категории'''
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        post = Post.objects.filter(category=category)
        return render(request, category.template, {'posts': post})


class TagView(View):
    '''Вывод статей тега'''
    def get(self, request, tag_slug):
        tag = Tag.objects.get(slug=tag_slug)
        posts = Post.objects.filter(tags=tag)
        return render(request, 'blog/tag_list.html', {'posts': posts})