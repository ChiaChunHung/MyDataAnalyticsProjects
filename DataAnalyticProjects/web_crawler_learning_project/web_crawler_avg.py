"""
File: web_crawler_avg.py
Name: Chia-Chun Hung
--------------------------
This file demonstrates how to get
averages score of 250 movies
on www.imdb.com/chart/top
"""

import requests
from bs4 import BeautifulSoup


def main():
	url = 'http://www.imdb.com/chart/top'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}
	response = requests.get(url, headers=header)
	html = response.text
	soup = BeautifulSoup(html)
	tags = soup.find_all('span', {'class': 'ipc-rating-star--rating'})
	# 小心因為網頁又改版了，現在不把評分放在上課的那個位置，故改用下方方法去做
	total = 0
	for tag in tags:
		total += float(tag.text)
	print(total/25)

	# 原始網頁還為改版前，評分是放在tag中的'aria-label'那一個key-value pair
	# total = 0
	# for tag in tags:
	# 	total += float(tag['aria-label'][13:16])
	# print(total/25)


if __name__ == '__main__':
	main()
