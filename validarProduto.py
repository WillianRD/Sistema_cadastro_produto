def checkSize(produto):
    if len(produto) <= 1:
        return False
    
    if len(produto) >= 255:
        return False
    
    return True

def checkPrice(preco):
    preco = float(preco)
    
    if preco == 0.0:
      return False
    
    return True

def checkDesc(descricao):
    if len(descricao) == 0:
        return False
    
    if len(descricao) < 10:
        return False
    
    if len(descricao) > 255:
        return False
    
    return True
    
    