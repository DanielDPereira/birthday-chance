import math as math

X = int(input("Amount of people: "))

print(f"The chance that {X} people have the same birthday is " + (str(100 - (math.factorial(365)/(365 ** X * math.factorial(365 - X))) * 100))+"%")
