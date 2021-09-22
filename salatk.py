import os
print("Dla ilu osób jest przepis?")
o1 = int(input("Podaj liczbę: "))
print("Ile składników jest potrzebne dla",o1,"osób?")
s1 = int(input("Podaj liczbę: "))
print("Ile bedzię osób?")
o2 = int(input("Podaj liczbę: "))
s2 = (o2/o1)*s1
print("Musisz użyć",s2,"składników!")
os.system("PAUSE")