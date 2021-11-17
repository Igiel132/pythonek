#ZADANIE 1
def wielokrotnosc(x):
    lista = [x, 2*x, 3*x, 4*x, 5*x]
    return lista
#print(wielokrotnosc(4))

#ZADANIE 2
def przedial(x,y):
    lista=[]
    for i in range(x,y+1):
        lista.append(i)
    return lista
#print(przedial(4,6))

#ZADANIE 3
def malejace(x,y):
    lista=[]
    i=y
    while i>=x:
        if (i % 2 == 1):
            lista.append(i)
        i-=1
    return lista
#print(malejace(3,18))    

#ZADANIE 4
def kwadrat(n):
    tablica = []
    if(n!=1):
        for i in range(1,n):
            tablica.append(i*i)
        return tablica
    else:
        return tablica
#print(kwadrat(5))

#ZADANIE 5
def dzielnik(n):
    tablica = []
    for i in range(1,n):
        if(n%i==0):
            tablica.append(i)
    return tablica
#print(dzielnik(15))