#https://projecteuler.net/problem=16

a=2**1000
sum=0
for i in range(303):
    sum+=int(a%10)
    a=a//10
print(sum)