##import function 
import string
import random 

## define a genPassword function 
def genPassword(n):

##input number, uppercase, lowercase and puncutation fuction 
    digits = string.digits             
    uppercase = string.ascii_uppercase 
    lowercase = string.ascii_lowercase
    punct = string.punctuation  

    digits_num = random.randint(1,n)
    uppercase_num = random.randint(1,n-digits_num-1)
    lowercase_num = random.randint(1, n - (digits_num + uppercase_num))
    puntuation_num = n-(digits_num + uppercase_num+lowercase_num)
 
 ##generating formalized password
    password = random.sample(digits,digits_num) + random.sample(uppercase,uppercase_num) + random.sample(lowercase,lowercase_num) +random.sample (punct, puntuation_num)
 
##random password
    random.shuffle(password)
 
##convert to string
    pwd = ''.join(password)

    return(pwd)

 

