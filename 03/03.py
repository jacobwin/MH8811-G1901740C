#define the Homework 1
def P01():
    print ('Hello, World')
    return

#define the homework 2-01
def P02_01():
    name=input('Who are you? ')
    print ('Hello', name)
    return 

#define the homewrok 2-02
def P02_02():
    C = float (input('Enter the temperature in degree celsius: '))
    F = C*1.8+32
    print ('The temperature in Fahrenheit is', F)
    return

#go back to run the loop
while True:
    
    #list all the sub-programs for options and with short descriptions
    print('List the sub-programs for you to choose: ')
    print('program 1: Hello, world ')
    print('program 2: Hello, name ')
    print('program 3: Convert temperature from Celsius to Fahrenheit ')
    
    #prompt user to choose
    n= int(input('What sub-programs would you like to choose? (Just type 1,2 or 3):' ))
    
    #run the chosen sub-programs
    if n==1:
        P01()
        print ('Thanks for your choosing, hope you enjoy the programs!')
    elif n==2:
        P02_01()
        print ('Thanks for your choosing, hope you enjoy the programs!')
    elif n==3:
        P02_02()
        print ('Thanks for your choosing, hope you enjoy the programs!')

#What else can you make a function?
#A lambda function: an anonymous function and can take many arguments

 #For exapmle:
x = lambda a, b : a * b
print(x(5, 6))