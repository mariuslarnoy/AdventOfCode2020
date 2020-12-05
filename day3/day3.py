import numpy as np
import re

slope_length = 323

def split(word):
    return [char for char in word]


def createArray():

    f = open("inputDay3.txt", "r")

    array = []
    
    for line in f:
        valids = re.sub("\n", '', line)
        column = split(valids)
        while (len(column) < slope_length*3):
            column = column*3
        
        array.append(column)

    return array

hill = createArray()

row_pos = 1
col_pos = 1
tree_counter1 = 0
while (row_pos < len(hill)):
    
    if (hill[row_pos][col_pos] == '#'):
        tree_counter1 += 1

    col_pos += 1
    row_pos += 1

print("Right 1, down 1: " + str(tree_counter1))


row_pos = 1
col_pos = 3
tree_counter2 = 0
while (row_pos < len(hill)):
    
    if (hill[row_pos][col_pos] == '#'):
        tree_counter2 += 1

    col_pos += 3
    row_pos += 1

print("Right 3, down 1: " + str(tree_counter2))

row_pos = 1
col_pos = 5
tree_counter3 = 0
while (row_pos < len(hill)):
    
    if (hill[row_pos][col_pos] == '#'):
        tree_counter3 += 1

    col_pos += 5
    row_pos += 1

print("Right 5, down 1: " + str(tree_counter3))

row_pos = 1
col_pos = 7
tree_counter4 = 0
while (row_pos < len(hill)):
    
    if (hill[row_pos][col_pos] == '#'):
        tree_counter4 += 1

    col_pos += 7
    row_pos += 1

print("Right 7, down 1: " + str(tree_counter4))

row_pos = 2
col_pos = 1
tree_counter5 = 0
while (row_pos < len(hill)):
    
    if (hill[row_pos][col_pos] == '#'):
        tree_counter5 += 1

    col_pos += 1
    row_pos += 2

print("Right 1, down 2: " + str(tree_counter5))

print("Multiplied: " + str(tree_counter1*tree_counter2*tree_counter3*tree_counter4*tree_counter5))