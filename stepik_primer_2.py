import json
from pprint import pprint

with open('numbers.txt') as f:
    s = f.read().split('\n')
l = [int(i) for i in s[:-1]]
n = 0
s = 0
for i in l:
    if 100<=i<=999:
        n += 1
    if 10<=i<=99:
        s += i
print(n,s)

with open(r'Z:\G\lorem.txt') as f:
    s = f.read().upper().split()
se = set(s)
print(len(se))
di = {}
for i in s:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1
print(di)

with open(r'Z:\G\words.txt', encoding='utf-8') as f:
    s = [i for i in f.read().upper().split() if i[-2:]=='ЕЯ']
s = set(s)
d = {}
for i in s:
    if len(i) not in d:
        d[len(i)] = [i]
    else:
        d[len(i)].append(i)
print(s)
print(d)
result = []
for i in sorted(d):
    result.extend(sorted(d[i]))
    print(*sorted(d[i]), sep='\n')
 #   for j in range(len(d[i])):
#print(*result, sep='\n')

with open(r'Z:\G\manager_sales.json') as f:
    s = json.load(f)
max = 0
for i in s:
    summ = 0
    for j in i['cars']:
        print(j)
        summ += j['price']
    if summ > max:
        max = summ
        f_n = i['manager']
print(f_n, max)
print('###'*50)

with open(r'Z:\G\group_people.json') as f:
    s = json.load(f)
pprint(s)
max = 0
for i in s:
    coun = 0
    for j in i['people']:
        if j['gender'] == 'Female' and j['year'] >= 1977:
            coun += 1
    if coun>max:
        max = coun
        idg = i['id_group']
    print(i['id_group'], coun)
print(idg, coun)

with open(r'Z:\G\Abracadabra__1_.txt') as f:
    text = f.read()
with open(r'Z:\G\Alphabet.json') as f:
    cod = json.load(f)
res = ''
for i in text:
    if i in cod:
        res = res + cod[i]
    else:
        res = res + i
print(res)
with open(r'Z:\G\Decod.txt', 'w') as f:
    f.write(res)
