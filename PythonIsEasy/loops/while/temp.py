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

participants = ['Jen', 'Alex', 'Tina', 'Joe', 'Ben', 'Tom']

position = 1

# for name in participants:
#     if name == 'Tina':
#         print('About to break')
#         break
#     print('About to increment')
#     position = position + 1

# print(position)

# index = 0

# for currentIndex in range(len(participants)):
#     print(currentIndex)
#     if participants[currentIndex] == 'Joe':
#         print('have breaked')
#         break
#     print('Not breaked')
#     # currentIndex = currentIndex + 1

# print(currentIndex+1)

for number in range(10):
    if number%3 == 0:
        print(number)
        print('is divisible by 3')
        continue
    print(number)
    print('not divisible by 3')






# height = 5000
# velocity = 0.49

# time = 0
# while (height>0):
#     height = height - velocity
#     time = time + 0.01

# print(height)
# print(time)