s=input("enter string")
l=len(s)
i=l-1
while(i>=0):
    print(s[i],end='')
    i=i-1
    
''' or '''

print(s[-1:-(l+1):-1])
