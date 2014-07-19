'''
Created on Jul 16, 2014

@author: Elizabeth

Projects for Python Mastery completed 7/15/14 by Elizabeth Mort.
'''
import math

if __name__ == '__main__':
    pi = math.pi;
    print pi;
    formatter = input('Please enter a number 1-9');
    
    if(formatter == 1):
        print "%.1f" % pi;
    elif(formatter == 2):
        print "%.2f" % pi;
    elif(formatter == 3):
        print "%.3f" % pi;
    elif(formatter == 4):
        print "%.4f" % pi;
    elif(formatter == 5):
        print "%.5f" % pi;
    elif(formatter == 6):
        print "%.6f" % pi;
    elif(formatter == 7):
        print "%.7f" % pi;
    elif(formatter == 8):
        print "%.8f" % pi;
    elif(formatter == 9):
        print "%.9f" % pi;  
    else:
        print "Pi is " + str(pi) + " according to Python." 