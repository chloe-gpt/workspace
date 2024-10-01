"""
A few tools for Dungeons & Dragons, including a customizeable die roller and a character stat generator.
"""

def dnd():
    import random, time; from functions import clear
    while True: #loops the whole program
        menu = input("Enter \'stats\' to roll stats, or enter a die to roll that die.\n> ")
        from dnd_main.stats import stats
        from dnd_main.roll import roll
        if menu == "stats": 
            stats()
        elif "d" in menu.lower(): #if it does not start with d but contains d
            roll(menu)