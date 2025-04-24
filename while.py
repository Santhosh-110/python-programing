# a=0
# while(a<10):
#     a=a+1
#     print(a)

# print("****Multiplication table*****")
# a=int(input("Enter the multiplication table: "))
# i=0
# while(i<10):
#     i=i+1
#     print(i,"*",a,"=",(i*a))



#   #factorial  
# a=int(input("Enter the length"))
# n=1
# while(a>=1):
#     n=n*a
#     a=a-1
#     print(n)

# a=int(input("enter the no: "))
# i=1
# while(i<a):
#     if(a%1==0)and(a%a==0):
#          i=i+1
#          print(i)
#          break
# a=list(map(int,input("Enter the number")))
# print(a)
# i=1
# while a>i:
#     print(i.reverse())

# n=int(input("enter the length"))
# i=1
# s=n
# b=""
# i=len(s)-1 #6-1=5
# while i>=0:
#     b=b+s[i]
#     i-=1
# print(b)
    
    
#     # Example with sets
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# # Using the intersection() method
# intersection = set1.intersection(set2)
# print(intersection)  # Output: {3, 4}

# # Or using the & operator
# intersection = set1 & set2
# print(intersection)  # Output: {3, 4}


# # while loop using sum
# a=int(input("Enter the num: "))
# sum=0
# current=1
# while current<=a:
#   sum=sum+current
#   current = current+1
# print(f"The sum of number is:{sum} ")

# # count the number
# n=int(input("Enter the number: "))
# count=0
# while n>0:
#   n//=10
#   count+=1
# print(count)

# # reverse a number
# n=int(input("Enter the number: "))
# rev_num=0
# while rev_num<n:
#   digit=n%10
#   rev_num=rev_num*10+digit
#   n//=10
#   rev_num=rev_num-1
# print(f"Reverse a num:{rev_num}")

# # fibonacci program
# n=int(input("enter the no: "))
# count=0
# a,b=0,1
# while n>count:
#   print(a,end="")
#   a,b=b,a+b
#   count+=1

# # sum of digit
# n=int(input("Enter the number: "))
# sum_digit=0
# while n>0:
#   digit=n%10
#   sum_digit=digit+1
#   n//=10
# print(f"The sum of digit: {sum_digit}")

# # countown program
# n=int(input("Enter the number to countown start: "))
# while n>0:
#   print(n)
#   n-=1
