#!/usr/bin/python


# returns a list of chars
def load_input(path):

  input_file = open(path, "r")
  path = list()

  column = 0
  width = 0

  for line in input_file:

    line = line.strip()

    if column == 0:
      column += 3
      width = len(line)
      continue

    index = column % width
    path.append(line[index])
    column += 3

  return path


if __name__ == '__main__':

  path = load_input('./input.txt')

  count = 0
  for spot in path:
    if spot == '#':
      count += 1

  print count

