# Print all Divisors of a number
n = 66
for i in range(1,((n+2)//2)):
  if (n%i == 0):
    print(i)
