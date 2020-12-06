#!/usr/bin/python


def load_input(path):

  with open(path, 'r') as f:
    data = f.read()

  parties = [party.split('\n') for party in data.split('\n\n')]

  total = 0
  for party in parties:

    common = list(party[0])

    for ind in party[1:]:
      if ind == '':
        continue
      ind = filter(lambda x: x is not None, ind)
      common = [c for c in common if c in ind]

    total += len(common)

  return total


if __name__ == '__main__':

  print load_input('./input.txt')


