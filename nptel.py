'''
Objective : to check if a number is prime or not
return value: True if Prime
              False if Non-Prime
'''

def checkPrime(n):
  for i in range(2,n):
    if n%i == 0:
       return(False)

  return(True)
print(checkPrime(5))
