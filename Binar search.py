a = [1, 5, 3, 2, 8, 6]
value = int(input())
 
mid = len(a) // 2
low = 0
high = len(a) - 1
 
while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
 
if low > high:
    print("No value")
else:
    print("ID =", mid)
