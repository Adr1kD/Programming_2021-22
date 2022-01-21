L=[]
n= int(input("How much elements?  "))
for a in range (n):
    new=int(input())
    L.append(new)


for y in range (len(L)):
    for x in range(0,(len(L)-1)-y):
        if L[x]>L[x+1]:
            temp=L[x]
            L[x]=L[x+1]
            L[x+1]=temp
print(L)
