import math as math

X = int(input("Amount of people: "))

print(f"A chance de {X} pessoas fazerem aniversário no mesmo dia é de " + (str(100 - (math.factorial(365)/(365 ** X * math.factorial(365 - X))) * 100))+"%")
