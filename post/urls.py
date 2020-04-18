# post/urls.py
from django.urls import path
from .views import HomePageView
from .views import UserCreateView
from .views import UserDetailView

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('post/new/', UserCreateView.as_view(), name='post_new'), # new
path('post/<int:pk>/', UserDetailView.as_view(), name='post_detail'),
]

