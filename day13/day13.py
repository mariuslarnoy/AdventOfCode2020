import math
from itertools import count

def part_1(): 

    f  = open('day13/inputDay13.txt', 'r')

    departure = int(f.readline())
    bus_table = list(map(int,filter(lambda x: x != 'x', [bus for bus in f.readline().split(',')])))

    best_ID = 0
    best_wait = 100000000 #big number lol

    for bus in bus_table:
        current_ID = bus
        table = []
        for i in range(0, 100000):
            table.append(current_ID * i)
        
        table = filter(lambda x: x > departure, table)
        if table[0] - departure < best_wait:
            best_ID = current_ID
            best_wait = table[0] - departure

    print(str(best_ID * best_wait))


def part_2():
    f  = open('day13/inputDay13.txt', 'r')

    departure = int(f.readline())
    counter_table = [bus for bus in f.readline().split(',')]
    bus_table = list(map(int,filter(lambda x: x != 'x', counter_table)))

    offset_dict = {}

    #add keys to dict
    for bus in bus_table:
        offset_dict[bus] = 0


    print(offset_dict)
    

part_2()