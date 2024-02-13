import random

streak = 0
match = 0
misschance = 0.8
hit = 0
numstreak = 0

while (match < 50):
    match = match + 1
    hit = random.random()
    if (hit < misschance):
        streak = streak + 1
        print (streak)
    else:
        streak = 0
    if (streak > 7):
        numstreak = numstreak + 1

