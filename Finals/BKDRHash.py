
import string

def BKDR(string):
    
    seed = 131
    hash = 0
    
    for char in string:
        hash = (hash*seed) + ord(char)
        
    return hash

string = "Hello, World!"
print("The hash is",BKDR(string))