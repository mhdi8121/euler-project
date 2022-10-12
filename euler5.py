#https://projecteuler.net/problem=5


numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
prime_num=list()
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

for num in numbers:
    if is_prime(num):
        prime_num.append(num)
print(prime_num)
print(16*9*5*7*11*13*17*19)