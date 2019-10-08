
def my_min(data):
    smallest_so_far= None
    for num in data:
        if smallest_so_far is None:
         smallest_so_far = num
         continue
        elif smallest_so_far > num:
         smallest_so_far = num
    return smallest_so_far


def my_max(data):
    largest_so_far=None 
    for a in data:
        if largest_so_far is None:
         largest_so_far= a
         continue
        elif largest_so_far < a:
         largest_so_far = a
    return largest_so_far


def my_average(data):
    sum=0
    for b in data:
        sum += b 
        avg=sum/len(data)
    return avg



def my_median(data):
    data.sort()
    r=int(len(data)/2)
    c=len(data)
    if c%2==0:
        median=(data[r-1]+data[r])/2
    elif c%2==1:
        median=data[r]
    return median 


def my_range(data):
    range=(my_max(data))-(my_min(data))
    return range

#----------------------------------------------------------

def getFilelines(data):
    fhandle = open(data)
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


