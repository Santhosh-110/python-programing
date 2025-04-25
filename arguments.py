def name(x,y=50):
    print("X",x)
    print("Y:",y)
name(30)

def student(fname,lname):
    print(fname,lname)
student(fname='hello', lname='world')
student(lname='world',fname='hello')



def adder(*num):
    sum=0
    for n in num:
        sum=sum+n
    print("Sum",sum)
adder(3,5)
adder(1,2,3,4,5)
adder(4,5,6,7)


# posisonal argument:
def nameAge(name,age):
    print("hii iam ",name)
    print("my age is",age)
print("Case-1")
nameAge("santhosh",23)
print("Case-2")
nameAge("Rohan",21)

def intro(**data):
    print("\n Data type of argument: ",type(data))
    for key,value in data.items():
        print("{} is {}".format(key,value))
intro(fname="sita",lname="sharma",age=22,phone=123456)
intro(fname="jhon",lname="wood",email="jhonwood@gmail.com",country="Wakknad",Age="25",phone="9360445369")

# hollo square pattern
a=5
for i in range(1,a+1): 
    for j in range(1,a+1):
        if i==1 or i==a or j==1 or j==a:
            print("*",end="  ")
        else: 
            print(" ",end="  ")
    print()
