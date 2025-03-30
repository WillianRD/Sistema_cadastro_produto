def checkSize(produto):
    if len(produto) <= 1:
        print("Primeior")
        return False
    
    if len(produto) >= 255:
        print("Segundo")
        return False
    
    return True
    
    