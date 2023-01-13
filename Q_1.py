menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
print('=======Menu=======')
for i in range(len(menu)):
    print(str(i+1)+'.',menu[i][0],'- Rs.',menu[i][1])
print('==================')
item_no=[]
quantity=[]
while True:
    a=input('Enter Item No:')
    if a=='':
        break
    item_no.append(int(a))
    b=input('Enter quantity of item number '+a+':')
    quantity.append(int(b))
l1=[]
for i in item_no:
    l1.append(item_no.count(i))
if not l1.count(1)==len(l1):
            i=0
            quantity_1=[]
            while i<len(item_no):
                quantity1=quantity[i]
                for j in range(i+1,len(item_no)):
                    if item_no[i]==item_no[j]:
                        quantity1=quantity1+quantity[j]
                i=i+1
                quantity_1.append(quantity1)
            item_no_1=[]
            for i in item_no:
                if i not in item_no_1:
                    item_no_1.append(i)
            total_bill=[]
            for i in range(len(item_no_1)):
                print(menu[item_no_1[i]-1][0]+',',str(quantity_1[i])+',Rs.'+str(quantity_1[i]*menu[item_no_1[i]-1][1]))
                total_bill.append(quantity_1[i]*menu[item_no_1[i]-1][1])
            print('TOTAL,',sum(quantity),'items, Rs.',sum(total_bill))
else:
        total_bill=[]
        for i in range(len(item_no)):
            print(menu[item_no[i]-1][0]+',',str(quantity[i])+',Rs.'+str(quantity[i]*menu[item_no[i]-1][1]))
            total_bill.append(quantity[i]*menu[item_no[i]-1][1])
        print('TOTAL,',sum(quantity),'items, Rs.',sum(total_bill))

    