import os
a = int(input("Podaj szerokość paneli: "))
b = int(input("Podaj długość paneli: "))
x = int(input("Podaj powierzchnie domu: "))
k = x/(a*b)
print("Potrzebujesz",k,"paneli!")
os.system("PAUSE")