def checkSize(produto):
    
    if len(produto) < 1:
        print("Primeior")
        return False
    
    if len(produto) >= 255:
        print("Segundo")
        return False
    
    if len(produto) > 1 and len(produto) < 255:
        print("Terceiro")
        return True
    
    