# def func():
#     print("This is first")
# func()
#
# func2=func
# del func
# func2

# def dec(fun):
#     if fun==0:
#         return print
#     if fun==1:
#         return sum
# a=dec(0)
# print(a)

def dec1(num):
    def def2():
        print("Executin now")
        num()
        print("Executed")
    return def2
@dec1
def who_is_akki():
    print("He is Aklesh")

# who_is_akki=dec1(who_is_akki)
who_is_akki()


