from django.contrib import admin
from django.urls import path, include
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),               # Routes home and app URLs to your tracker app
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in login/logout/password URLs
]
