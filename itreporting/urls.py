from django.urls import path
from users import views as users_views
from . import views 

app_name = 'itreporting'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('register', users_views.register, name = 'register'),
]