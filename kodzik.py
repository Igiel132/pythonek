pesel = int(input("Podaj pesel: "))
x = pesel // 100
x *= 100
y = pesel - x #wyciąga dwie ostatnie liczby pod y
z = y // 10
print(z)
if (z % 2 == 0 ):
    print("Jesteś kobietą!")
else:
    print("Jesteś mężczyzną")

#x = int(input("Podaj liczbę punktów zdobytych przez klasę: "))
#y = float(input("Podaj średnią frekwencje: "))
#z = float(input("Podaj średnią klasy: "))
#if(y > 94 and z > 5):
#    x += 20
#    print("Klasa posiada", x, "punktów!")
#else:
#    print("Klasa posiada", x, "punktów!")