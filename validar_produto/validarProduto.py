import re
from datetime import datetime

def checkSize(produto):
    if len(produto) <= 1:
        return 'O produto não pode ter apenas 1 caractere', False
    
    if len(produto) >= 255:
        return 'ERRO: Produto com muitos caracteres', False
    
    return True

def checkCategory(marketplace):
    if marketplace == 'Selecione uma opcão': return 'Opção invalida', False
    if marketplace == 'Mercado Livre': return True
    if marketplace == 'Amazon': return True
    if marketplace == 'Olist': return True
    if marketplace == 'Magalu': return True
    if marketplace == 'Loja Virtual': return True
    else:
        return 'O produto deve estar na categoria', False
    
def checkProdut(produto):
    if produto == 'Moldura Interativa': return True
    if produto == 'Lousa Interativa': return True

    else:
        return 'Produto não disponivel', False
        
def checkFornecedor(loja):
    if loja == 'Brasil Touch Audiovisuais': return True
    if loja == 'Show de Imagem Audiovisuais': return True

    return False