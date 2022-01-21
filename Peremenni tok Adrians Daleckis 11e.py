s = input()
print(type(s))
a = ['']
for i in s:
    if a[1]==i:
        a.pop()
    else:
        a.append(i)
if len(a)==1:
    print("Yes")
else:
    print("No")
