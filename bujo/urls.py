from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='bujo-home'),
    path('profile', views.profile, name='bujo-profile'),
    path('key', views.key, name='bujo-key'),
    path('this_week', views.week, name='bujo-week'),
    path('today', views.today, name='bujo-today'),
]