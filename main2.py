""" A program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10."""

from random import randint

list = []
s = 0
while s < 4:
    s = s + 1
    x = randint(0, 1)
    list.append(x)
base_10_value = list[0] * 2**3 + list[1] * 2**2 + list[2] * 2**1 + list[3] * 2**0
print(f"The generated digits are {list}")
print(f"The converted value in base 10 is {base_10_value}")





