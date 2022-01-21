
def Merge_sort(arr, l, r):
    
    def sort(arr, l, r):
        if l<r:
            c=(l+r)//2    
            sort(arr, l, c)
            sort(arr, c+1, r)
            Merge(arr, l, c, r)

    def Merge(arr, l, c, r):
        p1 = l
        p2 = c+1
        a=l
        while p1 <= c and p2 <= r:
            
            if arr[p1]<arr[p2]:
                TempArr[a] = arr[p1]
                p1 +=1
                a +=1
            else:
                TempArr[a] = arr[p2]
                p2 +=1
                a+=1

    TempArr=[0] * len(arr)
    sort(arr, l, r)

    for p1 in range(l, r):
        arr[p1]=TempArr[p1]

    return arr
            

arr=[]
r= int(input("How much elements?  "))
for a in range (r):
    new=int(input())
    arr.append(new)
l=0

Merge_sort(arr, l, r)
