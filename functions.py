"""
Basic function library
"""

def restart():
    import sys, os
    os.execv(sys.executable, ['python'] + sys.argv) #restart file
    
def clear():
    from os import system, name
    if name == 'nt': #windows
        _ = system('cls')
    else: #mac & linux (posix)
        _ = system('clear')

def file(filename, op, text): #args are the filename, operation, and what to write
    log = open(filename, op) #open log
    log.write("\n" + str(text)) #write text to log
    log.close() #close log