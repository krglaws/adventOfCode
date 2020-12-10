#!/usr/bin/python


# returns a list of ints
def load_input(path):

  with open(path, 'r') as f:
    nums = [int(line) for line in f.readlines()]

  return nums 


# returns a boolean
def has_two_sum(target, num_range):

  seen = set()

  for i in range(len(num_range)):

    curr = num_range[i]
    looking_for = target - curr

    if looking_for in seen:
      return True

    else:
      seen.add(curr)

  return False



def find_first_false(nums):

  for i in range(len(nums))[25:]:

    curr = nums[i]
    num_range = nums[:i]

    if has_two_sum(curr, num_range) == False:
      return curr

  return None


if __name__ == '__main__':

  nums = load_input('./input.txt')
  print find_first_false(nums)

