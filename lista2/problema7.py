def primeList():
    number = 1
    while number < 100:
        if isPrime(number): yield number
        number += 1

def isPrime(n):
  for i in range(2,n):
    if (n%i) == 0: return False
  return True
