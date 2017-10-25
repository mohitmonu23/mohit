'''
Objective: this code checks if a number is prime or not
return Value: True for Prime
              False for non-Prime
Changes done: range is decreased from 2-num to 2-num//2
              it will work more efficiently as compared to last code
'''


def checkPrime(num):
  for i in range(2,num//2):
    if num%i == 0:
       return(False)

  return(True)
print(checkPrime(5))
