import os
s = int(input("Podaj średnią wieku: "))
x = int(input("Podaj wiek najmłodszej osoby: "))
y = int(input("Podaj wiek najstarszej osoby: "))
k = (3*s) - x - y
print("Trzecia osoba ma",k,"lat")
os.system("PAUSE")