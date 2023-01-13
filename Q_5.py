n=int(input('Enter no of coordinates:'))
l=[]
for i in range(n):
    a=list(input())
    a.remove(',')
    b=[int(x) for x in a]
    b=b+[1]
    l.append(b)
Cx=int(input('Enter Cx:'))
Cy=int(input('Enter Cy:'))
l1=[[Cx,0,0],[0,Cy,0],[0,0,1]]
l2=[]
for i in range(n):
    l3=[]
    for j in range(3):
        l4=[]
        for k in range(3):
            c=l[i][k]*l1[k][j]
            l4.append(c)
        l3.append(sum(l4))
    l2.append(l3)
for i in range(n):
    f=[l2[i][0],l2[i][1]]
    print(tuple(f))
