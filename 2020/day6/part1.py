#!/usr/bin/python


def load_input(path):

  with open(path, 'r') as f:
    data = f.read()

  return sum([len(set(party.replace('\n', ''))) for party in data.split('\n\n')])


if __name__ == '__main__':

  print load_input('./input.txt')

