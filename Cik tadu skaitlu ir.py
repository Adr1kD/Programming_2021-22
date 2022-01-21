x=input("Massiv ")
x=x.split(" ")
cik=input("cik jautajumu bus? ")
cik=int(cik)
q=0

def skaitam(sk):
    b=0
    for a in range(len(x)):
        x[a]=int(x[a])
        if sk==x[a]:
            b=b+1
    print(b)

while(q<cik):
    sk=input("Skaitlis ")
    sk=int(sk)
    skaitam(sk)
    q=q+1
