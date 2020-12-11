import copy

def preprocess():
    f = open('day11/inputDay11.txt', 'r')

    input_list = []

    for line in f:
        cleaned_line = line.strip()
        input_list.append([char for char in cleaned_line])

    return input_list

def transform(input_list):
    result_list = copy.deepcopy(input_list)

    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):

            if input_list[i][j] == 'L':
                if rule_1(i,j, input_list):
                    result_list[i][j] = '#'

            elif input_list[i][j] == '#':
                if rule_2(i,j, input_list):
                    result_list[i][j] = 'L'

    return result_list

def rule_1(i, j, input_list):
    valid_x = [x for x in range(0, len(input_list))]
    valid_y = [y for y in range(0, len(input_list[0]))]
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if i+x in valid_x and j+y in valid_y:
                if input_list[i + x][j + y] == '#' and (x != 0 ^ y != 0):
                    return False
             
    return True

def rule_2(i, j, input_list):

    occupied_counter = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if i+x in range(len(input_list)) and j+y in range(len(input_list[0])) and input_list[i + x][j + y] == '#' and (x != 0 ^ y != 0):  
                occupied_counter += 1
    
    if occupied_counter >= 4:
        return True

    else:
        return False

def count_occupied(input_list):
    counter = 0
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if input_list[i][j] == '#':
                counter += 1
    
    return counter

def part_1(input_list):
    
    list_copy = copy.deepcopy(input_list)
    prev = copy.deepcopy(input_list)
    
    while True:
        print("\n")
        for line in list_copy:
            print(line)

        list_copy = copy.deepcopy(transform(list_copy))
        
        if prev == list_copy:
            return count_occupied(prev)

        prev = copy.deepcopy(list_copy)

def main():
    print("Part 1: " + str(part_1(preprocess())))

if __name__ == '__main__':
    main()