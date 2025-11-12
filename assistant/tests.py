from django.test import TestCase, Client
from django.urls import reverse
import json
from .models import Conversation, Message
from .ai_engine import JarvisAssistant
from produtos.models import Produto, Categoria


class JarvisAssistantTests(TestCase):
    """Tests for the JARVIS AI engine"""
    
    def setUp(self):
        self.assistant = JarvisAssistant()
        # Create test data
        self.cat = Categoria.objects.create(nome="Teste")
        self.produto = Produto.objects.create(
            nome="Produto Teste",
            preço=100.00,
            categoria=self.cat
        )
    
    def test_greeting_response(self):
        """Test greeting messages"""
        response = self.assistant.process_message("Olá")
        self.assertIn("JARVIS", response)
        self.assertIn("assistente", response.lower())
    
    def test_product_query(self):
        """Test product listing"""
        response = self.assistant.process_message("Mostre os produtos")
        self.assertIn("produto", response.lower())
        self.assertIn("Produto Teste", response)
    
    def test_category_query(self):
        """Test category listing"""
        response = self.assistant.process_message("Ver categorias")
        self.assertIn("categoria", response.lower())
        self.assertIn("Teste", response)
    
    def test_price_query(self):
        """Test price queries"""
        response = self.assistant.process_message("Qual o preço do Produto Teste?")
        self.assertIn("100", response)
    
    def test_search_product(self):
        """Test product search"""
        response = self.assistant.process_message("Buscar Produto Teste")
        self.assertIn("Produto Teste", response)
    
    def test_help_response(self):
        """Test help command"""
        response = self.assistant.process_message("ajuda")
        self.assertIn("ajudá-lo", response.lower())


class AssistantViewTests(TestCase):
    """Tests for assistant views"""
    
    def setUp(self):
        self.client = Client()
        # Create test data
        self.cat = Categoria.objects.create(nome="Eletrônicos")
        Produto.objects.create(
            nome="Notebook",
            preço=3000.00,
            categoria=self.cat
        )
    
    def test_assistant_page_loads(self):
        """Test that assistant page loads successfully"""
        response = self.client.get(reverse('assistant:assistant'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "JARVIS")
    
    def test_chat_api_post(self):
        """Test chat API endpoint"""
        data = {
            'message': 'Olá',
            'session_id': 'test-session'
        }
        response = self.client.post(
            reverse('assistant:chat_api'),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertIn('response', json_response)
        self.assertIn('JARVIS', json_response['response'])
    
    def test_chat_api_invalid_method(self):
        """Test that GET requests are not allowed"""
        response = self.client.get(reverse('assistant:chat_api'))
        self.assertEqual(response.status_code, 405)
    
    def test_chat_api_empty_message(self):
        """Test that empty messages return error"""
        data = {
            'message': '',
            'session_id': 'test-session'
        }
        response = self.client.post(
            reverse('assistant:chat_api'),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
    
    def test_history_api(self):
        """Test conversation history endpoint"""
        # Create a conversation first
        conversation = Conversation.objects.create(session_id='test-session')
        Message.objects.create(
            conversation=conversation,
            user_message="Olá",
            assistant_response="Olá! Eu sou o JARVIS"
        )
        
        response = self.client.get(
            reverse('assistant:get_history') + '?session_id=test-session'
        )
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertIn('messages', json_response)
        self.assertEqual(len(json_response['messages']), 1)


class ConversationModelTests(TestCase):
    """Tests for Conversation and Message models"""
    
    def test_create_conversation(self):
        """Test creating a conversation"""
        conversation = Conversation.objects.create(session_id='test-123')
        self.assertEqual(conversation.session_id, 'test-123')
        self.assertIsNotNone(conversation.created_at)
    
    def test_create_message(self):
        """Test creating a message"""
        conversation = Conversation.objects.create(session_id='test-456')
        message = Message.objects.create(
            conversation=conversation,
            user_message="Test question",
            assistant_response="Test answer"
        )
        self.assertEqual(message.user_message, "Test question")
        self.assertEqual(message.assistant_response, "Test answer")
        self.assertIsNotNone(message.timestamp)
    
    def test_conversation_message_relationship(self):
        """Test that messages are related to conversations"""
        conversation = Conversation.objects.create(session_id='test-789')
        Message.objects.create(
            conversation=conversation,
            user_message="Question 1",
            assistant_response="Answer 1"
        )
        Message.objects.create(
            conversation=conversation,
            user_message="Question 2",
            assistant_response="Answer 2"
        )
        self.assertEqual(conversation.messages.count(), 2)

