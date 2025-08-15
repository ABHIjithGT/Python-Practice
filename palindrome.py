#palindrome or not
n= 1234321
check = n
re = 0
while(n != 0):
  re = re*10
  re = re+(n%10)
  n = n//10
if (re == check)  :
  print("Palindrome")
else:
  print("Not a palindrome")  
