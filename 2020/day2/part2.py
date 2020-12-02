#!/usr/bin/python


# returns a list of dictionaries
def load_input(path):

  input_list = list()
  input_file = open(path, "r")

  for line in input_file:

    rule, passwd = line.split(':')
    passwd = passwd.strip()

    low, high = rule.split('-')
    low = int(low)
    high, char = high.split(' ')
    high = int(high)

    input_list.append({'char': char, 'positions': (low, high), 'passwd': passwd})

  input_file.close()

  return input_list


def check_positions(char, string, pos):

  pos1 = pos[0] - 1
  pos2 = pos[1] - 1

  if (pos1 > len(string)-1 or pos1 < 0 or pos2 > len(string)-1 or pos2 < 0):
    return False

  char1 = string[pos1]
  char2 = string[pos2]

  return (char1 == char and char2 != char) or (char2 == char and char1 != char)


# returns an int
def process_input(input_list):

  num_valid = 0

  for i in range(len(input_list)):

    currdict = input_list[i]

    if check_positions(currdict['char'], currdict['passwd'], currdict['positions']):
      num_valid += 1

  return num_valid 


if __name__ == '__main__':

  input_list = load_input('./input.txt')
  print process_input(input_list)

