"""
File: quadratic_solver.py
Name: Tony
Time spent: 16 min (not include note)
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

import math


def main():
	"""
	This main function asks user to enter three integers for variables (a, b, and c), which
	will represent the coefficient of a quadratic function. The main function will then
	calculate the root of this quadratic function and tell the user how many root does it have
	and what the values of the roots are if it have any.
	"""
	print("Hello, this is stanCode Quadratic Solver!")
	a = int(input("please enter an integer for value a: "))
	b = int(input("please enter an integer for value b: "))
	c = int(input("please enter an integer for value c: "))
	x = b*b - 4*a*c														# 把判別式的值丟給變數x
	if x > 0:  															# 判別式大於零
		y = math.sqrt(x)
		first_root = (-1*b + y)/(2*a)
		second_root = (-1*b - y)/(2*a)
		print("Two roots: " + str(first_root) + "," + str(second_root))
	elif x == 0:  														# 判別式等於零
		root = (-1*b)/(2*a)												# 只有一根
		print("One root: " + str(root))
	else:  																# 判別式小於零
		print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
