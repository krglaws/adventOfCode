#!/usr/bin/python

from time import time


def load_input(path):

  with open(path, 'r') as input_file:
    lines = [line[:-2] for line in input_file.readlines()]

  return lines


def parse_bags(lines):

  parent_map = dict()

  for line in lines:

    parent, children = line.replace(' bags', '', 1).split(' contain ')

    if 'other' in children:
      parent_map[parent] = []
      continue

    for child in children.split(', '):

      childls = child.split()

      count = int(childls[0])
      color = ' '.join(childls[1:3])

      if parent in parent_map.keys():
        parent_map[parent].append((count, color))
      else:
        parent_map[parent] = [(count, color)]

  return parent_map


def count_bags_inside(color, parent_map):

  return 1 + sum(count * count_bags_inside(child, parent_map) for count, child in parent_map[color])


if __name__ == '__main__':

  lines = load_input('./input.txt')

  parent_map = parse_bags(lines)

  print count_bags_inside('shiny gold', parent_map) - 1

