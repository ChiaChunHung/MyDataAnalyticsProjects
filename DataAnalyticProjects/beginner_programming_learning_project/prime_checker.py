"""
File: prime_checker.py
Name:
Time Spent: 49 min (not include note)
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	After asking user to enter a number, this program will
	identify whether the number is a prime number.
	"""
	print("Welcome to the prime checker!")  			# 引言，告訴使用者這個程式是啥
	while True:
		number = int(input("n: "))
		if number == EXIT:  							# 若使用者輸入-100，就可以直接離開此回圈
			break
		divisor = 2  									# 初始的除數一定為2，因為要看"2"~"使用者輸入的數值-1"之間是否有可以把使用者輸入的數值整除的數
		while True:										# 此回圈會從2開始找到使用者輸入的數字-1為止，看有沒有人是使用者輸入值的因數
			if number % divisor != 0:  					# 若2還無法把被除數除盡，那就往下找有沒有其他數字可以除盡
				divisor += 1
			elif divisor == number:  					# 代表找完2~使用者輸入值-1之間的數了，但都沒有任何因數，所以自己是質數。
				print(str(number) + " is a prime number.")
				break  									# 判斷不是質數後，就該離開回圈，否則會一直拿同一個數做出相同判斷並一直印出不是質數。
			else:  										# 此區間代表有比自己小但大於等於2的整數可以整除自己，所以自己非質數。
				print(str(number) + " is not a prime number.")
				break  									# 判斷是質數後，就該離開回圈，否則會一直拿同一個數做出相同判斷並一直印出是質數。
	print("Have a good one!")




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
