"""
Generates strong and customizeable passwords
"""

def password(hmSections, hmCharacters): # takes password paramaters as function arguments
    import time, os, random; password = ""; sectionNum = 1; charNum = 0 # packages and setting variables

    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    UPPERCASE = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','#','$','%','&','?']
    charType = [lowercase, lowercase, UPPERCASE, UPPERCASE, numbers, symbols] # setting character lists and list of lists

    while sectionNum <= hmSections: # loops each section
        while charNum <= hmCharacters: # loops each character
            listType = random.choice(charType) # random type of character
            character = random.choice(listType) # random character
            password = password + character # add to password
            charNum += 1 # increment number of characters
            if charNum == hmCharacters: # if last character of section
                if sectionNum < hmSections: # AND if not last section
                    password = password + "-" # adds dash to password
                sectionNum += 1 # increment sections
                charNum = 0 # resets characters
                break # restart character loop

    print("Your password is: " + password) # prints finished product