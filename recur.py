
# def fact_iterative(n):
#     fact = 1
#     for i in range(n):
#         fact=fact*(i+1)
#     return fact

# def fact_recursion(n):
#     if n==1:
#         return n
#     else:
#         return n*fact_recursion(n-1)
#
#
# num=int(input("Enter no. : "))
# # fact_iterative(num)
# # print("Factorial using iteratictve : ",fact_iterative(num))
# print("Factorial using recursion : ",fact_recursion(num))


def fabonacci(n):
    num1=0
    num2=1
    print(num1,end=" ")
    print(num2,end=" ")
    for i in range(1,n-1):
        sum = num1 + num2
        print(sum,end=" ")
        num1=num2
        num2=sum
    return sum

# def fabonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fabonacci(n-1)+fabonacci(n-2)

number= int(input("Enter number : "))
fabonacci(number)
