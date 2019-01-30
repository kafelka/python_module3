#this script checks if a given number is a prime number

def is_prime(number):
    for num in range(2, number):
        
        if number % num == 0:
            return False
        
    return True

#print(is_prime(10))

def next_prime(number):
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
            
#print(next_prime(5))