import random
from math import sqrt, ceil

average_results = False #set to True to average out multiple trials; set to False to output each result individually

def estimate_pi(max_value, number_of_trials):

    coprimes = 0 # count of number of coprimes found
    cofactors = 0 # count of number of cofactors found

    for i in range(number_of_trials):
        num1 = random.randint(1, max_value)
        num2 = random.randint(1, max_value) #get next two random numbers

        primes1 = get_prime_factors(num1)
        primes2 = get_prime_factors(num2)

        for factor in primes1:
            if factor in primes2:
                cofactors += 1 #factor shared by both numbers
                break
        else: #no shared factor found
            coprimes += 1

    probability_of_coprime = coprimes / number_of_trials

    my_pi = sqrt(6/probability_of_coprime)

    return my_pi

def get_prime_factors(n):
    for i in range(2, ceil(sqrt(n))): # ceil so that 2 works.
        if n/i == n//i: # n is divisible by i
            return [i] + get_prime_factors(n//i) # 
    return [n] # no i found such that n is divisible by i; n is prime


max_rand_value = 1000000
number_of_trials = 10000

if average_results:
    results = []
    for i in range(10):
       results.append(estimate_pi(max_rand_value, number_of_trials))

    mean = sum(results)/len(results)
    print(mean)
else:
    for i in range(10):
        print(estimate_pi(max_rand_value, number_of_trials))

input()
