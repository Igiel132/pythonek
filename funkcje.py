#Zad 1
def petla():
    x=2
    while(x<=8):
        print(x)
        x+=1
petla()


#Zad 2 
def funkcja(a,b,c,d,e,f):
    x=[a,b,c,d,e,f]
    return x
trzy=funkcja(1,5,6,3,6,7)
print(trzy)


#Zad 3
def function(tekst,znak):
    if(znak in tekst):
        print("Znalazłem w tym tekście "+znak)
    else:
        print("Nie znalazłem w tym tekście "+znak)
function("quick brown fox jumps over a lazy dog","do")


#Zad 5
def obj(a,h):
    if(a>0 and h>0):
        obj=a*a*h
        return obj
    else:
        print("taki graniastosłup nie istnieje")
        return 0
x=obj(0,5)
print(x)

