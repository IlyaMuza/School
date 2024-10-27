#import calendar
#from math import e
#from os import environ
#from string import Template

#print(e)

#c = calendar.TextCalendar()
#print(c.formatyear(2024))

#strings = ['This is a string', 'test String', 'test', 'string']

#d={}
#for i in range(len(strings)):
#    for j in strings[i].lower().split():
#        if j in d:
#            d[j].append(i)
#        else:
#            d[j] = [i]
#print(d)

#print(environ)
from string import punctuation

l=[]
with open('test.txt', 'r', encoding='utf-8') as f:
    k=[w for w in f.read().split()]
    print(k)
    f.seek(0)
    for line in f:
        for word in line.split():
            w=''
            for ch in word:
                if ch not in punctuation and not ch.isdigit():
                    w=w+ch
            l.append((w,len(w)))
m=l[0][1]
w=l[0][0]
for i in range(1,len(l)):
    if l[i][1]>=m:
        m=l[i][1]
        w=l[i][0]
print(w)