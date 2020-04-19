# post/urls.py
from django.urls import path
from .views import HomePageView
from .views import UserCreateView
from .views import UserDetailsView
from .views import EditDetailsView
from .views import DeleteUserView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add_user/new/', UserCreateView.as_view(), name='register'),
    path('view_details/<int:pk>/', UserDetailsView.as_view(), name='user_details'),
    path('edit_user/<int:pk>/', EditDetailsView.as_view(), name='edit_user'),
    path('delete_user/<int:pk>/delete/', DeleteUserView.as_view(), name='delete_user'),
]
