from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls, name=admin),
    path('', include('blog.urls')),
    path('login/', LoginView.as_view(), name="blog_login"),
    path('logout/', LogoutView.as_view(), name="blog_logout"),
]