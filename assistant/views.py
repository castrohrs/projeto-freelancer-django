from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import uuid
from .models import Conversation, Message
from .ai_engine import JarvisAssistant


def assistant_view(request):
    """View principal do assistente"""
    # Gera ou recupera session_id
    session_id = request.session.get('assistant_session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        request.session['assistant_session_id'] = session_id
    
    return render(request, 'assistant/assistant.html', {
        'session_id': session_id
    })


@csrf_exempt
def chat_api(request):
    """API para interação com o assistente"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        session_id = data.get('session_id', '')
        
        if not user_message:
            return JsonResponse({'error': 'Mensagem vazia'}, status=400)
        
        if not session_id:
            session_id = str(uuid.uuid4())
        
        # Obtém ou cria a conversa
        conversation, created = Conversation.objects.get_or_create(
            session_id=session_id
        )
        
        # Processa a mensagem com o assistente
        assistant = JarvisAssistant()
        response_text = assistant.process_message(user_message)
        
        # Salva a mensagem
        Message.objects.create(
            conversation=conversation,
            user_message=user_message,
            assistant_response=response_text
        )
        
        return JsonResponse({
            'response': response_text,
            'session_id': session_id
        })
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_history(request):
    """Retorna o histórico de conversas"""
    session_id = request.GET.get('session_id', '')
    
    if not session_id:
        return JsonResponse({'messages': []})
    
    try:
        conversation = Conversation.objects.get(session_id=session_id)
        messages = conversation.messages.all()
        
        history = [
            {
                'user': msg.user_message,
                'assistant': msg.assistant_response,
                'timestamp': msg.timestamp.isoformat()
            }
            for msg in messages
        ]
        
        return JsonResponse({'messages': history})
    except Conversation.DoesNotExist:
        return JsonResponse({'messages': []})

