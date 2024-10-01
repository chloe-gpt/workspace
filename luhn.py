"""
This program is a Python reimplimentation of Luhn's Algorithm, a primary check for the validity of credit card numbers.
"""

def luhn():
    import time, json; from functions import file; listObj = []

    card_number = input("Enter card number: > ") #take input
    card_digits = [*card_number] #convert to list
    
    count = len(card_digits) #number of digits
    if count == 16: #verify length of number
        print(f"Number of digits: {count} (Valid)")
    else:
        print(f"Number of digits: {count} (Invalid)")
    
    for index, num in enumerate(card_digits): #for each digit
        if index % 2 == 0: #every other digit from the first 
            card_digits[index] = int(num) * 2 #multiply by 2
            if card_digits[index] > 9: #if greater than 9
                total = 0
                while card_digits[index] > 0: #for each digit
                    total += card_digits[index] % 10
                    card_digits[index] //= 10
                card_digits[index] = total #adds all digits together
        else:
            card_digits[index] = int(num) #convert to int
        
    card_sum = sum(card_digits) #add all card digits together
    if card_sum % 10 == 0: #if multiple of 10, verify
        print(f"Sum of modified digits: {card_sum} (Valid)")
        if len(card_digits) == 16:
            valid = True
        else:
            valid = False
    else:
        print(f"Sum of modified digits: {card_sum} (Invalid)")
        valid = False
        
    card_dict = dict(number = card_number, digits = count, digit_sum = card_sum, valid = valid)
    with open('logs/cards.json') as fp:
        listObj = json.load(fp)
    listObj.append(card_dict)
    
    with open('logs/cards.json', 'w') as json_file:
        json.dump(listObj, json_file, 
                            indent=4,  
                            separators=(',',': '))
    
    print('Successfully appended to the JSON file')

if __name__ == "__main__":
    luhn()