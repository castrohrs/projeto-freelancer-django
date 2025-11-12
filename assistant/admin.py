from django.contrib import admin
from .models import Conversation, Message


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'created_at']
    list_filter = ['created_at']
    search_fields = ['session_id']
    readonly_fields = ['created_at']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['conversation', 'timestamp', 'user_message_preview']
    list_filter = ['timestamp']
    search_fields = ['user_message', 'assistant_response']
    readonly_fields = ['timestamp']
    
    def user_message_preview(self, obj):
        return obj.user_message[:50] + '...' if len(obj.user_message) > 50 else obj.user_message
    user_message_preview.short_description = 'Mensagem do Usuário'

