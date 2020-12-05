import numpy as np
import math

cabin = np.zeros((128,8))

highest_value = 0

f = open("day5/inputDay5.txt", "r")

for line in f:

    upper_row = 127.0
    lower_row = 0.0

    row_num = 0
    col_num = 0

    for i in range(0,7):
        if line[i] == 'F':
            upper_row = upper_row - math.ceil((upper_row-lower_row) / 2)
            

        elif line[i] == 'B':
            lower_row = lower_row + math.ceil((upper_row-lower_row) / 2)

    if line[6] == 'F':
        row_num = int(lower_row)
    elif line[6] == 'B':
        row_num = int(upper_row)

    upper_col = 7.0
    lower_col = 0.0

    for i in range(7,10):

        if line[i] == 'L':
            upper_col = upper_col - math.ceil((upper_col-lower_col) / 2)
        

        elif line[i] == 'R':
            lower_col = lower_col + math.ceil((upper_col-lower_col) / 2)

    if line[9] == 'L':
        col_num = int(lower_col)
    elif line[9] == 'R':
        col_num = int(upper_col)


    cabin[row_num,col_num] = (row_num * 8) + col_num

    if cabin[row_num,col_num] > highest_value:
        highest_value = cabin[row_num,col_num]

print("Highest value: " + str(highest_value))

#part2

my_ID = 0.0
for i in range(1, 128):
    for j in range(1, 7):
        if cabin[i,j] == 0.0:
            temp_ID = i * 8 + j
            if temp_ID - 1 == cabin[i,j-1] and temp_ID +1 == cabin[i,j+1] and cabin[i,j-1] != 0 and cabin[i,j+1] != 0:
                my_ID = temp_ID

print("My ID: " + str(my_ID))


        