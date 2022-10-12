#https://projecteuler.net/problem=10

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

prime_below_two_million=[]

for i in range(1,2*10**6):
    if is_prime(i)==True:
        prime_below_two_million.append(i)

print(prime_below_two_million)
print(sum(prime_below_two_million))