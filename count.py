
l=int(input("size"))
f=[]
count=0
for i in range(0,l):
    a=input("enter name")
    f.append(a)
    for x in a:
        if x in ("a"):
            count+=1

print(f)
print("count",format(count))
    

    
    
