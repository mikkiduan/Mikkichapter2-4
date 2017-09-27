# p is principal amount
p = 10000

#n is number of times per year
n = 12

#r is interest rate
r = .88

# t is number of year money is compounded for
t = float(input("Enter the number of years:"))

#the following line has an error
a = p*(1+r/n)**(n*t)

print("Amountwith interest is: " + str(a))