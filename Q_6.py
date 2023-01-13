file1=open('IPmarks.txt')
file2=open('IPgrades.txt','w')
a=file1.readlines()
wts = [(10, 5), (20, 5), (100, 15), (40, 10), (20, 10), (40, 20), (70, 35)]
for i in range(len(a)):
    l=a[i].split(',')
    sum=0
    for j in range(0,len(l)-1):
        l[j+1]=int(l[j+1])
        b=(l[j+1]/wts[j][0])*(wts[j][1])
        sum=sum+b
    sum=round(sum,2)
    if sum>80:
            grade='A'
    elif 80>=sum>70:
            grade='A-'
    elif 70>=sum>60:
            grade='B'
    elif 60>=sum>50:
            grade='B-'
    elif 50>=sum>40:
            grade='C'
    elif 40>=sum>35:
            grade='C-'
    elif 35>=sum>30:
            grade='D'
    elif sum<=30:
            grade='F'
    sum=str(sum)
    file2.write(l[0]+', '+sum+', '+grade+'\n')
file1.close()
file2.close()
        
        

