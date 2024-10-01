import random
def roll(_input):
    if _input[0].lower() == "d":
        die = int(_input[1:]) #all characters after d become int
        roll = random.randint(1,die) #random num within range
        print(f"You rolled a d{die} and got a {roll}.") #print
    elif "d" in _input[0:].lower(): #if it does not start with d but contains d
        total = 0
        _input_list = _input.split("d") #splits by the 'd' into list
        rolls = int(_input_list[0]) #first number is of rolls
        die = int(_input_list[1]) #second is what size die
        for i in range(0,rolls): #rolls each die
            roll = random.randint(1,die)
            total += roll #adds roll to toal
        print(f"You rolled {rolls}d{die} and got a total of {total}.") #prints total