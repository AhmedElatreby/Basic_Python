# you can store a lise of number in python using sequence
# List( has a specific order, and the list can be changed anytime)
# Square brackets[] enclose items in the list
# Commas separate the items from each other

# create a list and we called listA
from typing import Type


listA = [5, 10, 15, 20, 25]
print(listA)

# if you want to check data type in listA we use type(listA) the out come will be list
print(type(listA))

# if you want to access an item from the list we use []
print(listA[0])
print(listA[1])
print(listA[2])

# We can change the value inside the list as well for example listA[0] = 1000
listA[0] = 1000
print(listA[0])

# A list can hold more than one date type

listB = [0, 1.2, "Ahmed", True ]
print(listB)


