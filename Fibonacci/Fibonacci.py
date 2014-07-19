'''
Created on Jul 11, 2014
Projects for Python Mastery completed 7/16/14 
Fibonacci sequence. Number of digits determined by user input.
@author: Elizabeth
'''


def main():    
    number = input('Please enter a number: ');
    i = 0;
    
    while(i < number):
        print fibonacci(i);
        i += 1;
                         
                         

def fibonacci(n):      
    if(n < 2):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
        
        
if __name__ == '__main__':
    main();