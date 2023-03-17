from django.urls import path
from . import views

urlpatterns = [
    path('', views.HelloWorldAPIView.as_view())
]