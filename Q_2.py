l=[]
grade={'A+':10,'A':10,'A-':9,'B':8,'B-':7,'C':6,'C-':5,'D':4,'F':2}
while True:
    a=input('Enter Course No.,Credits,Grade: ').split()
    c=0
    if a==[]:
        break
    for i in range(len(a[0])-1):
        d=a[0][i].isupper()
        e=a[0][i+1].isupper()
        if d!=e:
            c=c+1
    if c>1:
        f='Improper Course No'
    else:
        f=''
    
    if not (a[1]=='1' or a[1]=='2' or a[1]=='4'):
        g='Incorrect credit'
    else:
        g=''
    if not (a[2]=='A+' or a[2]=='A' or a[2]=='A-' or a[2]=='B' or a[2]=='B-' or a[2]=='C' or a[2]=='C-' or a[2]=='D' or a[2]=='F'):
        h='Incorrect Grade'
    else:
        h=''
    if f=='' and g=='' and h=='':
        l.append(a)
    else:
        print(f,g,h)
course_no=[]     
for i in range(len(l)):
    course_no.append(l[i][0])
course_no.sort()
for i in range(len(l)):
    print(course_no[i]+':'+l[i][2])
sgpa=[]
credit=[]
for i in range(len(l)):
    sgpa.append(int(l[i][1])*grade[l[i][2]])
for i in range(len(l)):
    credit.append(int(l[i][1]))
print('SGPA:',format((sum(sgpa)/sum(credit)),'.2f'))


    


    
