from django.urls import path
from .views import index,ml_model
urlpatterns=[
    path('',index),
    path('home',ml_model)
]