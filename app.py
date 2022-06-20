from func import say
from func import hello
from func import loop

# print(hello())

# name = str(input("masukkan namamu: "))

# print(say(name))

loop = int(input("masukkan nilai loop: "))
number = 1

names = []

while number <= loop:
    name = str(input("masukkan nama: "))
    names.append(name)
    number += 1

loop(names)