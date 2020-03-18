import math
qw=raw_input()
gezegen=int(qw.split()[0])
M=int(qw.split()[1])
def binary(n):
    sayi=0
    while(n!=0):
        if n%2==1:
            sayi+=1
            n=n-1
        else:
            a=math.log(n,2)
            b=int(a)
            if b==a:
                sayi+=10**a
                n=0
            else:
                c=math.log(n,2)
                c=int(c)
                m=n-(2**c)
                sayi+=10**c
                n=m
    return int(sayi)

def xor(a,b):
    final=''
    y=0
    la=len(str(a))
    lb=len(str(b))
    if lb > la:
        c=lb-la
        a=(c*'0'+str(a))
    elif la > lb:
        c=la-lb
        b=(c*'0'+str(b))
    a=str(a)
    b=str(b)
    for i in range(len(a)):
        if a[i]==b[i]:
            final='0'+final
        else:
            final='1'+final
    liste=list(final)
    for j in range(len(final)):
        y+=int(liste[j])*(2**j)
    return y
def final(gezegen,M):
    l=[]
    miktar=0
    z=raw_input()
    for i in range(0,gezegen):
        a=int(z.split()[i])
        l.append(a)
    for j in l:
        j=int(j)
        t=binary(j)
        miktar+=xor(1,t)
    if miktar > M:
        print("-1")
    else:
        k=1
        miktar=0
        while(miktar<=M and k<=M):
            miktar=0
            kk=binary(k)
            for m in l:
                m=int(m)
                mm=binary(m)
                miktar+=xor(kk,mm)
            k+=1
        print(k-2)
    return 0

final(gezegen,M)
