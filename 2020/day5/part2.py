#!/usr/bin/python

def load_input(path):

  with open(path, 'r') as input_file:
    filestr = input_file.read()

  output = [{'row': bp[:7], 'col': bp[7:]} if bp is not '' else None for bp in filter(lambda x: x is not '', filestr.split('\n'))]

  return output


def calc_row_num(rowstr):

  binstr = ''.join(['1' if char == 'B' else '0' for char in rowstr])

  return int(binstr, 2)


def calc_col_num(colstr):

  binstr = ''.join(['1' if char == 'R' else '0' for char in colstr])

  return int(binstr, 2)


def pass_exists(passlist, row, col):

  for p in passlist:
    if calc_row_num(p['row']) == row and calc_col_num(p['col']) == col:
      return True

  return False


def find_missing_seat(passlist):

  rownums = [calc_row_num(p['row']) for p in passlist]

  highrow = max(rownums)
  lowrow = min(rownums)

  for row in range(lowrow + 1, highrow):
    for col in range(0, 8):
      if not pass_exists(passlist, row, col):

        return (row * 8) + col

  return -1


if __name__ == '__main__':

  passlist = load_input('./input.txt')
  
  print find_missing_seat(passlist)

