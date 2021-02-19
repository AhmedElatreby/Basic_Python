raining = input("Is it raining? (yes/no)")
umbrella = input("Do you have an umbrella? (yes/no)")
if raining == "yes" and umbrella == "yes":
    print("Don't forget your umbrella when you go out! ")
elif raining == "yes" and umbrella == "no":
    print("Wear a waterproof jacket when you go out!")    


# second example
x = input("Enter a number here: ")
x = float(x)
if x < 2:
    print("The number is less than 2. ")
elif x < 6:
    print("The number is less than 6.")    
elif x < 8:
    print("The number is less than 8.")    
elif x < 10:
    print("The number is less than 10.")  


# Thired example
x = 1
print(float(x))   

# Fourth example
# input is -4 --> absolute value is 4 (4 is -1 * -4)
# input is 0 --> absolute value is 0
# input is 86.4 --> absolute value is 86.4

def abs_val(num):
    if num < 0:
        return -num
    elif num == 0:
        return 0
    else:
        return num     

result = abs_val(-5)
print(result)

result = abs_val(0)
print(result)   

result = abs_val(99.9)
print(result)           