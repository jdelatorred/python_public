
import time
from functools import lru_cache

end = 40
fibonacci_cache = {}

#no performance using normal way
def fibonacci(n):
    #check the input
    if type(n) != int:
        raise TypeError("n Must be a positive int")
    if n < 1:
        raise ValueError("n Must be a positive int")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

#optimized metod using cache
def fibonacci_memoization(n):
    #check the input
    if type(n) != int:
        raise TypeError("n Must be a positive int")
    if n < 1:
        raise ValueError("n Must be a positive int")
    #if we have cached the value then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    #cache the value and return it
    fibonacci_cache[n] = value
    return value

#using lru cache from functools improves performance
@lru_cache(maxsize = 1000)
def fibonacci_lru_cache(n):
    #check the input
    if type(n) != int:
        raise TypeError("n Must be a positive int")
    if n < 1:
        raise ValueError("n Must be a positive int")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

time1 = time.time()
for n in range(1, end):
    print(n, ":", fibonacci(n), " With Normal Method")
print("Time for normal way", time.time() - time1)

time2 = time.time()
for n in range(1, end):
    print(n, ":", fibonacci_memoization(n), " With Memorization Method")
print("Time for Cache way", time.time() - time2)

time3 = time.time()
for n in range(1, end):
    print(n, ":", fibonacci_lru_cache(n), " With Memorization LRU Cache Method")
print("Time for Cache LRE way", time.time() - time3)