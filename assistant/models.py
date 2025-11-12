from django.db import models
from django.utils import timezone


class Conversation(models.Model):
    """Armazena histórico de conversas com o assistente"""
    session_id = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Conversa {self.session_id} - {self.created_at}"


class Message(models.Model):
    """Armazena mensagens individuais"""
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    user_message = models.TextField()
    assistant_response = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        return f"Mensagem em {self.timestamp}"
