import random
n=random.randint(0,100)
a=-1
gusues=1
while(a!=n):
    a=int(input("Enter The Number"))
    if(a>n):
        print("Lower the number ")
        gusues+=1
    
    elif(a<n):
        print("Higher Number plz") 
        gusues+=1
    
print(f"Your correct gusues is {a} and no. of guesus is {gusues}")
