#https://projecteuler.net/problem=7

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

prime_list=[]
i=0
while len(prime_list)<=10000:
    if is_prime(i)==True:
        prime_list.append(i)
    i+=1
print(prime_list[-1])

#t=600851475143
#print(is_prime(t))
