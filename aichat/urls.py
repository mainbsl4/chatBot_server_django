from django.urls import path
from .views import chat_api

urlpatterns = [
    # path('', chat_view, name='chat'),
    # path('chat/', chat_api, name='chat_api'),
    path('chat/', chat_api, name='chat_api'),
]
