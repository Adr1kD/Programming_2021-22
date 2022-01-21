import math

from bisect import bisect

def funk(com , p):
    sm = []
    s = 0
    for (x,y,a,d) in com:
        s += a
        sm.append(s)
    ind = bisect(sm, p)
    return math.ceil(com[ind][3])

def solve(n, p, xc, yc, a):
    r = 0
    com = []
    i = 0
    while(i < n):
        d = math.sqrt(xc[i]**2 + yc[i]**2)
        com.append([xc[i], yc[i], a[i], d])
        i+=1
    com = sorted(com, key = lambda x:x[3])
    if(sum(a) < p):
        return -1
    return funk(com, p)
o = int(input())

for _ in range(o):
    n, p = [int(i) for i in input().split()]
    x = [int(i) for i in input().split()]
    y = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    out = solve(n, p, x, y, a)
print(out)
