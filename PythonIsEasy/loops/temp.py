# word = 'Hello'

# letter = []

# number = 1,2,3,4,5,6

# for w in word:
#     print(w)
#     if w == 'e':
#         print('what a funny letter')
    
#     letter.append(w)

# print(letter)



# for n in number:
#     print(n)

# for num in numbers:
#     print(num)

# for l in letter:
#     print(l)

# Modulus: dives by the numbers then prints the remainder
# 1%2 = 1
# 2%2 = 0
# 3%2 - 0

# numbers = [1,2,3,4,5]

# for l in numbers:
#     if 1%2 == 1:
#         print(l)
# range (start, stop & steps) stopping value is not inclusive

numbers = []

# to add all numbers to a list
# for num in range(10):
#     numbers.append(num)
#     print(num)

# print(numbers)

# to only add selcted ranges to a list. Shown below is all the odd numbers form a range starting at 0
for num in range(0,10,2):
    numbers.append(num)
    print(num)

print(numbers)