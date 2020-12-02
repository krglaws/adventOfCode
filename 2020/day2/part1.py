#!/usr/bin/python


# returns a list of strings
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

    input_list.append({'char': char, 'low': low, 'high': high, 'passwd': passwd})

  input_file.close()

  return input_list


def char_count(char, string):

  count = 0
  for currchar in string:
    if currchar == char:
      count += 1

  return count


# returns an int
def process_input(input_list):

  num_valid = 0

  for i in range(len(input_list)):

    char = input_list[i]['char']
    low = input_list[i]['low']
    high = input_list[i]['high']
    passwd = input_list[i]['passwd']

    count = char_count(char, passwd)

    if count >= low and count <= high:
      num_valid += 1

  return num_valid 


if __name__ == '__main__':

  input_list = load_input('./input.txt')
  print process_input(input_list)

