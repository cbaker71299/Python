# Write a program that
# reads in an investment amount, the annual interest rate, and the number of years,
# and displays the future investment value using the following formula.

# futureinvestmnentValue = investment amount * (1 + monthly interest rate)^Number of months

investmentAmount = eval(input("Enter investment amount:"))      #1000
annualInterestrate = eval(input("Enter annual interest rate:"))    #4.25
numberofYears = eval(input("Enter number of years:"))      #1

monthlyinterestrate = annualInterestrate / 12
numberofmonths = numberofYears / 12

futureinvestmentvalue = investmentAmount * (1 + monthlyinterestrate) ** numberofmonths

print("The accumulated value is",futureinvestmentvalue)

# my answer is 1025.5873999640332
# the answer is supposed to be 1043.33

#SOMETHING IS WRONG ****************************************************************