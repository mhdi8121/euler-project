#https://projecteuler.net/problem=48

self_power=[]

for i in range(1,(10**3)+1):
    self_power.append(i**i)

sumetion=str(sum(self_power))
print(sumetion[-10:])
