#!/usr/bin/python

import time


# hardware
MEM = list()
IP = 0
ACC = 0


def load_program(path):

  global MEM

  with open(path, 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  MEM = [[line.split()[0], int(line.split()[1])] for line in lines]


def fetch(addr):

  global MEM

  return MEM[addr]


def start():

  global IP
  global ACC

  # set of candidate instruction addresses
  # that don't fix program when flipped.
  dont_change = set()

  # list of instruction addresses previously
  # executed in sequence.
  seen = list()

  # the index in 'seen' where we last tried
  # flipping an instruction
  reset_seen_index = -1

  # old 'ACC' value before last instruction
  # flip
  ACC_old = 0

  # old 'IP' value before last instruction
  # flip
  IP_old = 0

  while True:

    #time.sleep(0.5)

    print "IP =", IP

    # check if end reached
    if IP == len(MEM):
      print "End of program reached."
      return ACC

    # check for infinite loop
    if IP in seen:
      print "Infinite loop detected at ", IP

      seen = seen[:reset_seen_index]
      reset_seen_index = -1

      IP = IP_old
      ACC = ACC_old
      print "Reset to", IP
      continue

    seen.append(IP)
    instr = fetch(IP)

    print "Executing", instr

    if instr[0] == 'acc':
      ACC += instr[1]
      IP += 1

    elif instr[0] == 'nop':

      # check if this is a good candiate for flipping
      if reset_seen_index == -1 and instr[1] != 0 and IP not in dont_change:

        print "Flipping 'nop' to 'jmp' at", IP

        dont_change.add(IP)
        ACC_old = ACC
        IP_old = IP
        reset_seen_index = len(seen) - 1

        # do jmp instead
        IP += instr[1]

      else:
        IP += 1
 
    elif instr[0] == 'jmp':

      if reset_seen_index == -1 and IP not in dont_change:

        print "Flipping 'jmp' to 'nop' at", IP

        dont_change.add(IP)
        ACC_old = ACC
        IP_old = IP
        reset_seen_index = len(seen) - 1

        # do nop instead
        IP += 1

      else:
        IP += instr[1]

    else:
      print "invalid instruction:", instr
      quit()


if __name__ == '__main__':

  load_program('./input.txt')

  print start()

