# Guia do Assistente JARVIS

## 🎯 Visão Geral

O JARVIS é um assistente virtual inspirado no sistema de IA do Homem de Ferro, desenvolvido para o projeto Django de gerenciamento de produtos. Ele permite que os usuários interajam com o sistema usando linguagem natural, tanto por texto quanto por voz.

## 🚀 Início Rápido

### 1. Acessar o Assistente

```
http://localhost:8000/assistant/
```

### 2. Formas de Interação

- **Texto**: Digite sua mensagem e clique em "Enviar" ou pressione Enter
- **Voz**: Clique no ícone 🎤 e fale (funciona melhor no Chrome)
- **Sugestões**: Use os botões de sugestão rápida na tela inicial

## 💬 Comandos Disponíveis

### Saudações
```
Olá JARVIS
Oi
Bom dia
Boa tarde
Boa noite
```

### Consultar Produtos
```
Mostre os produtos
Quais produtos você tem?
Listar todos os produtos
Quantos produtos existem?
```

### Buscar Produtos
```
Buscar notebook
Procurar mouse
Encontrar livros
```

### Consultar Preços
```
Qual o preço do notebook?
Quanto custa o mouse?
Valor do teclado
Preço de [nome do produto]
```

### Ver Categorias
```
Ver categorias
Mostre as categorias
Quais categorias existem?
```

### Ajuda
```
Ajuda
Help
O que você pode fazer?
```

### Despedidas
```
Tchau
Adeus
Até logo
Até mais
```

## 🎤 Recursos de Voz

### Reconhecimento de Voz
- Clique no ícone 🎤 para ativar
- Fale sua pergunta claramente
- O texto será preenchido automaticamente e enviado

### Síntese de Voz
- Todas as respostas do JARVIS são faladas
- Funciona automaticamente em navegadores compatíveis
- Configurado para português do Brasil

## 🔧 API Endpoints

### POST /assistant/api/chat/
Envia uma mensagem para o assistente

**Request:**
```json
{
  "message": "Olá JARVIS",
  "session_id": "unique-session-id"
}
```

**Response:**
```json
{
  "response": "Olá! Eu sou o JARVIS...",
  "session_id": "unique-session-id"
}
```

### GET /assistant/api/history/
Recupera o histórico de conversas

**Query Params:**
- `session_id`: ID da sessão

**Response:**
```json
{
  "messages": [
    {
      "user": "Olá JARVIS",
      "assistant": "Olá! Eu sou o JARVIS...",
      "timestamp": "2025-11-12T17:45:00Z"
    }
  ]
}
```

## 🎨 Interface

### Cores e Tema
- Gradiente roxo inspirado no tema do Homem de Ferro
- Avatar 👤 para usuário
- Avatar 🤖 para JARVIS
- Animações suaves nas mensagens

### Responsividade
- Funciona em desktop e mobile
- Layout adaptativo
- Altura máxima otimizada para diferentes telas

## 🔒 Segurança

- Validação de entrada em todos os endpoints
- Proteção contra injeção de código
- Mensagens de erro genéricas para usuários
- Logging detalhado para debugging
- Sem exposição de stack traces

## 📊 Modelos de Dados

### Conversation
- `session_id`: ID único da sessão
- `created_at`: Data/hora de criação

### Message
- `conversation`: Referência à conversa
- `user_message`: Mensagem do usuário
- `assistant_response`: Resposta do assistente
- `timestamp`: Data/hora da mensagem

## 🧪 Testes

Execute os testes com:
```bash
python manage.py test assistant
```

14 testes cobrem:
- Motor de IA (padrões de reconhecimento)
- Views e APIs
- Modelos de dados
- Validações de segurança

## 🔄 Fluxo de Processamento

1. Usuário envia mensagem via interface ou API
2. Mensagem é validada e session_id é gerado/recuperado
3. `JarvisAssistant.process_message()` analisa a mensagem
4. Padrões são reconhecidos e resposta é gerada
5. Mensagem e resposta são salvas no banco
6. Resposta é retornada ao usuário
7. Interface exibe texto e sintetiza voz

## 🛠️ Personalização

### Adicionar Novos Padrões

Edite `assistant/ai_engine.py`:

```python
def process_message(self, message):
    message_lower = message.lower().strip()
    
    # Adicione seu padrão aqui
    if "novo_comando" in message_lower:
        return self._seu_novo_metodo()
    
    # ... resto do código
```

### Adicionar Nova Funcionalidade

1. Adicione método em `JarvisAssistant`
2. Registre padrão em `process_message()`
3. Adicione testes em `tests.py`
4. Atualize documentação

## 📈 Estatísticas

Consulte o Django Admin para:
- Total de conversas
- Mensagens por dia
- Padrões mais consultados
- Sessões ativas

Acesse: `http://localhost:8000/admin/`

## 🐛 Troubleshooting

### Reconhecimento de voz não funciona
- Verifique se está usando Chrome ou Edge
- Confirme permissões do microfone
- Verifique conexão com internet

### Síntese de voz não funciona
- Verifique volume do sistema
- Teste em navegador diferente
- Verifique se há voices instaladas para pt-BR

### API retorna erro 500
- Verifique logs do servidor
- Confirme que produtos/categorias existem
- Verifique migrações aplicadas

## 📞 Suporte

Para problemas ou sugestões:
1. Verifique os logs em `assistant/views.py`
2. Execute os testes para identificar problemas
3. Consulte a documentação do Django

## 🎓 Aprendizado

O JARVIS usa um sistema simples de pattern matching. Para IA mais avançada, considere:
- Integração com OpenAI GPT
- TensorFlow/PyTorch para ML
- Rasa para NLP avançado
- Dialogflow para chatbots

## 📝 Licença

Este assistente faz parte do projeto Django e segue a mesma licença.
