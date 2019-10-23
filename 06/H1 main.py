import pwdmodule

n=int(input('Wihich passoword length you want? '))
if n>=4:
    pwd=pwdmodule.genPassword(n)
    print('The generating password is', pwd) 
elif n<4:
    print ('The password should be at least 4 digits')

      

        



    
