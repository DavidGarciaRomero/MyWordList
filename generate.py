'''
Created on 26 jul. 2017

@author: Dave
'''
from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':

    name = raw_input("Name:")
    lastname = raw_input("LastName:")
    bdate = raw_input("Birthday:")
    others = raw_input("More words, separate by , :")
    
    print(name, lastname, bdate, others)