xy=raw_input()
limit=int(xy.split()[0])
sembol=int(xy.split()[1])
tekrar=[]
for i in range(sembol):
    a=int(raw_input())
    tekrar.append(a)
alfabe=range(sembol)
zz=[]
alfabe=map(str,alfabe)
zz.append(alfabe)
sayi=sembol
for i in range(limit-1):
    y=[]
    ee=[]
    ex=zz[i]
    for m in ex:
        control=m[-1]
        ind=alfabe.index(control)
        if tekrar[ind]==1:
            sayi +=sembol-1
            ee=alfabe[:ind]+alfabe[ind+1:]
            h=[m]*len(ee)
            for u,p in zip(h, ee):
                y.append(str(u)+str(p))
        else:
            t=tekrar[ind]
            if len(m)>=t:
                w=m[-t:-1]
                if w==(t-1)*control:
                    sayi+=sembol-1
                    ee=alfabe[:ind]+alfabe[ind+1:]
                    h=[m]*len(ee)
                    for u,p in zip(h, ee):
                        y.append(str(u)+str(p))
                else:
                    sayi+=sembol
                    h=[m]*len(alfabe)
                    for u,p in zip(h, alfabe):
                        y.append(str(u)+str(p))
            else:
                sayi+=sembol
                h=[m]*len(alfabe)
                for u,p in zip(h, alfabe):
                    y.append(str(u)+str(p))


    zz.append(y)

def func(limit,sembol,sayi):
    gr=sayi%((10**9)+7)
    print(gr)
    return 0

func(limit,sembol,sayi)
