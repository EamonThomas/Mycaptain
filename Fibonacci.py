#Program by Eamon Thomas

no_of_terms = int(input("How many terms? "))

n1, n2 = 0, 1
n3 = 0

if no_of_terms == 1:
   print("Fibonacci sequence upto",no_of_terms,":")
   print(n1)
# generating fibonacci sequence
else:
   print("Fibonacci sequence upto ",no_of_terms,":")
   while n3 < no_of_terms:
       print(n1)
       add = n1 + n2
       n1 = n2
       n2 = add
       n3 += 1
