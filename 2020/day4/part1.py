#!/usr/bin/python


# returns a list of dictionaries
def load_input(path):

  with open(path, 'r') as f:
    filestr = f.read()

  output = list()

  for ppstr in filestr.split('\n\n'):
    d = dict()
    fieldlist = ppstr.replace('\n', ' ').split(' ')
    for field in fieldlist:
      if field == '':
        continue
      keyval = field.split(':')
      d[keyval[0]] = keyval[1]
    output.append(d)

  return output


def no_empty_fields(d):

  keys = d.keys()

  for key in keys:
    if d[key] == '':
      return False 

  return True


# returns an int
def count_valid_passports(pplist):

  mandatory_fields = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])

  count = 0

  for pp in pplist:
    if not mandatory_fields.difference(set(pp.keys())):# and no_empty_fields(pp):
      count += 1
    else:
      continue

  return count


if __name__ == '__main__':

  passports = load_input('./input.txt')

  print count_valid_passports(passports)

