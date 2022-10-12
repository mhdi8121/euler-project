#https://projecteuler.net/problem=6

def sum_of_the_squares(n) :
    sum1=0
    for i in range(n+1) :
        sum1=i**2+ sum1
    return sum1
#print(sum_of_the_squares(100))
def square_of_the_sum(n) :
    sum1=0
    for i in range(n+1) :
        sum1=i+sum1
        square_sum=sum1**2
    return square_sum
#print(square_of_the_sum(10))

print('answer is:%i'%(square_of_the_sum(100)-sum_of_the_squares(100)))
#done