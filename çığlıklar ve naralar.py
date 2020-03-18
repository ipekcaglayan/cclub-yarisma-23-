def mirror(w):
    l=len(w)
    if l%2==0:
        if l==2:
            if w[0]==w[1]:
                return True
            else:
                return False
        else:
            if w[1]==w[-2]:
                return mirror(w[1:-1])
            else:
                return False
    else:
        return False

num=int(raw_input())
words=[]
for i in range(num):
    w=raw_input()
    words.append(w)
def kuvvet(w,hepsi):
    if len(w)==1:
        hepsi.append(0)
    else:
        ll=len(w)
        ctrl=w[0]
        ind=w[1:].find(ctrl)
        if ind==-1:
            return kuvvet(w[1:],hepsi)
        else:
            xx=[]
            ind=ind+1
            xx.append(ind)
            for i in range(2,ll):
                index=w[i:].find(ctrl)
                if index== -1:
                    break
                else:
                    index+=i
                    xx.append(index)
                    for g in xx:
                        new=w[:g+1]
                        if mirror(new):
                            if w[g+1:g+1+len(new)]==new:
                                ss=len(w[:g+1+len(new)])
                                hepsi.append(ss)
            return kuvvet(w[1:],hepsi)
    print(max(hepsi))
    return 0
def funct(words):
    for f in words:
        hepsi=[]
        kuvvet(f,hepsi)
    return 0

funct(words)
