import random, os, sys
sys.path.append(os.path.abspath('../'))
from functions import clear
def stats():
    stats = ['STR', 'DEX', 'CON', 'WIS', 'INT', 'CHA']
    stats_mid = [0] * 6
    stats_end = [0] * 6
    stats_rba = [0] * 6
    for index, stat in enumerate(stats): #repeats each stat
        roll_1 = random.randint(1,6) #4 random d6
        roll_2 = random.randint(1,6)
        roll_3 = random.randint(1,6)
        roll_4 = random.randint(1,6)
        rolls = [roll_1, roll_2, roll_3, roll_4] #lists each
        rolls.pop(rolls.index(min(rolls))) #removes lowest
        total = str(sum(rolls)) #sums remaining
        stats_mid[index] = total
    clear()
    stats_mid = sorted(stats_mid, reverse=True)
    for x, i in enumerate(stats_mid):
        stats_mid[x] = str(i).zfill(3)
    print(stats_mid) #prints all final numbers
    for index, roll in enumerate(stats_mid): #for each stat
        choice = int(input(f"Which stat would you like to assign the value {stats_mid[index]} to?\n1: STR ({stats_end[0]})\n2: DEX ({stats_end[1]})\n3: CON ({stats_end[2]})\n4: WIS ({stats_end[3]})\n5: INT ({stats_end[4]})\n6: CHA ({stats_end[5]})\n> ")) #choose which stat to apply roll to, repeats for each and updates to show which numbers you've selected
        index_choice = choice - 1
        stats_end[index_choice] = stats_mid[index] #sets your chosen number in final stat list
        clear() #clears screen each choice
            
    print(f" ———   ———   ———   ———   ———   ———  \n|{stats_end[0]}| |{stats_end[1]}| |{stats_end[2]}| |{stats_end[3]}| |{stats_end[4]}| |{stats_end[5]}|\n|STR| |DEX| |CON| |WIS| |INT| |CHA|\n ———   ———   ———   ———   ———   ———  ") #finally prints array of all stats
    if input("Apply racial bonuses? y/n > ").lower() == "y":
        clear()
        print("Races:\n1: Dwarf (Hill)\n2: Dwarf (Mountain)\n3: Elf (High)\n4: Elf (Wood)\n5: Elf (Drow)\n6: Halfling (Lightfoot)\n7: Halfling (Stout)\n8: Human\n9: Dragonborn\n10: Gnome (Forest)\n11: Gnome (Rock)\n12: Half-Elf\n13: Half-Orc\n14: Tiefling")
        race = input("Enter the number corresponding to your race. > ")
        race_bonuses_dict = {
            #####S D C W I C
            #####T E O I N H
            #####R X N S T A
            "1":[0,0,2,1,0,0],
            "2":[2,0,2,0,0,0],
            "3":[0,2,0,0,1,0],
            "4":[0,2,0,1,0,0],
            "5":[0,2,0,0,0,1],
            "6":[0,2,0,0,0,1],
            "7":[0,2,1,0,0,0],
            "8":[1,1,1,1,1,1],
            "9":[2,0,0,0,0,1],
            "10":[0,1,0,0,2,0],
            "11":[0,0,1,0,2,0],
            "12":[0,0,0,0,0,2],
            "13":[2,0,1,0,0,0],
            "14":[0,0,0,0,1,2]
            } #defines bonuses for each
            
        race_bonuses = race_bonuses_dict[race] #creates list of your race's bonuses
        
        if race == "12": #half elf
            while True:
                clear()
                choice_1 = int(input(f"Which stat would you like to assign your first +1 bonus to?\n1: STR\n2: DEX\n3: CON\n4: WIS\n5: INT\n6: CHA\n> "))
                choice_2 = int(input(f"Which stat would you like to assign your second +1 bonus to?\n1: STR\n2: DEX\n3: CON\n4: WIS\n5: INT\n6: CHA\n> "))
                if choice_1 == choice_2: #prevent choosing the same stat
                    print("You can't select the same stat twice!")
                    time.sleep(2)
                    continue
                else:
                    break
                
            race_bonuses[choice_1 - 1] = race_bonuses[choice_1 - 1] + 1 #adds first bonus
            race_bonuses[choice_2 - 1] = race_bonuses[choice_2 - 1] + 1 #adds second bonus
        for index, stat in enumerate(stats_end): #adds bonuses to base stats
            stats_rba[index] = int(stats_end[index]) + race_bonuses[index]
            stats_rba[index] = str(stats_rba[index]).zfill(3)
        clear()
        print(f" ———   ———   ———   ———   ———   ———  \n|{stats_rba[0]}| |{stats_rba[1]}| |{stats_rba[2]}| |{stats_rba[3]}| |{stats_rba[4]}| |{stats_rba[5]}|\n|STR| |DEX| |CON| |WIS| |INT| |CHA|\n ———   ———   ———   ———   ———   ———  ") #prints array