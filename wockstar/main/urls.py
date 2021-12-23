from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('feedback', views.feedback, name='feedback'),
    path('procedures', views.procedures, name='procedures'),
    path('services', views.services, name='services'),
    path("sign", views.login_request, name="sign"),
    path("signout", views.signout_request, name="signout"),
    path('register', views.register_request, name='register')

]