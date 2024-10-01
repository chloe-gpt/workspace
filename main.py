from functions import clear

def password():
    from password import password
    a = int(input("arg hmSections > "))
    b = int(input("arg hmCharacters > "))
    password(a,b)

def frequency():
    from frequency import frequency; frequency()
    
def luhn():
    from luhn import luhn; luhn()
    
def beta():
    from beta import beta; beta()
    
def dnd():
    from dnd import dnd; dnd()
    
def sj():
    from stevejobs import SJ; SJ()

def strdiv():
    from stringdivision import divide_str; divide_str()

def fileaverage():
    from fileaverage import fileaverage; fileaverage()

def markov():
    from markov import generate_text; generate_text()

def cringe():
    from cringe import are_you_cringe; are_you_cringe()

def directory():
    from directory import directory; directory()

function_dict = {
    'password':password,
    'frequency':frequency,
    'luhn':luhn,
    'beta':beta,
    'dnd':dnd,
    'sj':sj,
    'strdiv':strdiv,
    'favg':fileaverage,
    'directory':directory,
    'markov': markov,
    'amicringe': cringe
}

while True:
    try:
        func = input('> ')
        clear()
        print(f"> {func}")
        function_dict[func]()
    except KeyError:
        print("Invalid function")