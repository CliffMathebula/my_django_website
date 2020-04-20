from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('post.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # new
    path('accounts/', include('accounts.urls')),  # new
    path('admin/', admin.site.urls),
]
