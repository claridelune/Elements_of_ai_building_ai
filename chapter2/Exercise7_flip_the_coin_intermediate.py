def count11(seq):
   count = 0
   find = False
   for i in seq:
       if(find):
           if(i == 1):
               count += 1
           find = False
       if(i == 1):
           find = True
   return count

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2
