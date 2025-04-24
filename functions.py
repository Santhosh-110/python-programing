# default argument
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

# task using functions
a=int(input("Enter the no 1:"))
b=int(input("Enter the no 2: "))
c=int(input("Enter the no 3: "))
sum=0
def posti():
    if a>sum:
        print("1 is Positive no")
    elif b>sum:
        print("2 is positive no:")
    elif c>sum:
        print("3 is Positive no")
    # else:
    #     print("Negative")
def neg():
    if a<sum:
        print("1 is Negative no")
    elif b<sum:
        print("2 is Negative no:")
    elif c<sum:
        print("3 is Negative no")
def zero():
    if a==sum:
        print("1 is Zero")
    elif b==sum:
        print("2 is Zero")
    elif c==sum:
        print("3 is Zero")
posti()
neg()
zero()

a=int(input("Enter the no 1: "))
b=int(input("Enter the no 2: "))
def add():
    print("Addition: ",(a+b))
def sub():
    print("Subtraction: ",(a-b))
def mul():
    print("Multiplication: ",(a*b))
def div():
    print("Divition: ",(a//b))
add()
sub()
mul()
div()


# task 10
def info(name,age,city):
    print(f"My name is {name},i am {age} years old and i live in {city}")
info("santhosh",21,"pudukkottai")

# task 7
def greet(name):
    print(f"hello{name}")
greet(" Santhosh!")

def sym():
    a=int(input("enter the number: "))
    b=int(input("Enter the number: "))
    return a+b
sum=sym()
print(sum)

# task 9
def wel(name,mes="Welcom!"):
    print(name,mes)
wel("Santhosh")

def fact():
    n=int(input("Enter the number: "))
    if n<0:
        print("the factorial num is not defined negative value!")
    else:
        facto=1
        i=1
        while n>=i:
            facto*=i
            i+=1
        print(f"The factorial {n} is {facto}")     
fact()    



def add(n):
    if n<=0:
        return
    print(n)
    add(n-1)
add(5)
def lam(a,b):
    result=lambda a:a*b
    print(result(a))
lam(10,10)

# task no 15    
def a(n):
    return lambda b:b*n
c=a(7)
print(c(3))
  
  
#   palindrome program part-1
def palindrome():
    s="wordpad"
    print(s)
    a=s[::-1]
    print(a)
    if s[0]==a[0] or s[1]==a[1] or s[2]==a[2] or s[3]==a[3] or s[4]==a[4] :
        print("is palindrome")
    else:
        print("not palindrome")
palindrome()