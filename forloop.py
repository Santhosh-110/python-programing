n=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*(i-1)+1))

n=5
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))

n=5
for i in range(1,5):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(n,0,-1):
        print(" "*(n-i)+"*"*(2*i-1))

n=5
for i in range (1,n+1):
   for j in range (1,i+1):
        print(" "*(n-i),end="") 
        print (j ,end="")
   print()

n=5
m=1
for i in range(1,n+1):
 for j in range(1,i+1):
    print(m,end=" ")
    m+=1
 print()

n=5
for i in range(1,n+1):
    for j in range(2,n+1):
        print()

n=5
m=15
for i in range(0,6):
    print(i)
for j in range(i,16):
    print(j)
print()
a=input()
b=input()

if(a=="w" or b=="w"):
    print("present")
else:
    print("not present")
a=int(input("enter the no: "))
for a in range(1,11):
    if(a%2==0):
        print()
    else:
        print(a)
a=input("Enter the no")
for i in a:
    
    if a==5:
        break