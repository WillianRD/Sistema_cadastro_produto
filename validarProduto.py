import re
from datetime import datetime

def checkSize(produto):
    if len(produto) <= 1:
        return 'O produto não pode ter apenas 1 caractere', False
    
    if len(produto) >= 255:
        return 'ERRO: Produto com muitos caracteres', False
    
    return True

def checkCategory(categoria):
    if categoria == 'Selecione uma opcão': return 'Opção invalida', False
    if categoria == 'Alimentos': return True
    if categoria == 'Bebidas': return True
    if categoria == 'Roupas': return True
    if categoria == 'Tecnologia': return True 
    if categoria == 'Saúde': return True
    
    else:
        return 'O produto deve estar na categoria', False
    
def checkPrice(preco):
    preco = float(preco)
    if preco < 0.0:
        return 'Preço não pode ser igual a R$ 0.0', False
    
    elif preco > 9.999:
        return 'Valor muito alto para o produto', False
    
    return True

def checkDesc(descricao):
    
    if len(descricao) == 0:
       return 'Vocẽ não adicionou uma descrição', False
    
    if len(descricao) < 10:
        return 'Descrição muita pequena', False
    
    if len(descricao) > 255:
        return 'Descriçaõ muito grande', False
    
    if len(descricao) != 0:
        return 'Descrição: OK' , True
    
    return True

def checkSizeEstoque(estoque):
    
    conversao = int(estoque)
    
    if conversao > 0: return True
    if conversao == 0: return True
    if conversao < 0: return 'Valor não pode ser negativo'
    
    return False

def checkFornecedor(fornecedor):
    pattern = r"^[A-Za-zÀ-ÿ\s'-]+$"
    
    if re.match(pattern, fornecedor):
        return "Fornecedor OK", True
    
    return False

def caracteres(caracteres):
    if len(caracteres) == 0: return 'Nenhuma caracteristicas foi adicionada', False
    if len(caracteres) < 5: return 'Adicione pelo menos uma caracteristica do produto', False
    if len(caracteres) > 5 and len(caracteres) < 255: return True
    
    return False

def url(url_link):
    if len(url_link) == 0: return 'Link vazio', False
    if len(url_link) > 5 and len(url_link) < 5000: return True
    if len(url_link) > 5000: return 'Link muito grande', False
    
    return True  