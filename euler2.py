#https://projecteuler.net/problem=2

def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False

first_num=1
seceond_num=2
summ=0
while(first_num<4000000):
    if is_even(first_num)==True:
        summ=summ+first_num
    new=first_num+seceond_num
    first_num=seceond_num
    seceond_num=new
    
print('sum is:' , summ)
#done