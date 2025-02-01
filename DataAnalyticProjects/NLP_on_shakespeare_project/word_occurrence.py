"""
File: word_occurrence.py
Name: Chia-Chun Hung
------------------------------
This project applies Natural Language Processing (NLP) and Data Analytics
to explore word frequency trends in Romeo & Juliet, one of Shakespeare’s most famous plays.
Using Python, I process and analyze the text to identify the most frequently used words.
"""


# The file name of our target text file
FILE = 'romeojuliet.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


# 此program測試對象的：讀檔、list、字串處理、token、dict、python comprehension、python lambda function
def main():
	word_d = {}										# 先開空的dictionary
	with open(FILE, 'r') as f:						# 讀檔，把羅密歐那份txt文字檔讀到RAM上
		for line in f:								# 把每行字叫出來assign給line變數
			tokens = line.split()					# 利用字串內建的絕招.split()來做tokenization，再存入tokens變數箱
			for token in tokens:					# 對list做for each loop，每圈會丟一格櫃子中的"元素"出來(！不是丟櫃子)
				token = string_manipulation(token)  # 故需資料前處理。用string_manipulation()把每個元素中夾雜的標點符號拿掉以及大小寫一致化
				if token not in word_d:				# 先確認該字有沒有在word_d這個字典中。若沒有確認，有可能會讓該字對應的出現次數恆是1
					word_d[token] = 1				# 進入此區，代表該字沒有出現在字典中過，所以該字是第一次作為字卡被存入，此時他出現一次
				else:								# 進入此區，代表該字出現過，故等等要加字卡背後存的內容(他出現的次數)更新
					word_d[token] += 1				# 左邊寫法等於右邊這個寫法-> word_d[token] = word_d[token] + 1
		print_out_d(word_d)


def print_out_d(d):
	"""
	: param d: (dict) key of type str is a word
					value of type int is the word occurrence
	---------------------------------------------------------------
	This function prints out all the info in d
	"""
	for word, occurrence in sorted(d.items(), key=lambda t: t[1]):
		print(word, '->', occurrence)


def string_manipulation(token):					# 此函數在把資料去除標點符號＆把大小寫一致化。因字串不可直接更改，只能重串，故這裏用到SC001概念
	ans = ''									# 先做空竹籤
	for ch in token:							# loop over舊的字串
		if ch.isdigit() or ch.isalpha():		# 判斷：當data type是字串的數字或是字母時，就是目標對象，要串入新的竹籤
			ans += ch.lower()					# 目標對象串上新竹籤
	return ans									# 因為user端那邊有接，故要return


if __name__ == '__main__':
	main()
