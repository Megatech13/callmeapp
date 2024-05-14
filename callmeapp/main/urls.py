from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('specialists', views.specialists, name='specialists'),
    path('my_contacts', views.my_contacts, name='my_contacts'),
]
