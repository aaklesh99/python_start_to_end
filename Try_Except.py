print("Enter first no. : ")
num1 = input()
print("Enter Second no : ")
num2=input()
try:
    print("The sum of two number is : ",int(num1)+int(num2))
except Exception as invalid:
    print(invalid)
print("this is example of try exception ")