#!/usr/bin/env python3
""" A - mortage amount
    b - interest rates plus the bank's margin
    n - number of installments to be repaid (loan period l (like years) multiplied by m, i.e. 12, because there are so many months in a year) 
    R - the amount of our installment 
    C - total amount to be repaid
    m - number of months per year """

b=4.7
m=12
A=300000
n=25*m

q=1+(b/(100*m))
print(f"q is: {q}")


R = A*(q**n)*(q-1)/((q**n)-1)
print(f"R is: {R}")

if __name__ == "__main__":
    print("Run as a separate program")
else:
    print("Imported interest calculator")
