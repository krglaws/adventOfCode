#!/usr/bin/python


# returns a list of ints
def load_input(path):

  input_list = list()
  input_file = open(path, "r")

  for line in input_file:
    input_list.append(int(line))

  input_file.close()

  return input_list


# returns a tuple of two ints
def two_sum(input_list):

  goal = 2020
  s = set()

  for i in range(len(input_list)):

    curr = input_list[i]
    looking_for = (goal - curr)

    if looking_for in s:
      return (curr, looking_for)

    else:
      s.add(curr)

  print "didn't work"
  quit()


if __name__ == '__main__':

  input_list = load_input('./input.txt')
  nums = two_sum(input_list)

  print nums[0] * nums[1]

