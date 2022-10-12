#https://projecteuler.net/problem=3

import math
def is_prime(num):
  re_turn=True
  if num <= 0 or num == 1 :
      return False
  elif num == 2:
      return True
  else :
   for  i in range(2,int(math.sqrt(num))+1):
      if num % i == 0:
        re_turn=False
        break
  return re_turn



def prime_factor(num):
  factors=[]
  for i in range(1,int(math.sqrt(num))+1):
    if num % i == 0 and is_prime(i)==True:
      factors.append(i)
  return factors



t=600851475143
print(prime_factor(t))

