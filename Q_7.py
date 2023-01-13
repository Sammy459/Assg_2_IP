f1=open('addressbook.txt','r')
l=f1.readlines()
if len(l)==0:
    address_book={}
    print('Address book is empty')
else:
    add=l[0]
    address_book=eval(add)
    print('Address book not empty')
f1.close()
while True:
    a=input('Enter name for new entry:')
    if a=='':
        break
    address_book[a]={}
    d=address_book[a]
    b=input('Enter Number:')
    d['Number']=b
    c=input('Enter Address:')
    d['Address']=c
    e=input('Enter email:')
    d['Email']=e
while True:
    a=input('Enter name for deleting entry:')
    if a=='':
        break
    b=address_book.copy()
    for key in b:
        if not a==key:
            print('Entry not found')
        else:
            del address_book[a]
            print('Entry deleted')
while True:
    a=input('Enter name for searching:')
    if a=='':
        break
    for key in address_book:
        if a in key:
            print(key+':',address_book[key])
        else:
            print('Name not found')
while True:
    a=input('Enter phone number for searching:')
    if a=='':
        break
    for key in address_book:
        b=address_book[key]
        if b['Number']==int(a):
            print(key)
while True:
    a=input('Enter email for searching:')
    if a=='':
        break
    for key in address_book:
        b=address_book[key]
        if b['Number']==a:
            print(key)
f1=open('addressbook.txt','w')
f1.write(str(address_book))
f1.close()
