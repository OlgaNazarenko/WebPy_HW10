from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import (add_author, add_quote, about_author,
                    search_tag, top_ten_tags)


app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('add_author/', views.add_author, name='add_author'),
    path('author/<int:author_id>', views.about_author, name = 'about_author'),
    path('search_tag/<str:tag>/', views.search_tag, name='search_tag'),
    path('top_ten_tags/', views.top_ten_tags, name='top_ten_tags'),
]
