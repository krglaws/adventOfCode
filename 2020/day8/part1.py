#!/usr/bin/python


# hardware
MEM = list()
IP = 0
ACC = 0

seen_addrs = set()


def load_program(path):

  global MEM

  with open(path, 'r') as f:
    MEM = [line[:-1] for line in f.readlines()]


def fetch(addr):

  global MEM

  instr = MEM[addr].split()
  opcode = instr[0]
  operand = int(instr[1])

  return (opcode, operand)


def start():

  global IP
  global ACC

  while True:

    if IP in seen_addrs:
      return ACC
    else:
      seen_addrs.add(IP)

    instr = fetch(IP)

    if instr[0] == 'acc':
      ACC += instr[1]
      IP += 1

    elif instr[0] == 'nop':
      IP += 1
 
    elif instr[0] == 'jmp':
      IP += instr[1]

    else:
      print "invalid instruction:", instr
      quit()



if __name__ == '__main__':

  load_program('./input.txt')

  print start()

