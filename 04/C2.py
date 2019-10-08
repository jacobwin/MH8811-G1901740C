lst=[9,14,12,3,74,15]

def my_min(lst):
    smallest_so_far= None
    for num in lst:
        if smallest_so_far is None:
         smallest_so_far = num
         continue
        elif smallest_so_far > num:
         smallest_so_far = num
    return smallest_so_far

print(lst)
print('Min:',my_min(lst))

def my_max(lst):
    largest_so_far=None 
    for a in lst:
        if largest_so_far is None:
         largest_so_far= a
         continue
        elif largest_so_far < a:
         largest_so_far = a
    return largest_so_far

print(lst)
print ('Max:',my_max(lst))

def my_average(lst):
    sum=0
    for b in lst:
        sum += b 
        avg=sum/len(lst)
    return avg

print(lst)
print('Average:',my_average(lst))

def my_median(lst):
    lst.sort()
    r=int(len(lst)/2)
    c=len(lst)
    if c%2==0:
        median=(lst[r-1]+lst[r])/2
    elif c%2==1:
        median=lst[r]
    return median 

print(lst)
print('Medain:',my_median(lst))

def my_range(lst):
    range=(my_max(lst))-(my_min(lst))
    return range

print(lst)
print('Range:',my_range(lst))



    





