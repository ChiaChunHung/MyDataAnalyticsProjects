"""
File: weather_master.py
Name: Tony
Time Spent: 1 hr 30 min (include note)
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

EXIT = -1


def main():
	"""
	This program asks users to enter temperature data,
	and it will then indicate the highest and the lowest temperature;
	the average temperature; and how many days had temperature lower than 16 degree,
	days that we call them cold days.
	"""
	print('stanCode "Weather Master 4.0"!')												# 若要讓雙引號在雙引號刮住的範圍中顯現出來，還可以用 \" 此寫法
	degree = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
	if degree == EXIT:  																# 代表使用者一開始就來亂
		print("No temperatures were entered.")
	else:  																				# 代表使用者輸入了有意義的數字，可以開始判斷了
		maximum = degree  																# 第一筆進入值 先坐上最大值的寶座
		minimum = degree  																# 第一筆進入值 也同時先坐上最小值的寶座
		average_need_sum = degree  														# 第一筆進入值 也丟到樣本總和的箱子中
		average_need_number = 1  														# 進入此區間代表第一筆進入值有意義，屬於樣本，故樣本數量此時為1
		cold_days = 0  																	# cold_days一定要先有數字才能加，故先設0
		if degree < 16:  																# 第一筆起始值若非EXIT值，也算在資料樣本中，要幫我看是不是低於16度
			cold_days += 1																# 是了話就在cold_days上+1
		while True:
			degree = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))  	# 跟使用者要第二筆數值
			if degree == EXIT:  														# 回圈的開關
				break
			average_need_sum = average_need_sum + degree  								# 第二筆值開始，若非EXIT值，則算是樣本，故可以在樣本總和的箱子加入該值
			average_need_number += 1  													# 第二筆值開始，若非EXIT值，則算是樣本，故可以在樣本數量的箱子+1個數量
			if degree < 16:  															# 第二筆值開始，若非EXIT值，都要幫我判斷是不是低於16度
				cold_days += 1															# 是了話就在cold_days上+1
			if degree >= maximum:  														# 第二筆值開始，誰比較大，就誰上最大值寶座
				maximum = degree
			elif degree < minimum:  													# 第二筆值開始，誰比較小，就誰上最小值寶座
				minimum = degree
		print("Highest temperature = " + str(maximum))  								# 印出最大值
		print("Lowest temperature = " + str(minimum))  									# 印出最小值
		average = average_need_sum / average_need_number  								# 把平均數算出來丟到名叫平均數的箱子
		print("Average = " + str(average))  											# 印出平均數
		print(str(cold_days) + " cold day(s)") 											# 印出多少個低於16度的冷天



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
