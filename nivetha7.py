int = 407
if int > 1:
   # check for factors
   for i in range(2,int):
       if (int % i) == 0:
           print(int,"is not a prime number")
           print(i,"times",int/i,"is",int)
           break
   else:
       print(int,"is a prime number")
else:
   print(int,"is not a prime number")
