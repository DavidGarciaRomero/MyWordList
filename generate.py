'''
Created on 26 jul. 2017

@author: Dave
'''
from pip._vendor.distlib.compat import raw_input
from lib import text

if __name__ == '__main__':

    name = raw_input("Name:")
    name = name.lower()
    lastname = raw_input("LastName:")
    lastname = lastname.lower()
    year = raw_input("Year:")
    others = raw_input("More words, separate by , :")
    others = others.lower()
    
        
    #text.basicNameLast(name, lastname)    
    #text.year(name, lastname, year)
    #text.others(others)
    #text.template()
    text.permutations(name)
    print("File done")


    
    