def g(n):
  for i in range(2,n):
    if n%i == 0:
       return(False)

  return(True)
print(g(5))
