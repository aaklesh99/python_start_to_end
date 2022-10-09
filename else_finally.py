f1 = open("Akki.txt")
try:
    # f = open("doex.txt")
    f=open("doex2.txt")
except Exception as e:
    print("This is exception error", e)

except EOFError as e:
    print("This is EOF error" , e)

except IOError as e:
    print("This is IOE error" , e)

else:
    print("Else is run when except is not exits . ")

finally:
    print("Run anyway...")
    f1.close()

print("File Exits")