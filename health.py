#
print("Health Management Project\n")
def take(k):
    print("1. for Akki \n2. for Ashu\n3. for Abhi")
    code = int(input("Enter Name Code : "))
    print("1. for Dite\n2. for Exercise")
    code2 = int(input("Enter dite code : "))
    if (code == 1):
        if (code2==1):
            def dite():
                f=open("AkkiDite.txt","a")
                food=(input())
                f.write(food)
                print("Dite added Successfully ")
            return dite()
        elif code2 == 2:
            def exec():
                f=open("AkkiExec.txt","a")
                exec=(input())
                f.write(exec)
                print("Exercise added successfully")
            return exec()
        else:
            print("Invalid choice")
    elif code==2:
        if code2==1:
            def dite():
                f=open("AshuDite.txt","a")
                food=(input())
                f.write(food)
                print("Dite added Successfully ")
            return dite()
        elif code2==2:
            def dite():
                f=open("AshuExec.txt","a")
                exec=(input())
                f.write(exec)
                print("Exercise added successfully")
            return exec()
        else:
            print("Invalid choice")
    elif code == 3:
        if code2==1:
            def dite():
                f=open("Abhidite.txt","a")
                food=(input())
                f.write(food)
                print("Dite added Successfully ")
            return dite()
        elif code2==2:
            def dite():
                f=open("AbhiExec.txt","a")
                exec=(input())
                f.write(exec)
                print("Exercise added successfully")
                return exec()
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")

def show(k):
    print("1. for Akki \n2. for Ashu\n3. for Abhi")
    code = int(input("Name Code : "))
    print("1. for Dite\n2. for Exercise")
    code2 = int(input("Input dite code"))
    if code == 1:
        if code2 == 1:
            def dite():
                with open("AkkiDite.txt") as op:
                    print("Your Dite : ")
                    print(op.read())
            return dite()

        elif code2 == 2:
            def exec():
                f = open("AkkiExec.txt", "a")
                print("Your exercise : ")
                print(f.read())

        else:
            print("Invalid choice")
    elif code == 2:
        if code2 == 1:
            def dite():
                with open("AshuDite.txt") as op:
                    print("Your Dite : ")
                    print(op.read())

        elif code2 == 2:
            def dite():
                with open("AshuExec.txt") as op:
                    print("Your exercise : ")
                    print(op.read())
        else:
            print("Invalid choice")
    elif code == 3:
        if code2 == 1:
            def dite():
                with open("Abhidite.txt") as op:
                    print("Your Dite : ")
                    print(op.read())
        elif code2 == 2:
            def dite():
                # f = open("AbhiExec.txt", "a")
                with open("AbhiExec.txt") as op:
                    print("Your exercise : ")
                    print(op.read())
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")


k=int(input("1. for Log and 2. for Retrive : "))
if (k==1):
    take(k)
if(k==2):
    show(k)

