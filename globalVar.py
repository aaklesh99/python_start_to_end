# a=10 #Global
# print(a)
#
# def func(name):
#     b=15 #Local
#     print(a,b)
#     print("Raj")
#
# func("This is Akki")
# # print(b) # Cannot print
# print(a)
def Akki():
    x=99
    def Raj():
        global x
        x=100
    print(x)
    Raj()
    print(x)

Akki()

