n=int(input('Enter value of n for n highest ranking pages:'))
f1=open('pages.txt')
l=f1.readlines()
f1.close()
a=len(l)
rank,l1={l[i][:5]:0 for i in range(len(l))},[float(l[i][7:10]) for i in range(len(l))]  
for i in range(a):
    b=l[i].split(' ')
    d={}
    for j in range(1,len(b)):
            f=b[j]
            if f[:3]=='URL' and len(f)>=5 and b[0][:5]!=f[:5]:
                d[f[:5]]=1
    e=l1[i]/len(d)
    for key in d:
        if key in rank:
            rank[key]=rank[key]+e
l2 = sorted(rank.items(), key=lambda x:x[1], reverse=True)[:n]
for i in l2:
    print(i[0],round(i[1],2))
    




    