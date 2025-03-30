def checkSize(produto):
    if len(produto) <= 1:
        return False
    
    if len(produto) >= 255:
        return False
    
    return True
    
    