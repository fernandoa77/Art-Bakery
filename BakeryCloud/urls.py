from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from bakery import views as bakery_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bakery/', include('bakery.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', bakery_views.logout_view, name='logout'),
    path('', bakery_views.home_redirect, name='home_redirect'),
]