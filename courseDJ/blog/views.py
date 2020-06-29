from datetime import datetime

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.base import View

from blog.models import Category, Post



class PostDetailView(View):
    '''Вывод полной статьи'''
    def get(self, request, **kwargs):
        category_list = Category.objects.all()
        post = get_object_or_404(Post, slug=kwargs.get('slug'))
        return render(request, post.template, {'categoryes': category_list, 'post': post})



class PostListView(View):
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=datetime.now(), published=True)

    '''Вывод статей'''
    def get(self, request, category_slug=None, tag_slug=None):
        category_list = Category.objects.all()
        # по категории
        if category_slug is not None:
            posts = self.get_queryset().filter(category__slug=category_slug,
                                               category__published=True,
                                               published=True)
        # по тегу
        elif tag_slug is not None:
            posts = self.get_queryset().filter(tags__slug=tag_slug)
        else:
            posts = self.get_queryset()

        if posts.exists():
            template = posts.first().get_category_template()
        else:
            template = 'blog/post_list.html'
        return render(request, template, {'post_list': posts,
                                          'categoryes': category_list})
