def Bubble_sort(): 
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


def Selection_sort():
    LF=[]

    q= int(input("How much elements?  "))
    for a in range (q):
        new=input()
        LF.append(new)


    for i in range(1, len(LF)):
        min_temp=i
        for x in range(i+1, len(LF)):
                if LF[min_temp]> LF[x]:
                    min_temp=x
        LF[i], LF[min_temp]= LF[min_temp], LF[i]
            
    print(LF)

def Insert_sort():
    list1=[]

    q= int(input("How much elements?  "))
    for a in range (q):
        new=input()
        list1.append(new)

    for x in range(1, len(list1)):  
        value = list1[x]
        j = x - 1  
        while j >= 0 and value < list1[j]:  
            list1[j + 1] = list1[j]  
            j -= 1  
            list1[j + 1] = value  
    print(list1) 

Sort=int(input("Bubble_sort = 1   Selection_sort = 2  Insert_sort = 3 \n"))
if Sort == 1:
    Bubble_sort()
if Sort == 2:
    Selection_sort()
if Sort == 3:
    Insert_sort()
