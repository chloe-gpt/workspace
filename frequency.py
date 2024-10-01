"""
Test for the frequency at which a specific random number is rolled
"""

def frequency():
    import random, os, time; from functions import restart, clear, file
    tries = 0; run = True #runs loop

    while run == True: #main loop to roll numbers
        st = time.time()
        rand = random.randint(10000,99999) #random number in range
        tries += 1 #increment number of rolls
        #print(str(tries) + " - " + str(rand)) #output result

        if rand == 66666: #end if number is reached
            end = time.time()
            tme = (round((end - st), 3))
            print("Success! It took " + str(tries) + " tries! " + str(tme) + "s")
            if tries == 66666:
                print("YOOOOO")
            file("logs/log04.txt", "a", tries); time.sleep(1) # appends to log file
            tries = 0; clear()