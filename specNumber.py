def specNumber():
     N = 0

     for i in range(1, 101):
         N = N + 1
         if N % 3 == 0 or N % 5 == 0:
             continue
         else:
             print(N)
specNumber()
