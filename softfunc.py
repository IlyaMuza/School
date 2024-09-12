nums = [5,4,2,3,4,7,8,9,1]
def bubble_sort(ls):
    swapped=True
    g=0
    while swapped:
        swapped=False
        g += 1
        for i in range(len(ls)-1):
            if ls[i]>ls[i+1]:
                ls[i],ls[i+1] = ls[i+1],ls[i]
                swapped=True
    return g

# print(bubble_sort(nums))
# print(nums)

def select_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i+1,len(ls)):
            if ls[j]<ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest],ls[i]
    return len(ls)+1

print(select_sort(nums))
print(nums)
