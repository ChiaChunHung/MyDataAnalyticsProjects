"""
File: extension1_factioral.py
Name: Tony
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	After asking user to enter a number, the program will ask user
	to enter an number and calculate the factorial result of that number,
	then printing the result on console.
	"""
	print("Welcome to stanCode factorial master!")
	# 引言，告訴使用者這個程式是啥
	while True:
		number = int(input("Give me a number, and I will list the answer of factorial: "))
		if number == EXIT:  					# 若輸入值是EXIT，那就直接離開並印出SeeYA
			break
		else:
			count_from = 1  					# 從1開始乘
			base = number  						# 把number丟到不同箱子，等等可以讓該箱子做裝乘積的箱子並保留number箱子去做“乘到number就停止”的煞車條件
			while True:							# 此回圈幫我把"1"乘到"使用者輸入的值"
				if count_from == number:  		# 使用者輸入值(number)當作乘到該數字就代表階層執行完畢的條件。
					break
				else:
					base = base * count_from 	# base當作裝載乘積的箱子
					count_from += 1  			# 從1開始乘，每乘完一次就加1，直到乘到"使用者輸入的值-1"為止
			print("Answer: " + str(base))		# 印出階層的結果
	print("------------- See ya! -------------")



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()