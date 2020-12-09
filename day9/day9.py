def preprocess():

    f = open('day9/inputDay9.txt', 'r')

    #cleanup, convert to int list
    input_list = []
    for line in f:
        input_list.append(int(line))
    
    return input_list

def sum_all(input_list):

    sums = []
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if i != j:
                sums.append(input_list[i] + input_list[j])

    return sums

def part1(input_list):

    #start at 25, first index outside preamble
    currentIndex = 25
    preamble = input_list[:25]
    

    while True:
        if input_list[currentIndex] in sum_all(preamble):
            preamble = preamble[1:]
            preamble.append(input_list[currentIndex])
            currentIndex += 1
        
        else:
            break
    
    return input_list[currentIndex]

def part2(input_list, invalid_number):

    temp_list = input_list
    while True:

        contigous = []
        counter = 0


        for i in range(0, len(temp_list)):

            if counter > invalid_number:
                temp_list = temp_list[1:]
                break
            
            elif counter == invalid_number:
                contigous.append(temp_list[i])
                return min(contigous) + max(contigous)
                

            else:
                contigous.append(temp_list[i])
                counter += temp_list[i]
 

def main():
    invalid_number = part1(preprocess())
    print("Part 1: " + str(invalid_number))

    encryption_weakness = part2(preprocess(), invalid_number)
    print("Part 2: " + str(encryption_weakness))

if __name__ == "__main__":
    main()
