def name(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(f"{key} is {value}")



lst=["Akki","mohan","Raj","Krish"]
normal="Hello I am aklesh Kumar"
dict={"Aklesh":"Student","Ashish":"Web developer","Shyam":"Java Develpoer"}
name(normal,*lst,**dict)