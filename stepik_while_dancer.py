# найти максимальное количество возможных танцевальных пар по данным: nli- список уровня танцевабельности мальчиков, mli - девочек
# разница в скиле не должна быть больше 1
nli = list(map(int,input().split()))
mli = list(map(int,input().split()))
c=0
nli.sort(reverse=True)
mli.sort(reverse=True)
while len(nli)!=0 and len(mli)!=0:
    if (abs(nli[0]-mli[0]))>0:
        if nli[0]>mli[0]:
            nli.pop(0)
        else:
            mli.pop(0)
    else:
        c += 1
        nli.pop(0)
        mli.pop(0)
print(c)