
from django import views
from django import urls

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet


from posts.api import views
from django import urls

from django.urls import path




urlpatterns =[
    path(r'^post$',views.postApi),
    path(r'^post/([0-9]+)',views.postApi)
]

post_router = DefaultRouter()
post_router.register(r'posts', PostViewSet)


