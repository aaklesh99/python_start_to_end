n=15
#n=int(input("Enter any number : "))
while(True):
    num=int(input("Try again,Enter number : "))
    if(num<n):
        print("Enter greater number\n")
    elif(num>n):
        print("Enter lower no.\n")
    else:
        print("Congratulation you guessed the number.\n")
        break


