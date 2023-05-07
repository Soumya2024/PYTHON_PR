n = int(input('Enter the starting number :'))
m = int(input('Enter the ending number :'))
for i in range(n, m+1):
    sum=0
    temp = i
    while(temp>0):
        rem = temp%10
        f = 1
        for j in range(1, rem+1):
            if(j%rem==0):
                f = f+1
        sum = sum+rem;
        temp = temp//10
    if(sum==i):
        print(i, end=' ')
        
            
        
