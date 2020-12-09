#!/usr/bin/python

from time import time


def load_input(path):

  with open(path, 'r') as input_file:
    lines = [line[:-2] for line in input_file.readlines()]

  return lines


def parse_bags(lines):

  bag_map = dict()

  for line in lines:

    parent, children = line.replace(' bags', '', 1).split(' contain ')

    if 'other' in children:
      bag_map[parent] = []
      continue

    for child in children.split(', '):

      childls = child.split()

      count = int(childls[0])
      color = ' '.join(childls[1:3])

      if parent in bag_map.keys():
        bag_map[parent].append((count, color))
      else:
        bag_map[parent] = [(count, color)]

  return bag_map


memo = dict()

def count_bags_inside(color, bag_map):

  if color in memo.keys():
    return 1 + memo[color]

  total = sum(count * count_bags_inside(child, bag_map) for count, child in bag_map[color])
  memo[color] = total

  return 1 + total


if __name__ == '__main__':

  lines = load_input('./input.txt')

  start = time()

  bag_map = parse_bags(lines)
  print count_bags_inside('shiny gold', bag_map) - 1

  print "Time = %fms" % (1000 * (time() - start))

