# Check prime number
n = 17
count = 0
for i in range(2,((n+2)//2)):
  if (n%i == 0):
    print("Not a prime number")
    count = 1
    break
if count == 0:
  print("Prime number")
