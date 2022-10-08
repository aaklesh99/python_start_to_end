
# ----------------------MAP------------------------

# lst =["23","32","23"]
#
# lst =list(map(int,lst))
# for item in range(len(lst)):
#     lst[item]=int(lst[item])
#     # print(lst)
# lst[2]=lst[2]+1
# print(lst)

# def sq(n):
#     return n*n
# num=[1,3,5,2,4,13]
# square=list(map(lambda x : x*x,num))
# print(square)
# for i in range:
#     print(sq(i))

# def sq(n):
#     return n*n
# def cub(n):
#     return n*n*n
# perform = [sq , cub]
#
# for i in range(10):
#     rslt=list(map(lambda x:x(i),perform))
#     print(rslt)

#-------------------------FILTER---------------------------

# num=[1,3,5,2,4,13,43,123,54,1,4]
# def is_greater_5(x):
#     return x>5
#
# big=list(filter(is_greater_5,num))
# print(big)

#----------------------------REDUCE---------------------
from functools import reduce

num=[1,3,5,2,4,13,43]
# sum=0
# for i in num:
#     sum=sum+i
# print(sum)

sum= reduce(lambda x,y:x+y ,num)
print(sum)
