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


def valid_byr(byr):

  if len(byr) != 4:
    return False

  if int(byr) < 1920 or int(byr) > 2002:
    return False

  return True


def valid_iyr(iyr):

  if len(iyr) != 4:
    return False

  if int(iyr) < 2010 or int(iyr) > 2020:
    return False

  return True


def valid_eyr(eyr):

  if len(eyr) != 4:
    return False

  if int(eyr) < 2020 or int(eyr) > 2030:
    return False

  return True


def valid_hgt(hgt):

  if len(hgt) < 4 or len(hgt) > 5:
    return False

  unit = hgt[-2:]
  num = 0
  try:
    num = int(hgt[:-2])
  except ValueError:
    return False

  if unit != 'cm' and unit != 'in':
    return False

  if unit == 'cm' and (num < 150 or num > 193):
    return False

  if unit == 'in' and (num < 59 or num > 76):
    return False

  return True


def valid_hcl(hcl):

  if len(hcl) != 7:
    return False

  if hcl[0] != '#':
    return False

  try:
    int(hcl[1:], 16)
  except ValueError:
    return False

  return True


def valid_ecl(ecl):

  if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
    return False

  return True


def valid_pid(pid):

  if len(pid) != 9:
    return False

  try:
    int(pid)
  except ValueError:
    return False

  return True


# returns an int
def count_valid_passports(pplist):

  #mandatory_fields = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])

  count = 0

  for pp in pplist:
    try:
      if not valid_byr(pp['byr']):
        continue
      if not valid_iyr(pp['iyr']):
        continue
      if not valid_eyr(pp['eyr']):
        continue
      if not valid_hgt(pp['hgt']):
        continue
      if not valid_hcl(pp['hcl']):
        continue
      if not valid_ecl(pp['ecl']):
        continue
      if not valid_pid(pp['pid']):
        continue
      count += 1
    except KeyError:
      continue

  return count


if __name__ == '__main__':

  passports = load_input('./input.txt')

  print count_valid_passports(passports)

