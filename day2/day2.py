import re

f = open("inputDay2.txt", "r")

counter = 0
for line in f: 

    
    rule_password = line.split(":")

    password = rule_password[1]
    character_in_focus = rule_password[0][-1]

    firstpos,secondpos = rule_password[0][:-1].split("-")

    valids = re.sub(r"[^a-z]+", '', password)
    
    if (valids[int(firstpos) - 1] == character_in_focus) ^ (valids[int(secondpos) - 1] == character_in_focus):
        counter += 1


print("counter: " + str(counter))
