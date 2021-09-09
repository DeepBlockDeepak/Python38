#!python3
'''
Problem: Given a number, find the next number which has the same number of ON bits
Ex: Given 6 (0b110), return 9 (0b1001)
'''

#readable-shmeadable, comments-shmomments
one_bit_counter = lambda x: 0 if x ==0 else ((x&1) + one_bit_counter(x>>1))

def bit_finder(x):

  next_val = x + 1
  while(one_bit_counter(next_val) != one_bit_counter(x)):
    next_val += 1
  
  return next_val


for i,j in zip(range(1,12), list(map(bit_finder, range(1,12)))):
  print(
    "-- {} has the same # of ON-bits as {} --".format(i,j)
  )
