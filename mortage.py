#!/usr/bin/env python3
""" A - mortage amount
    b - interest rates plus the bank's margin
    n - number of installments to be repaid (loan period l (like years) multiplied by m, i.e. 12, because there are so many months in a year) 
    R - the amount of our installment 
    C - total amount to be repaid
    m - number of months per year """



b=5/100
m=12
A=500000
n=15*m

q=1+(b/m)
# print(f"q is: {q}")


R = A*(q**n)*(q-1)/((q**n)-1)
print(f"A is: {A}")
print(f"R is: {R}")
C1=R*n


##
Rk=A/n
C2=0
print(f"A is: {A}")
for x in range(1,n):
 #   print(f"\nInstalment number: {x}")
    Ro=((A-x*Rk)*b)/12
 #   print(f"Rk is: {Rk}")
    total=Rk+Ro
    print(f"Ro is: {Ro},Monthly payment: {total}")
    if (x%12) == 0:
        print("\n")
    
  #  print(f"total is: {total}")
    C2+=total

print(f"\n\nC1 is: {C1}")
print(f"C2 is: {C2}")
if __name__ == "__main__":
    print("")
    # print("Run as a separate program")
else:
    print("")
    # print("Imported interest calculator")
