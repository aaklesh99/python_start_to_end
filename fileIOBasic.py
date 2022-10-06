# File IO Basic
"""
"r" - open file for reading
"w" - open file for writing
"x" - Creates file if not exits
"a" - Add more content to file
"t" - text mode - Default mode
"b" - Binary mode
"+" - Read and Write both
"""


# f = open("Akki.txt")
# # content = f.read()
# print(content)

# for line in f:
#     print(line,end=" ")
# content = f.read(10)
# print(content)
#
# content =f.read(10)
# print(content)

# print(f.readline())
# print(f.readline())
# print(f.readlines())
# f.close()


#  write mode

# f=open("LPU.txt","w")
# f.write("Lovely Professional University")
# f.close()

#Append mode

# f=open("LPU.txt","a")
# a=f.write("Lovely Professional University\n")
# print(a)
# f.close()

#Read and write mode
f=open("LPU.txt","r+")
a=f.write("Lovely Professional University\n")
print(a)
print(f.read())
f.write("Thanks")

f.close()
