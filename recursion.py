#find the sum of n numbers 
n=5 
total = 0 
for i in range(6):
    total += i 

print (total)

def sumofnumbers(n):
    if n == 1 or n == 0:
        return n 
    else:
        return n+ sumofnumbers(n-1) 

print(sumofnumbers(5))

#fibonacci sequence 
def fibonaacci(n):
    if n == 1 or n == 0:
        return n 
    else:
        return fibonaacci(n-2) + fibonaacci (n-1)
print (fibonaacci (5)) 

# factorial 

def factorial(n):
    if n == 1 or n == 0:
        return n 
    else: 
        return factorial (n-1)*n 

print (factorial (5))

#powers 

def powers(n,x):
    if x ==1:
        return n 
    else:
        if x %2 == 0:
            return (powers(n,x//2)*powers(n,x//2))
        else:
            return (x*powers(n,x//2)*powers(n,x//2))

print(powers (5,2))