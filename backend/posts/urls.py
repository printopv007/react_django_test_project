
from posts.api import views
from django import urls

from django.urls import path




urlpatterns =[
    path(r'^post$',views.postApi),
    path(r'^post/([0-9]+)',views.postApi)
]