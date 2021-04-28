import random

def alternatywa(x, y):
    if (x == 1 and y == 1) or (x == 1 and y == 0) or (x == 0 and y == 1):
        return 1
    elif x == 0 and y == 0:
        return 0

def koniunkcja(x, y):
    if x == 1 and y == 1:
        return 1
    else:
        return 0

def implikacja(x, y):
    if x == 0 and y == 1:
        return 0
    else:
        return 1

p = random.randint(0, 1)
q = random.randint(0, 1)

print("p:", p, "q:", q)
print("alternatywa:", alternatywa (p, q))
print("koniunkcja:", koniunkcja (p, q))
print("implikacja:", implikacja(p, q))
