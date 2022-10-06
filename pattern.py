row=int(input("Enter no. of row :  "))
print("Enter 0 or 1 : ")
check = input("Enter value : ")
new = bool(check)
if new==True:
    for i in range (1,row+1):
        for J in range(1,i+1):
            print("*",end=" ")
        print()
if new==False:
    for i in range(1, row):
           for J in range(row, i, -1):
               print("*", end=" ")
           print()
#
#


