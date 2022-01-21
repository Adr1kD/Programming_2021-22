n=int(input())
rez=0
while n>0:
    x=n%10
    rez=rez+x
    n=n//10
print(rez)
