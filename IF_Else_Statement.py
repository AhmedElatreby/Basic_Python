def minimum(x, y):
    if x < y:
        return x
    else:
        return y    

# test this function on the inputs 2 and 5
result = minimum(2, 5)
print(result)

# test this function on the inputs -2 and -5
result = minimum(-2, -5)
print(result)

# test this function on the inputs 6 and 6
result = minimum(6, 6)
print(result)

# test this function on the inputs 2 and 6.5
result = minimum(2, 6.5)
print(result)
