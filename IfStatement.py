# input is a function the will promet the user to input a value to the conseul 
#n = input("Choose a number between 1 - 10 and enter it here: ")

# we reassen the value of n after the user input
##n= int(n)

# using if statment if the value that the user input is less than 5 than thi smessage will despilay 
#if n <5:
    #print("The number you chose is less than d.")

print("Welcome to our app ")

name = input("What is your name? ")
name= str(name)
age = input("How old are you? ")
age = int(age)
if age < 5:
    #print((name), ("You are "),(age), ("years old and you are a baby"))
    print(f"{name}, You are {age} years old and you are a baby")

elif age >= 5 and age <11:
    print((name), ("You are "),(age), ("years old and you are a child"))
elif age >= 11 and age <20:
    print((name), ("You are "),(age), ("years old and you are a teen"))
elif age >= 20:
    print((name), ("You are "),(age), ("years old and you are an adult"))
# elif:
#     print("please enter a valad number ")    

print("Thank you for using our app")

