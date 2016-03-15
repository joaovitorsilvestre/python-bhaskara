### Biblioteca para calcular bhaskara, triangulo retangulo

def bhaskara(a,b,c):
    delta = (b**2) - 4*a*c
    if delta < 0:
        return('error')
    else:
        x1 = (-b+(delta**0.5))/2*a
        x2 = (-b-(delta**0.5))/2*a
        return(x1,x2)

def pitagoras(a,b):
    c = ((a**2)+(b**2))**0.5
    return(c)

def porcentagem(porcem, num):
    return (num*(porcem/100))
