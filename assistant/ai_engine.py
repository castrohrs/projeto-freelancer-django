"""
Motor de IA para o assistente virtual - similar ao JARVIS
"""
import re
from produtos.models import Produto, Categoria


class JarvisAssistant:
    """Assistente de IA inspirado no JARVIS do Homem de Ferro"""
    
    def __init__(self):
        self.name = "JARVIS"
        self.greetings = [
            "olá", "oi", "hey", "ei", "bom dia", "boa tarde", "boa noite"
        ]
        self.farewells = ["tchau", "adeus", "até logo", "até mais"]
    
    def process_message(self, message):
        """Processa a mensagem do usuário e retorna uma resposta"""
        message_lower = message.lower().strip()
        
        # Saudações
        if any(greeting in message_lower for greeting in self.greetings):
            return self._greeting_response()
        
        # Despedidas
        if any(farewell in message_lower for farewell in self.farewells):
            return self._farewell_response()
        
        # Ajuda
        if "ajuda" in message_lower or "help" in message_lower:
            return self._help_response()
        
        # Consultas sobre produtos
        if "produto" in message_lower or "produtos" in message_lower:
            return self._product_query(message_lower)
        
        # Consultas sobre categorias
        if "categoria" in message_lower or "categorias" in message_lower:
            return self._category_query(message_lower)
        
        # Buscar produto específico
        if "buscar" in message_lower or "procurar" in message_lower or "encontrar" in message_lower:
            return self._search_product(message)
        
        # Informação sobre preço
        if "preço" in message_lower or "preco" in message_lower or "valor" in message_lower or "custa" in message_lower:
            return self._price_query(message)
        
        # Listar tudo
        if "listar" in message_lower or "mostrar" in message_lower or "ver" in message_lower:
            if "tudo" in message_lower or "todos" in message_lower:
                return self._list_all_products()
        
        # Resposta padrão
        return self._default_response()
    
    def _greeting_response(self):
        """Resposta de saudação"""
        return (
            "Olá! Eu sou o JARVIS, seu assistente virtual. "
            "Estou aqui para ajudá-lo com informações sobre produtos e categorias. "
            "Como posso ser útil hoje?"
        )
    
    def _farewell_response(self):
        """Resposta de despedida"""
        return "Até logo! Foi um prazer ajudá-lo. Estarei aqui quando precisar."
    
    def _help_response(self):
        """Resposta de ajuda"""
        return (
            "Posso ajudá-lo com as seguintes tarefas:\n\n"
            "📦 Consultar produtos e suas informações\n"
            "🏷️ Ver categorias disponíveis\n"
            "🔍 Buscar produtos específicos\n"
            "💰 Verificar preços\n"
            "📋 Listar todos os produtos\n\n"
            "Exemplos de perguntas:\n"
            "- 'Quais produtos você tem?'\n"
            "- 'Mostre as categorias'\n"
            "- 'Buscar [nome do produto]'\n"
            "- 'Qual o preço de [produto]?'\n"
            "- 'Listar todos os produtos'"
        )
    
    def _product_query(self, message):
        """Consulta sobre produtos"""
        produtos = Produto.objects.all()
        count = produtos.count()
        
        if count == 0:
            return "No momento, não há produtos cadastrados no sistema."
        
        if "quantos" in message or "quantidade" in message:
            return f"Atualmente temos {count} produto(s) cadastrado(s) no sistema."
        
        # Lista alguns produtos
        produtos_list = produtos[:5]
        response = f"Temos {count} produto(s) cadastrado(s). Aqui estão alguns:\n\n"
        for produto in produtos_list:
            response += f"• {produto.nome} - R$ {produto.preço} ({produto.categoria.nome})\n"
        
        if count > 5:
            response += f"\n... e mais {count - 5} produtos."
        
        return response
    
    def _category_query(self, message):
        """Consulta sobre categorias"""
        categorias = Categoria.objects.all()
        count = categorias.count()
        
        if count == 0:
            return "No momento, não há categorias cadastradas no sistema."
        
        response = f"Temos {count} categoria(s) cadastrada(s):\n\n"
        for categoria in categorias:
            produto_count = categoria.produto_set.count()
            response += f"• {categoria.nome} ({produto_count} produto(s))\n"
        
        return response
    
    def _search_product(self, message):
        """Busca produto pelo nome"""
        # Extrai o termo de busca
        patterns = [
            r'buscar\s+(.+)',
            r'procurar\s+(.+)',
            r'encontrar\s+(.+)',
        ]
        
        search_term = None
        for pattern in patterns:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                search_term = match.group(1).strip()
                break
        
        if not search_term:
            return "Por favor, especifique o que você gostaria de buscar. Exemplo: 'buscar notebook'"
        
        # Busca produtos que contenham o termo
        produtos = Produto.objects.filter(nome__icontains=search_term)
        
        if not produtos.exists():
            return f"Não encontrei nenhum produto com '{search_term}'. Tente outro termo de busca."
        
        response = f"Encontrei {produtos.count()} produto(s) com '{search_term}':\n\n"
        for produto in produtos:
            response += f"• {produto.nome} - R$ {produto.preço} ({produto.categoria.nome})\n"
        
        return response
    
    def _price_query(self, message):
        """Consulta sobre preço de produto"""
        # Tenta extrair o nome do produto
        patterns = [
            r'preço\s+(?:de|do|da)?\s*(.+)',
            r'preco\s+(?:de|do|da)?\s*(.+)',
            r'valor\s+(?:de|do|da)?\s*(.+)',
            r'quanto\s+custa\s+(?:o|a)?\s*(.+)',
        ]
        
        product_name = None
        for pattern in patterns:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                product_name = match.group(1).strip().rstrip('?')
                break
        
        if not product_name:
            return "Por favor, especifique qual produto você quer saber o preço. Exemplo: 'Qual o preço do notebook?'"
        
        produtos = Produto.objects.filter(nome__icontains=product_name)
        
        if not produtos.exists():
            return f"Não encontrei nenhum produto chamado '{product_name}'."
        
        if produtos.count() == 1:
            produto = produtos.first()
            return f"O produto '{produto.nome}' custa R$ {produto.preço}."
        
        response = f"Encontrei {produtos.count()} produtos:\n\n"
        for produto in produtos:
            response += f"• {produto.nome} - R$ {produto.preço}\n"
        
        return response
    
    def _list_all_products(self):
        """Lista todos os produtos"""
        produtos = Produto.objects.all()
        
        if not produtos.exists():
            return "No momento, não há produtos cadastrados no sistema."
        
        response = f"Lista completa de produtos ({produtos.count()} itens):\n\n"
        for produto in produtos:
            response += f"• {produto.nome} - R$ {produto.preço} ({produto.categoria.nome})\n"
        
        return response
    
    def _default_response(self):
        """Resposta padrão quando não entende a pergunta"""
        return (
            "Desculpe, não entendi completamente sua solicitação. "
            "Tente perguntar sobre produtos, categorias, preços ou digite 'ajuda' "
            "para ver o que posso fazer por você."
        )
