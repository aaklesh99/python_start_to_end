import time

# initial =time.time()
# print(initial)
#
# k=0
# while(k<45):
#     print("Akki Raj")
#     k+=1
# print("While loop run time ",time.time()-initial,"seconds")
#
# initial2=time.time()
# for i in range(25):
#     print("Akki Raj")
# print("For loop run time ",time.time()-initial2,"seconds")

currenttime=time.asctime(time.localtime((time.time())))
print(currenttime)
