# amstrong number or not
n = 153
check = n
am=0
while(n != 0):
  am1=n%10
  am=am+(am1**3)
  n=n//10
if (am == check)  :
  print("Amstrong")
else:
  print("Not a Amstrong")
