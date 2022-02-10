n = input("Enter number to check Harshad or Not :")
n=int(n)
num=n
result = 0
while(n!=0):
    number = n%10
    result=result + number
    n=int(n/10)	
if(num % result == 0):
    print("Harshad Number!")
else:
    print("Not an Harshad Number!")