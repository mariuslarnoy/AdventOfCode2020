def preprocess():
    f = open('day12/inputDay12.txt', 'r')

    input_list = []
    for line in f:
        input_list.append(line.strip())
    
    return input_list


def part_1(input_list):

    facing = 'E'
    vertical = 0
    horizontal = 0

    for instruction in input_list:
        letter = instruction[0]
        number = int(instruction[1:])

        facing, vertical, horizontal = update_position(facing, vertical, horizontal, letter, number)


    return abs(vertical) + abs(horizontal)   

def update_position(facing, vertical, horizontal, letter, number):

    if letter == 'E':
        horizontal += number
    elif letter == 'S':
        vertical -= number
    elif letter == 'W':
        horizontal -= number
    elif letter == 'N':
        vertical += number
    elif letter == 'F':
        if facing == 'E':
            horizontal += number
        elif facing == 'S':
            vertical -= number
        elif facing == 'W':
            horizontal -= number
        elif facing == 'N':
            vertical += number
    else:
        facing = change_direction(facing, letter, number)
    
    return (facing, vertical, horizontal)

def change_direction(current_direction, left_or_right, degrees):
    
    poles = ['N', 'E', 'S', 'W']
    number_of_steps = degrees / 90

    index = 0
    for i in range(0, 4):
        if poles[i] == current_direction:
            index = i
    
    #gross solution to this turning shit
    poles = poles * 3
    index += 4

    #turn left
    if left_or_right == 'L':
        return poles[index - number_of_steps]
    #turn right
    else:
        return poles[index + number_of_steps]


def part_2(input_list):
    
    wp_vertical = 1
    wp_horizontal = 10

    vertical = 0
    horizontal = 0

    for instruction in input_list:
        letter = instruction[0]
        number = int(instruction[1:])

        wp_vertical, wp_horizontal, vertical, horizontal = update_position_p2(wp_vertical, wp_horizontal, vertical, horizontal, letter, number)

def update_position_p2(wp_vertical, wp_horizontal, vertical, horizontal, letter, number):
    
    #another shit solution, never too many ifs
    if letter in ['N', 'E', 'S', 'W']:
        if letter == 'N':
            wp_vertical += number
        elif letter == 'E':
            wp_horizontal += number
        elif letter == 'S':
            wp_vertical -= number
        elif letter == 'W':
            wp_horizontal -= number
    else:
        if letter == 'L':
            #1st quadrant
            if wp_horizontal > horizontal and wp_vertical > vertical:

                if number == 90:
                    wp_horizontal -= 14
                    wp_vertical += 
            #2nd quadrant
            elif wp_horizontal < horizontal and wp_vertical > vertical:
            #3rd quadrant
            elif wp_horizontal < horizontal and wp_vertical < vertical:
            
            #4th
            else:

        
        #'R'
        else:

    return (wp_vertical, wp_horizontal, vertical, horizontal)

def main():
    print(str(part_1(preprocess())))

if __name__ == '__main__':
    main()