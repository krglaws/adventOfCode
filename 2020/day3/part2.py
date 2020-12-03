#!/usr/bin/python


# returns a list of strings
def load_input(file_path):

  lines = list()
  input_file = open(file_path, "r")

  for line in input_file:
    lines.append(line.strip())

  input_file.close()

  return lines


# returns an int
def count_trees(themap, slope):

  x = slope[0]
  y = slope[1]
  width = len(themap[0])
  height = len(themap)

  count = 0

  while y < height:

    if themap[y][x % width] == '#':
      count += 1

    x += slope[0]
    y += slope[1]

  return count


if __name__ == '__main__':

  themap = load_input('./input.txt')

  print (count_trees(themap, (1,1))*count_trees(themap, (3,1))*count_trees(themap, (5,1))*count_trees(themap, (7,1))*count_trees(themap, (1,2)))
