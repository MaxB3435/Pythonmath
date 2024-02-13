import random

streak = 0
streaklength = 8
match = 0
misschance = 0.5
numstreak = 0
season = 0
numseason = 10000

while season <= numseason:
    while match <= 52:
        if season == numseason:
            print(numstreak/(numseason/100),'%')
            exit()
        if match == 52:
           match = 0
           season = season +1
           
        match = match + 1
        if random.random() < misschance:
            streak = streak + 1
        else:
            streak = 0
        if streak == streaklength:
            numstreak = numstreak + 1
            streak = 0
            match = 0
            season = season +1


