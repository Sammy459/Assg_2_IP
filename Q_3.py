signs=open('signatures.txt')
a=signs.readlines()
for i in range(len(a)):
    if i*i==len(a):
        f=i
        break
dic={}
names=[]
for i in range(0,len(a),f):
    g={}
    names.append(a[i])
    for j in range(i+1,i+f):
        a[j]=a[j].strip()
        h=a[j].split(',')
        g[h[0]]=int(h[1])
    dic[a[i]]=g
l1=[]
for i in dic:
    c=0
    d=dic[i]
    for j in d:
        if d[j]==1:
            c=c+1
    l1.append(c)
max_signs=max(l1)
min_signs=min(l1)
print('People having max signatures are:')
for i in range(len(l1)):
    if l1[i]==max_signs:
        print(names[i],max_signs)
print('People having min signatures are:')
for i in range(len(l1)):
    if l1[i]==min_signs:
        print(names[i],min_signs)
signs.close()
