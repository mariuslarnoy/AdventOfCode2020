from itertools import groupby 
#preprocessing
f = open("inputDay4.txt", "r")

lines = f.read().strip()
lines = lines.split("\n")

res = [list(sub) for ele, sub in groupby(lines, key = bool) if ele] 

cleaned_passords = []

for id in res:

    cleaned_id = []
    for value in id:
        cleaned_id.append(value.split(" "))

    flat_list = [item for sublist in cleaned_id for item in sublist]
    cleaned_passords.append(flat_list)


def check_missing_field(id):
    for ele in id:
        field = ele[:3]
        if field == "cid":
            return False
    return True

def check_valid_fields(id):
    for ele in id:
        field = ele[:3]
        if field == "byr":
            value = ele[4:]
            if int(value) < 1920 or int(value) > 2002:
                return False
        elif field == "iyr":
            value = ele[4:]
            if int(value) < 2010 or int(value) > 2020:
                return False

        elif field == "eyr":
            value = ele[4:]
            if int(value) < 2020 or int(value) > 2030:
                return False

        elif field == "hgt":
            value = ele[4:]
            measure = value[-2:]
            number = value [:-2]
            if measure == "cm":
                if int(number) < 150 or int(number) > 193:
                    return False
            elif measure == "in":
                if int(number) < 59 or int(number) > 76:
                    return False
        elif field == "hcl":
            value = ele[4:]
            if value[0] != "#":
                return False
                
            colour = value[1:]
            if len(colour) != 6:
                return False

            num_dict = ['0','1','2','3','4','5','6','7','8','9']
            alp_dict = ['a','b','c','d','e','f']

            for letter in colour:
                if not(letter in num_dict or letter in alp_dict):  
                    return False


        elif field == "ecl":
            eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            value = ele[4:]

            if not value in eye_colours:
                return False

        elif field == "pid":
            value = ele[4:]
            if not len(value) == 9:
                return False

    return True

#check for validity
counter = 0
for id in cleaned_passords:
    if len(id) == 8:
        if check_valid_fields(id):
            counter += 1
    elif len(id) == 7:
        if check_missing_field(id):
            if check_valid_fields(id):
                counter += 1
        

print("Valid id's: " + str(counter))
