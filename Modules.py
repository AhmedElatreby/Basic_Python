# importing claender
import calendar

# importing math
import math

# importing random
import random

# create a variable named cal
# calender.month is a fenction take the year and month as input and retuen this calender for this month
print("showing calendar using cal function")
cal = calendar.month(2021, 2)

# running this with print
print(cal)

print("---------------------------------")
print("using math to show square")

# create a variable name result
result = math.sqrt(49) # this will return the square rote of 49

print(result)

print("---------------------------------")
print("random numbers")

# create a variable named number
number = random.randint(1, 100) # random.random is a function takes in two integers 

print(number)

print("---------------------------------")
print("random using array")

# use random from array
movies = ["Black Panther(2018)", "Lady Bird(2017)", "Mission: Impossible - Fallout(2018)", "Mission: Impossible - Fallout(2018)", "Get Out(2017)", "Mad Max: Fury Road(2015)", "Spider-Man: Into the Spider-Verse(2018)", "Moonlight(2016)", "Wonder Woman(2017)" ]

watch = random.choice(movies)
print(watch)
print("---------------------------------")


print("Random shuffle")

# using random to rearange the order of list
print("---------------------------------")
deck = ["Ace", "One", "Two", "Three", "Four", "Five", "six", "Seven", "Eight", "nine", "Ten", "Jack", "Queen", "King"]
print(deck)

random.shuffle(deck)
print(deck)
print("---------------------------------")
