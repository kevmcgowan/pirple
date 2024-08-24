participants = ['Jen','Alex','Tina','Joe','Ben']

# position = 1
# for name in participants:
#     if name == 'Alex':
#         print('About to break')
#         break
#     print('About to increment')
#     position = position + 1

# print(name,"\'s", "Position is:", position)
# print('Alex')



# for currentIndex in range(len(participants)):
#     print(currentIndex)
#     if participants [currentIndex ]== 'Joe':
#         print('have broke')
#         break
#     print('Have not broke')

# print(currentIndex+1)

for number in range(10):
    if number%3 == 0:
        print(number)
        print('Divisible by 3')
        continue
    print(number)
    print('Not divisible by 3')