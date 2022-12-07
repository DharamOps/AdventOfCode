#!/usr/bin/env python3

import re

#create function to read lines from input file
input_file = open('input.txt', 'w')
lineSpaces = input_file.readlines()

#remove spaces from lines
lines = [line.replace(' ', '') for line in lineSpaces]

#rewrite file with new lines
input_file.writelines(lines)

input_file.close()
#create array
elf = []
elf = input_file.read().split('\n\n')

print(elf)
