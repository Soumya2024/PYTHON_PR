n = int(input('Enter the number :'))
for i in range(1,n+1):
    sum=0
    while(n>0):
        rem = n%10
        sum = sum*10+rem
        n = n//10
    if(sum==i):
        print(' The palindrome numbers are :',i)
