def fibo(n):
    x1=1
    x2=0
    for i in range(n):
        x3=x1+x2
        x1=x2
        x2=x3
        yield x3

#    return x3
#        yield s_2
#        s_2,s_1 = s_2+2_1, s_2

d = fibo(6)
#print(next(d))
#print(next(d))
#print(next(d))

def my_range_gen(*args):
    if len(args) == 1:
        stop = args[0]
        start = 0
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        return
    while ((start < stop and step>0) or (start>stop and step<0)) and step!=0:
        yield start
        start += step
    return

for i in my_range_gen(4,7):
    print(i)

for i in my_range_gen(4,1,-2):
    print(i)