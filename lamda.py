#Lamda function

# minus = lambda x,y : x-y
#
# def minus(x,y):
#     return x-y
#
# print(minus(9,4))

def a_sort(x):
    return x[1]

a=[[1,5],[4,8],[6,6]]
# a.sort(key=lambda x:x[1])
a.sort(key=a_sort)
print(a)