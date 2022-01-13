'''Find all the numbers from M to N that satisfy the following conditions.
      i. Take a number Z and add all its digits to get a number X.
      ii. Now reverse the number X to get Y.
      iii. if we multiply X and Y you should get back Z.'''
      
def func(x):
    sum=0
    rev=0
    n=x
    while (n!=0):
        rem=n%10
        sum=sum+rem
        n = n//10
    n=sum
    while (n!=0):
        rem=n%10
        rev=(rev*10)+rem
        n =n // 10
        
    return sum*rev==x
m=int(input())
n=int(input())
for i in range (m,n+1):
    if (func(i)):
        print(i)
