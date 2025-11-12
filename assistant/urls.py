from django.urls import path
from . import views

app_name = 'assistant'

urlpatterns = [
    path('', views.assistant_view, name='assistant'),
    path('api/chat/', views.chat_api, name='chat_api'),
    path('api/history/', views.get_history, name='get_history'),
]
