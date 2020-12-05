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


def max_seat_id(passlist):

  return max([(calc_row_num(currpass['row']) * 8) + calc_col_num(currpass['col']) for currpass in passlist])


if __name__ == '__main__':

  print max_seat_id(load_input('./input.txt'))

