# remember counting starts at 0
for row in range(5):#0,1,2,3,4
    if row%2 == 0:
        for column in range(1,6): #1,2,3,4,5
            if column%2 == 1:
                if column != 5:
                 print(' ',end='')#1,3
                else:
                    print(' ')#5
            else:
                print('|',end='')#2,4    
        # print(' | | ')
        #      12345  
    else:
        print('-----')    

        x = 2
        for i in range(x):
            for j in range(x):
                a = x - j + i
                print(a)



f = 1
A = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
for i in range(0, 3):
     f =f*i
     for j in range(0, 3):
         A[i][j] = f
print(A)


for row in range(5):                           
    if row%2 == 0:                 
        print(row)