#!/usr/bin/python

def load_input(path):

  with open(path, "r") as input_file:
    text = input_file.read()

  return text.split('\n')[:-1]



def parse_bags(lines):

  bags = dict()

  for line in lines:
    key_end = line.index('bags')
    baglist = map(lambda bag: bag[3:].split(' ')[0:2], line[line.index('contain') + len('contain'):-2].split(','))
    if baglist[0][1] == 'other':
      bags[' '.join(line.split(' ')[:2])] = set([])
    else:
      for i in range(len(baglist)):
        baglist[i] = ' '.join(baglist[i])
      bags[' '.join(line.split(' ')[:2])] = set(baglist)

  return bags


target = 'shiny gold'
has_target = set()


def _find_all_paths(curr, bags):

  if curr == target:
    return False

  inner_bags = bags[curr]

  if inner_bags == set([]):
    return False

  if target in inner_bags:
    if curr not in has_target:
      has_target.add(curr)
    return True

  if inner_bags & has_target:
    if curr not in has_target:
      has_target.add(curr)
    return True

  result = False

  for bag in inner_bags:
    if _find_all_paths(bag, bags):
      result = True
      if bag not in has_target:
        had_target.add(bag)

  if result == True and curr not in has_target:
    has_target.add(curr)

  return result


def find_all_paths(bags):

  for key in bags.keys():
    _find_all_paths(key, bags)

  return len(has_target)


if __name__ == '__main__':

  lines = load_input('./input.txt')

  bags = parse_bags(lines)

  print find_all_paths(bags)
