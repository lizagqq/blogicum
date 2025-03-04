from django.urls import path
from django.shortcuts import render 
from .views import index, post_detail, category_view

app_name = "blog"

urlpatterns = [
    path('', index, name='index'),  
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', category_view, name='category'),

      path('about/', lambda request: render(request, 'blog/about.html'), name='about'),

       path('rules/', lambda request: render(request, 'blog/rules.html'), name='rules'),

        path('detail/', lambda request: render(request, 'blog/detail.html'), name='detail'),
]
