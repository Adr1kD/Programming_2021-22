n=input()
x=[]
n=n.split(" ")
for u in range(len(n)):
    x.append(n[u])

from_=int(x[-1])-3000
from_=int(from_)
if from_<0:
    from_=0

end=x[-1]
something=0
nothing=0

for i in range(len(x)):
    if int(x[i]) < from_:
        nothing=nothing+1
    else:
        something=something+1

print(something)
