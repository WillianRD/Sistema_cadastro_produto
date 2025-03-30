def checkDesc(descricao):
    if len(descricao) == 0:
        return False
    
    if len(descricao) < 10:
        return False
    
    return True