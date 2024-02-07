streak = 0
match = 0
misschance = 0.5
hit = 0
numstreak = 0

while (match < 10):
    match = match + 1
    hit = random(0,1)
    if (hit < misschance):
        streak = streak + 1
    else:
        streak = 0
    if (streak > 7):
        numstreak = numstreak + 1

