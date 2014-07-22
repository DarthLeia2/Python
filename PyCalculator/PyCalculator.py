'''
Created on Jul 22, 2014

@author: EM
'''

def main():
    numberOne = int(raw_input('Please enter a number:'))
    numberTwo = int(raw_input('Please enter another number:'))
    operator = raw_input('Please enter an operator (+, -, *, /)')
    
    if(operator == '+'):
        addition(numberOne, numberTwo)
    if(operator == '-'):
        subtraction(numberOne, numberTwo)
    if(operator == '*'):
        multiplication(numberOne, numberTwo)
    if(operator == '/'):
        division(numberOne, numberTwo)
    
def addition(x, y):
    result = x + y
    
    print result
    
def subtraction(x, y):
    result = x - y
    
    print result
    
def multiplication(x, y):
    result = x * y
    
    print result
    
def division(x, y):
    result = float(x) / float(y)
    
    print result


if __name__ == '__main__':
    main();