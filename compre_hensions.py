# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

#----------------List Comprehension-----------------

# ls=[i for i in range(100) if i%3==0]
#
# print(ls)

#---------------Dictonary Comprhension ---------------------------
# dict={i:f"item{i}" for i in range(100)}
# dict1={i:f"item{i}" for i in range(5)}
# dict2={value:key for key,value in dict1.items()}
# print(dict)
# print(dict1)
# print(dict2)

#-----------------------Set Comprhension ---------------------------

# dresses = {dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2","dress1","dress2"]}
# print(dresses)

#-----------------------Generator Comprhension --------------------------

# evens=(i for i in range(100) if i%2==0 )
# for i in evens:
#     print(evens.__next__())

#--------------------------Example of comprehensions-----------------

lst=[]
print( "Print how many items you want to insert : ")
a=int(input())
for i in range(a):
    items=input()
    lst.append(items)
# print(lst)
lists=[itm for itm in lst]
print(lists)