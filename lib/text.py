'''
Created on 5 ago. 2017

@author: Dave
'''

from lib import tofile
from lib import text


def basicNameLast(name, lastname):
    
    texto = name
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    
    texto = lastname
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    
    texto = name + lastname
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = name + "." + lastname
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = name + "-" + lastname
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = name + "_" + lastname
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    
    texto = lastname + name
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = lastname + "." + name
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = lastname + "-" + name
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = lastname + "_" + name
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
        
    texto = name[0] + lastname
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)    
    texto = name[0] + "." + lastname
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = name[0] + "-" + lastname
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = name[0] + "_" + lastname
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    
    texto = lastname[0] + name
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)    
    texto = lastname[0] + "." + name
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = lastname[0] + "-" + name
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = lastname[0] + "_" + name
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    
    texto = name + lastname[0]
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)    
    texto = name + "." + lastname[0]
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = name + "-" + lastname[0]
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = name + "_" + lastname[0]
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    
    texto = lastname + name[0]
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)    
    texto = lastname + "." + name[0]
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = lastname + "-" + name[0]
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = lastname + "_" + name[0]
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    
    texto = name[0] + name[1] + name[2] + lastname[0] + lastname[1] + lastname[2]
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)    
    texto = name[0] + name[1] + name[2] + "." + lastname[0] + lastname[1] + lastname[2]
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = name[0] + name[1] + name[2] + "-" + lastname[0] + lastname[1] + lastname[2]
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)
    texto = name[0] + name[1] + name[2] + "_" + lastname[0] + lastname[1] + lastname[2]
    tofile.wrtitefile(texto)
    text.plusNumbers(texto)


def permutations(texto):
    
    L = list(texto)
    
    for i in range(L.__len__()):
        
        letter=L[i]
        
        if L[i].isdigit():
            print(L[i] + " is number")
            if L[i] == 3:
                print("is a 3")
                L[i]. = 'E'
            elif L[i] == 0:
                L[i] = 'O'
        else:
            print(L[i] + " is letter")
            L[i].upper()

        print(L)
    
       
def plusNumbers(string):
       
    #to add 01, 02, 03, etc
    for i in range (0,10):
        texto = string + "0" + str(i)
        tofile.wrtitefile(texto)  
        
    for i in range (0,10):
        texto = string + "." + "0" + str(i)
        tofile.wrtitefile(texto)
    
    for i in range (0,10):
        texto = string + "-" + "0" + str(i)
        tofile.wrtitefile(texto)
        
    for i in range (0,10):
        texto = string + "_" + "0" + str(i)
        tofile.wrtitefile(texto) 
        
    # to add 0, 1, 2, 3, etc
    bignumber = 100
    
    for i in range (0,bignumber):
        texto = string + str(i)
        tofile.wrtitefile(texto)  
        
    for i in range (0,bignumber):
        texto = string + "." + str(i)
        tofile.wrtitefile(texto)
    
    for i in range (0,bignumber):
        texto = string + "-" + str(i)
        tofile.wrtitefile(texto)
        
    for i in range (0,bignumber):
        texto = string + "_" + str(i)
        tofile.wrtitefile(texto) 
           
    
def year(name, lastname, year):
    texto = name + year
    tofile.wrtitefile(texto)
    texto = name + "." + year
    tofile.wrtitefile(texto)
    texto = name + "-" + year
    tofile.wrtitefile(texto)
    texto = name + "_" + year
    tofile.wrtitefile(texto)
    
    texto = name + year[-2] + year[-1]
    tofile.wrtitefile(texto) 
    texto = name + "." + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = name + "-" + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = name +  "_" + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    
    texto = lastname + year
    tofile.wrtitefile(texto) 
    texto = lastname + "." + year
    tofile.wrtitefile(texto)
    texto = lastname + "-" + year
    tofile.wrtitefile(texto)
    texto = lastname + "_" + year
    tofile.wrtitefile(texto)
    
    texto = lastname + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname + "." + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname + "-" + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname + "_" + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    
    texto = name + lastname + year
    tofile.wrtitefile(texto)
    texto = name + lastname  + "." + year
    tofile.wrtitefile(texto)
    texto = name + lastname + "-" + year
    tofile.wrtitefile(texto)
    texto = name + lastname + "_" + year
    tofile.wrtitefile(texto) 
    
    texto = lastname + name + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname + name + "." + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname + name + "-" + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname + name + "_" + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    
    texto = name[0] + lastname + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname + name + "." + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname + name + "-" + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname + name + "_" + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    
    texto = lastname[0] + name + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname[0] + name + "." + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname[0] + name + "-" + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname[0] + name + "_" + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    
    texto = name + lastname[0] + year[-2] + year[-1] 
    tofile.wrtitefile(texto)
    texto = name + lastname[0] + "." + year[-2] + year[-1] 
    tofile.wrtitefile(texto)
    texto = name + lastname[0] + "-" + year[-2] + year[-1] 
    tofile.wrtitefile(texto)
    texto = name + lastname[0] + "_" + year[-2] + year[-1] 
    tofile.wrtitefile(texto)
    
    texto = lastname + name[0] + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname + name[0] + "." + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname + name[0] + "-" + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    texto = lastname + name[0] + "_" + year[-2] + year[-1]
    tofile.wrtitefile(texto)
    
def others(string):
    arr = string.split(",")
    
    for i in arr:
        texto = i
        tofile.wrtitefile(texto)
        text.plusNumbers(texto)
        
def template():
     
    template = "./template.txt" 
       
    file = open(template, 'r')
    
    for line in file:
        if '\n' == line[-1]:
            line = line[:-1]
            tofile.wrtitefile(line)
    

    