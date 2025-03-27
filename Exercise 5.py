# Write a program that reads the subtotal and
# the gratuity rate and computes the gratuity and total. For example, if the user
# enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
# as the gratuity and 11.5 as the total. Here is a sample run:

subtotal = eval(input("Enter the subtotal:"))
gratuityRate = eval(input("Enter the gratuity rate:"))

gratuity = gratuityRate / subtotal
total = subtotal + gratuity

print("The gratuity is",gratuity)
print("The total is",total)
