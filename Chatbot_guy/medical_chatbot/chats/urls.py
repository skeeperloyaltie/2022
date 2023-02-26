
from django.urls import path 
from . import views

urlpatterns = [
    path('index.html', views.chats__, name = 'chats'),
    path('chatbot.html', views.chatbot, name = 'chatbot'),
]

    