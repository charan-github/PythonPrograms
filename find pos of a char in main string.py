main=input('enter main string:')
sub=input('enter sub string :')
i=0
l=len(main)
while(i<l):
    if(main[i]==sub):
        print("found at pos",i)
    i=i+1 

