from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('log/', views.log_food, name='log_food'),
    path('summary/', views.food_log_summary, name='food_log_summary'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
]
