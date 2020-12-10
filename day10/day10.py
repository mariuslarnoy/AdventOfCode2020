def preprocess():
    f = open('day10/inputDay10.txt', 'r')

    input_list = []
    for line in f:
        input_list.append(int(line))

    input_list.sort()

    #adding the outlet and the device
    input_list.insert(0, 0)
    input_list.append(input_list[-1] + 3)

    return input_list


def part_1(input_list):

    one_jolt_count = 0
    three_jolt_count = 0

    for i in range(1, len(input_list)):

        if input_list[i] - input_list[i-1] == 1:
            one_jolt_count += 1
        elif input_list[i] - input_list[i-1] == 3:
            three_jolt_count += 1
    
    return one_jolt_count * three_jolt_count

def part_2(input_list):

    path_list = [0] * len(input_list)
    path_list[0] = 1

    for i in range(0, len(input_list)):

        if i + 1 < len(path_list) and input_list[i+1] - input_list[i] <= 3 and input_list[i+1] - input_list[i] > 0:
            path_list[i+1] += path_list[i]
        
        if i + 2 < len(path_list) and input_list[i+2] - input_list[i] <= 3 and input_list[i+2] - input_list[i] > 0:
            path_list[i+2] += path_list[i]

        if i + 3 < len(path_list) and input_list[i+3] - input_list[i] <= 3 and input_list[i+3] - input_list[i] > 0:
            path_list[i+3] += path_list[i]


    return path_list[-1]


def main():

    input_list = preprocess()

    print("Part 1: " + str(part_1(input_list)))
    print("Part 2: " + str(part_2(input_list)))

if __name__ == '__main__':
    main()