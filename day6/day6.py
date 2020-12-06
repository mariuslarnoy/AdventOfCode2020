from itertools import groupby 

def split(word): 
    return [char for char in word]

f = open("day6/inputDay6.txt", "r")

#preprocessing
groups = f.read().strip()
groups = groups.split("\n")

groups = [list(sub) for ele, sub in groupby(groups, key = bool) if ele] 

def part1(input):
    yes_counter = 0

    for i in range(0,len(input)):

        questions = ""
        for ele in input[i]:
            questions += ele

        questions = set(split(questions))
        yes_counter += len(questions)

    return yes_counter


def part2(input):
    yes_counter = 0

    for i in range(0,len(groups)):

        initial = split(input[i][0])
        for ele in groups[i]:
            initial = list(set(initial) & set(split(ele)))

        yes_counter += len(initial)

    return yes_counter

print("Part1: Yes-answers in total: " + str(part1(groups)))
print("Part2: Yes-answers in total: " + str(part2(groups)))
