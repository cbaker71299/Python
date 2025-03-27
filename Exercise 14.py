# Write a program that prompts the user to enter the
# three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and displays its area.
# The formula for computing the area of a triangle is
# Here is a sample run:
# s = (side1 + side 2 + side3) /2
# area = sqrt s(s - side1)(s - side2)(s - side3)


x1, y1 = eval(input("Enter x1 and y1 for point 1:")) #1.5, -3.4
x2, y2 = eval(input("Enter x2 and y2 for point 2:")) #4.6, 5
x3, y3 = eval(input("Enter x3 and y3 for point 3:")) #9.5, -3.4

side1 = ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)) ** 0.5    # distance of side 1 = 8.95377015563835
side2 = ((x2-x3)*(x2-x3) + (y2-y3)*(y2-y3)) ** 0.5    # distance of side 2 = 9.724710792614864
side3 = ((x3-x1)*(x3-x1) + (y3-y1)*(y3-y1)) ** 0.5    # distance of side 3 = 8.0

s = (side1 + side2 + side3) / 2

area = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5

print("The area of the triangle is", area)

