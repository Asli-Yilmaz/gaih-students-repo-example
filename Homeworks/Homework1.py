#Generating a 3x3 matrix with random prime numbers. 
import random as rnd
matrix=[]
for i in range(3):
    row=[]
    number=0
    #'number' veriable count the numbers in a row.To create a 3x3 matrix, number must be 3.    
    while number!=3:
        n=rnd.randint(0,100)
        if(n<2):continue
        elif(n==2 or n==3 or n==5 or n==7):
            row.append(n)
            number+=1
        elif(n%2==0 or n%3==0 or n%5==0 or n%7==0):continue       
        else:
            row.append(n)
            number+=1
    matrix.append(row)
    #adding row list into the matrix list
for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print()
#display the numbers. 
