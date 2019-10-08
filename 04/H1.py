
def my_min(fname):
    smallest_so_far= None
    for num in fname:
        if smallest_so_far is None:
         smallest_so_far = num
         continue
        elif smallest_so_far > num:
         smallest_so_far = num
    return smallest_so_far


def my_max(fname):
    largest_so_far=None 
    for a in fname:
        if largest_so_far is None:
         largest_so_far= a
         continue
        elif largest_so_far < a:
         largest_so_far = a
    return largest_so_far


def my_average(fname):
    sum=0
    for b in fname:
        sum += b 
        avg=sum/len(fname)
    return avg


def my_median(fname):
    fname.sort()
    r=int(len(fname)/2)
    c=len(fname)
    if c%2==0:
        median=(fname[r-1]+fname[r])/2
    elif c%2==1:
        median=fname[r]
    return median 


def my_range(fname):
    range=(my_max(fname))-(my_min(fname))
    return range


def getFilelines(fname):
    fhandle = open(fname)
    lines = []
    for line in fhandle:
        line = line.rstrip()
        if line:
            line = float(line)
            lines.append(line)
    fhandle.close()
    return lines

data = getFilelines('/Users/jacobzhu/Desktop/MH8811-04-Data.csv')

print('Min:', my_min(data))
print('Max:', my_max(data))
print('Average:', my_average(data))
print('Median:', my_median(data))
print('Range:',my_range(data))

#------------------------------------------------------------------
y=sum(data)
for x in data:
    x=int(x)
    mean=y/len(data)

total_sum=0
for x in data: 
    total_sum +=(x-mean)**2
    sample_variance = (total_sum)/(len(data)-1)

print('Sample variance:', sample_variance)

    
