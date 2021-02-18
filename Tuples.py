# Tuple has a specific order and cannot be changed once created
Shahd = ("Saudi Arabia", "Hospital", "Ryiadh", "06/05/2013")
Jana = ("Egypt", "Hospital", "Cairo", "17/11/2015")
Sarah = ("England", "Hospital", "Poole", "14/03/2018")
Yesmine = ("England", "Hospital", "Poole", "14/03/2018")

# you can use the type function to tell you which data type its
print(type(Shahd))

# printing Shahd
print(Shahd)

# access a specific item from tuple
print("Shahd's Birthday is on " + Shahd[3])

# we cannot change item in the tuple like list for example
Shahd[0] = "Egypt"
# the outcome will be (TypeError: 'tuple' object does not support item assignment)
