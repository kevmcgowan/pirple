length = 10
# if you use a number in the variable you must place it in "" or it will be treated as an interger and add, subtract, multiply or divide
toPrint = 'a'

# length goes upto but not including the stopping value, so use +1 to get the full range
for pos in range(1,length+1):
    print(toPrint*pos)
# remember to negative figure requires a comma 
# to aachieve the peak length need to start at 9 so use -1
for pos in range(length-1,0,-1):
    print(toPrint*pos)