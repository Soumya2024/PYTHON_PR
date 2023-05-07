e = int(input('Enter the number :'))
for i in range(0,e):
    sum=0
    while(i>0):
        rev = i%10
        sum = sum+rev*rev*rev;
        i = i//10
print(sum)
    
