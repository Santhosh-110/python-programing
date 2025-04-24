
n=5
for i in range(1,n+1):
    for j in range(n-i):
        for j in range(i,15):
            j+=1
            print(j,end="")
print()
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    for j in range(i*1):
        print(j+1,end=" ")


a = 1
while a < 11:
    print(a)
    a += 1
    
n = int(input("enter a number"))
i = 1
b = 0
while i <= n:
    b += i
    i += 1
    print(f"{i}:{b}")

n=5
for i in range(1,n+1):
     for j in range(n-i):
        print(end=" ")
     for j in range(i*1):
        print(j+1,end=" ")
     print()
for i in range(n,0,-1):
     for j in range(n-i):
        print(end=" ")
     for j in range(i*1):
        print(j+1,end=" ")
     print()    
n=5
m=1
for i in range(1,n+1):
 for j in range(1,i+1):
    print(m,end=" ")
    m+=1
 print()
        


    
n=5
for i in range(1,3):
    print("*")
for j in range(2,4):
    print("*-"*(i))
print("*-*-*")
i+=1
    
n=5
m="*"
for i in range(1,3):
    print("*")
for j in range(1,3):
    print(m+"-"+m)
a=list((input("Enter the number: ").split()))
print(a)
a.pop()
print(a)

a=list(map(int,input("Enter the input:").split()))

print(a.index(5))

a=[1,2,3]
b=a*3
print(b)

a=[]       
a.extend([1,2,3]*3)
print(a)
