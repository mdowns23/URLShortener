from django.urls import path
from . import views

urlpatterns = [
    # Url mapping to html file
    path('', views.index, name='index'),
    # Store url in database
    path('create', views.create, name='create'),
    # Store shortened link id in variable pk
    path('<str:pk>', views.go, name='go')
]