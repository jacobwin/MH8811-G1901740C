import json
###define a function to open the file
def open_file(filename):
    fh=open(filename)
    data=json.load(fh)
    fh.close()
    return data
    

###define a function to serialize
def serialize(l):
    s=json.dumps(l)
    return s

 ###input files       
filename=input('H1-1.json,H1-2.json,H1-3.json,H1-4.json or H1-5.json')

###Load the json files
d1=open_file(filename)
print(d1)
print(type(d1))
print('Success!')
    
###Convert data type into string
s=serialize(d1)
print(type(s)) 


filename1=input('what will be the name of the new file?')
with open(filename1,'w') as f1:
    json.dump(s,f1)
    f1.close()
    print('Success!')

###Read the string
with open(filename1) as f2:
       d2=json.load(f2)
       f2.close()
print(d2)
print(type(d2))
print('Success!')

###Deserialization function
d2=json.loads(d2)
print(d2)
print(type(d2))

###Define a function for comparison
def compare(d1,d2):
    if type(d1) == type(d2):
        if type(d1) == type([]):
            print(diff_lst(d1,d2))
        if type(d1) == type({}):
            print(diff_dict(d1,d2))
    else:
        return False

###define a function to compare the list
def diff_lst(d1,d2):
    if len(d1) == 0:
        return True
    v=d1[0]
    for v1 in d2:

        if type(v) == list:
            if not diff_lst(v,v1):
                return False

        if type(v) == dict:
            if not diff_dict(v,v1):
                return False

    return True

###define a function to comapre the dict
def diff_dict(d1,d2):
    if d1 and d2: 
       for k in set(d1) or set(d2): 
        if k in d1 and d2:
            if d1[k]==d2[k]:
                return True
        else:
            return False 
    elif d1==d2:
        return True
    else:
        return False


compare(d1,d2)
