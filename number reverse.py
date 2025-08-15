# number reverse
n= 1234
re = 0
while(n != 0):
  re = re*10
  re = re+(n%10)
  n = n//10
print(re)  
  
