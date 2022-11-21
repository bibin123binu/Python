   

def w_count(a):
 words=a.split( )
 count=dict()                
 for w in words:
        if w in count:
            count[w]+=1
        else:
            count[w]=1
 print(count)
a=input("enter the string")
w_count(a)
