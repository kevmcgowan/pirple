# while (condition):
#     Action
#     Action2
#     Action3


# counter = 1
# sum = 0 
# while (counter<=10):
#     print(counter)
#     sum = sum + counter
#     counter = counter + 1
# print (sum)


# letters = ['a','b','c','d','e']

# index = 0

# while (index < len(letters)):
#     print(index)
#     print(letters[index])
#     index = index + 1


height = 5000
velocity = 0.49

time = 0
while (height>0):
    height = height - velocity
    time = time + 0.01

print(height)
print(time)