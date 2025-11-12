# JARVIS - Assistente Virtual de IA

## 🤖 Sobre o Projeto

Este projeto Django agora inclui o **JARVIS**, um assistente virtual de IA inspirado no sistema do Homem de Ferro. O JARVIS foi desenvolvido para ajudar os usuários a interagir com o sistema de gerenciamento de produtos de forma natural e intuitiva.

## ✨ Funcionalidades

### Conversação Natural
- Interface de chat em tempo real
- Processamento de linguagem natural em português
- Respostas contextualizadas e inteligentes

### Gerenciamento de Produtos
- 📦 Listar todos os produtos cadastrados
- 🔍 Buscar produtos por nome
- 💰 Consultar preços de produtos
- 🏷️ Ver categorias disponíveis
- 📊 Obter estatísticas de produtos

### Recursos Avançados
- 🎤 **Reconhecimento de Voz**: Use comandos de voz para interagir com o assistente (suportado em navegadores compatíveis)
- 🔊 **Text-to-Speech**: O assistente responde com voz sintetizada
- 💾 **Histórico de Conversas**: Todas as conversas são salvas e podem ser recuperadas
- 🎨 **Interface Moderna**: Design inspirado no tema do Homem de Ferro com gradientes roxos e animações suaves

## 🚀 Como Usar

### 1. Acesse o Assistente

Após iniciar o servidor Django, acesse:
```
http://localhost:8000/assistant/
```

### 2. Interaja com o JARVIS

Você pode:
- Digitar mensagens no campo de texto
- Usar os botões de sugestão rápida
- Clicar no ícone 🎤 para usar comando de voz (navegadores compatíveis)

### 3. Exemplos de Comandos

**Saudações:**
- "Olá JARVIS"
- "Bom dia"
- "Oi"

**Consultas sobre Produtos:**
- "Mostre os produtos"
- "Quantos produtos você tem?"
- "Listar todos os produtos"

**Buscar Produtos:**
- "Buscar notebook"
- "Procurar mouse"
- "Encontrar livros"

**Consultar Preços:**
- "Qual o preço do notebook?"
- "Quanto custa o mouse?"
- "Valor do teclado"

**Categorias:**
- "Ver categorias"
- "Mostre as categorias"
- "Quais categorias existem?"

**Ajuda:**
- "Ajuda"
- "O que você pode fazer?"
- "Help"

## 🛠️ Tecnologias Utilizadas

- **Backend:**
  - Django 5.2.8
  - Python 3.12
  - SQLite

- **Frontend:**
  - HTML5
  - CSS3 (com gradientes e animações)
  - JavaScript (Vanilla)
  - Web Speech API (reconhecimento de voz)
  - Speech Synthesis API (text-to-speech)

## 📁 Estrutura do Projeto

```
assistant/
├── ai_engine.py          # Motor de IA com processamento de linguagem natural
├── models.py             # Modelos para Conversation e Message
├── views.py              # Views para a interface e API
├── urls.py               # Rotas da aplicação
├── admin.py              # Registro no Django Admin
├── templates/
│   └── assistant/
│       └── assistant.html # Interface do chat
└── migrations/           # Migrações do banco de dados
```

## 🔧 Instalação

1. O app `assistant` já está incluído em `INSTALLED_APPS`
2. As migrações já foram aplicadas
3. Os dados de teste já foram criados

Para recriar o ambiente:

```bash
# Instalar Django
pip install django

# Aplicar migrações
python manage.py migrate

# Criar dados de teste (opcional)
python manage.py shell
>>> from produtos.models import Categoria, Produto
>>> # Criar categorias e produtos...

# Iniciar servidor
python manage.py runserver
```

## 🎯 Recursos Futuros

- [ ] Integração com APIs de IA externa (OpenAI, Google AI)
- [ ] Suporte para múltiplos idiomas
- [ ] Comandos para criar/editar/deletar produtos
- [ ] Análises e relatórios via voz
- [ ] Integração com sistema de autenticação
- [ ] Notificações push
- [ ] Exportação de conversas

## 📝 Notas

- O reconhecimento de voz funciona melhor no Google Chrome
- A síntese de voz está configurada para português do Brasil
- O histórico de conversas é mantido por sessão do navegador
- Todas as interações são registradas no banco de dados

## 🎨 Design

A interface foi inspirada no design do JARVIS do universo Marvel, com:
- Gradientes roxos e azuis
- Animações suaves de entrada de mensagens
- Avatares para usuário e assistente
- Indicador de digitação animado
- Layout responsivo e moderno

## 🤝 Contribuindo

Para adicionar novas funcionalidades ao assistente, edite o arquivo `assistant/ai_engine.py` e adicione novos padrões de reconhecimento e respostas no método `process_message()`.

---

**Desenvolvido para o Projeto Freelancer Django**
