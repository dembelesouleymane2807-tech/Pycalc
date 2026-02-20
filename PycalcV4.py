def pypacalc(n1:int ,O:str,n2:int):
    if O=="+":
        cal=n1+n2
    elif O=="*":
        cal=n1*n2
    elif O=="/":
        cal=n1/n2
    else:
        cal=n1-n2
    return cal