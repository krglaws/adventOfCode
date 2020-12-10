#!/usr/bin/python


# returns a list of ints
def load_input(path):

  with open(path, 'r') as f:
    nums = [int(line) for line in f.readlines()]

  return nums 


def find_sum_range(target, nums):

  for i in range(len(nums)):

    j = i
    curr_sum = 0
    while curr_sum < target:

      curr_sum += nums[j]
      j += 1

    curr_range = sorted(nums[i:j])

    if curr_sum == target:
      return curr_range[0] + curr_range[-1]


if __name__ == '__main__':

  nums = load_input('./input.txt')

  print find_sum_range(23278925, nums)

