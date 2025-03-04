from django.urls import path
from .views import index, post_detail, category_view  # Все нужные импорты

app_name = "blog"  # Определяем app_name

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', category_view, name='category'),  # Категории
]
