#https://projecteuler.net/problem=1



numbers=list()
summ=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        numbers.append(i)
        summ =i+summ

print ( 'summ var is %s and sum fun is %s ' %(summ,sum(numbers)))
#done