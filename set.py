s=set()
print(type(s))
s.add(1)
s.add(2)
print(s)
s1=s.union({1,2,3})
#s1=s.intersection({1,2,3})

print(s,s1)