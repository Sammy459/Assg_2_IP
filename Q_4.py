words = ['apple', 'board', 'cloth', 'plant', 'house', 'glass', 'shirt','table', 'water', 'beach', 'light', 'party', 'knife', 'fruit', 'stone','woman', 'chair', 'plate', 'watch', 'clock', 'phone', 'truck', 'pizza','horse', 'mouse', 'bread', 'candy', 'cloud', 'couch', 'cream','dough', 'dress', 'final', 'fence', 'fries', 'grape', 'group', 'juice','knife', 'lemon', 'metal', 'onion', 'oxime', 'paper', 'plant', 'plate','porch', 'purse', 'shirt', 'table', 'teeth', 'tiger', 'truck', 'water','world']
import random
a=words[random.randint(0,len(words))]
for i in range(6):
    c=''
    b=input('Enter five character string:')
    for j in range(5):
        if a[j]==b[j]:
            c=c+b[j]
        else:
            c=c+'-'
    for j in range(5):
        if b[j] in b and b[j] in a and a[j]!=b[j]:
            print('Other characters presents are:',b[j])
    if c==a:
        print('Word guessed,YAY!')
        print('The word was',a)
        break
    print(c)
    if i==5:
        print('Too bad,Better Luck Next Time')
        print('The word was',a)
