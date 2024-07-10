# testList = ['element 1','element2','element3']
# testList - [0,1,2]


scores = [70,85,67.5,90,80]

# print(scores[2])  #remember counting starts from 0
# print(scores[-0]) #this minus method counts from the right starting at 0 on the left then jumps to 1 on the right
# print(scores[0:2])#this means upto but not including element at index 2
# print(scores[2:]) #this starts at index position 2 to the end of the list/array

# to assign a differnt value to a list. List can contain diffent data types such as interger or strings
# scores[0] = 75

# print(scores)

# To remove data from a list
# scores[1:3] = [] #this example shows the start poinnt of index 1 up to but not including index 3. This removes the data from those index positions in the  list

print(scores)

# To add another list within a list
# scores[2] = ['Hello','World']

# print(scores)
# print(scores[2]) 
# print(scores[2][0]) #to access an element within an element use another set of[]

# To add data to a list
scores.append(82)

print(scores)