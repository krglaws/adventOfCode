#!/usr/bin/python


# returns a list of ints
def load_input(path):

  input_list = list()
  input_file = open(path, "r")

  for line in input_file:
    input_list.append(int(line))

  input_file.close()

  return input_list


# returns a tuple of three ints
def three_sum(input_list):

  goal = 2020
  input_list = sorted(input_list)
  input_len = len(input_list)

  for i in range(input_len - 2):

    j = i + 1
    k = input_len - 1

    while (j < k):

      inum = input_list[i]
      jnum = input_list[j]
      knum = input_list[k]

      currsum = (inum + jnum + knum)

      if currsum < goal:
        j += 1

      elif currsum > goal:
        k -= 1

      else:
        return (inum, jnum, knum)

  print "didn't work"
  quit()


if __name__ == '__main__':

  input_list = load_input('./input.txt')
  nums = three_sum(input_list)

  print nums[0] * nums[1] * nums[2]

