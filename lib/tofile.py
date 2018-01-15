'''
Created on 5 ago. 2017

@author: Dave
'''

import os


def wrtitefile(string):
    filename = "C:/Users/Dave/Documents/Tunel/test.txt"    
    
    if(os.path.exists(filename)):        
        file = open(filename, 'a')
    else:
        file = open(filename, 'w')            
            
    file.write(string + '\n') 
    file.close()    