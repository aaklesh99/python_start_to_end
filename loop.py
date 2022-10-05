# list1={"Akki","Aklesh","Ashish","Nitish"}
# for item in list1:
#     print(item)

list2={"int","float","Akki",2,52,1324,35,54,2,56}
for item in list2:
    if str(item).isnumeric() and item>6:
        print(item)