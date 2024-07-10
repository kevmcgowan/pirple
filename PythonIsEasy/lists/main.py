# # Define the global variable myUniqueList
# myUniqueList = []

# # Define the function to add elements to myUniqueList
# def add_to_unique_list(item):
#     if item not in myUniqueList:
#         myUniqueList.append(item)
#         return True
#     else:
#         return False

# # Testing the function with different scenarios
# print(add_to_unique_list(5))      # Expected: True, as 5 is not in the list
# print(add_to_unique_list(10))     # Expected: True, as 10 is not in the list
# print(add_to_unique_list(5))      # Expected: False, as 5 is already in the list
# print(add_to_unique_list("hello"))# Expected: True, as "hello" is not in the list
# print(add_to_unique_list(10))     # Expected: False, as 10 is already in the list

# # Print the value of myUniqueList to show that it worked
# print(myUniqueList)               # Expected: [5, 10, 'hello']


# Define the global variable myUniqueList
myUniqueList = []

# Define the global variable myLeftovers
myLeftovers = []

# Define the function to add elements to myUniqueList or myLeftovers
def add_to_unique_list(item):
    if item not in myUniqueList:
        myUniqueList.append(item)
        return True
    else:
        myLeftovers.append(item)
        return False

# Testing the function with different scenarios
print(add_to_unique_list(5))      # Expected: True, as 5 is not in the list
print(add_to_unique_list(10))     # Expected: True, as 10 is not in the list
print(add_to_unique_list(5))      # Expected: False, as 5 is already in the list
print(add_to_unique_list("hello"))# Expected: True, as "hello" is not in the list
print(add_to_unique_list(10))     # Expected: False, as 10 is already in the list

# Print the value of myUniqueList and myLeftovers to show that it worked
print(myUniqueList)               # Expected: [5, 10, 'hello']
print(myLeftovers)                # Expected: [5, 10]
