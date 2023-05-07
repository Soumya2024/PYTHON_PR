maximum = int(input(" Please Enter the Maximum Value : "))

#print("Palindrome Numbers between 1 and %d are : " %(maximum))
for num in range(1, maximum + 1):
    temp = num
    reverse = 0
    
    while(temp > 0):
        Reminder = temp % 10
        reverse = reverse + Reminder*Reminder*Reminder
        temp = temp //10

    if(num == reverse):
        print("%d " %num, end = '  ')
