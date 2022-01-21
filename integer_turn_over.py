number = int(input("Enter a positive integer: "))
rev = 0
while(number!=0):
    digit = number%10
    print(digit)
    rev = (rev*10)+digit
    number = number//10
print(rev)
print(type(rev))
