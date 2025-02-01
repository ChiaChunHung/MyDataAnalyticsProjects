"""
File: web_crawler.py
Name: Chia-Chun Hung
--------------------------
This file demonstrates how to bypass IMDb’s anti-scraping mechanisms
to extract data from the website. After successfully retrieving the data,
we process and sort it to determine which year had the highest number of movie releases.
"""

import requests  # 引入此套件，來讓pycharm可以連上網路
from bs4 import BeautifulSoup
# bs4中的一個物件BeautifulSoup->幫我們把正個HTML變成一個物件，讓我們比較好找到目標


def main():
	url = 'http://www.imdb.com/chart/top'  # 網址的專有名詞叫url

	# 網站瀏覽時，他的HTML中會有很多header，每個header都是一個dictionary，找到存瀏覽者身份資料的那個dictionary
	# 並拿此去更改.get()這一絕招中的key word arg，就可以讓pycharm騙過網站，讓他們以為我是網站瀏覽者不是pycharm，進而允許我存取他們的資料
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}

	response = requests.get(url, headers=header)
	# request套件中有.get()絕招，會到給定的url去把抓到的東西做成物件並回傳
	# 把.get()中的key word arg headers 這個眾多header都改成header，
	# 這樣一來，當pycharm去access該網站的資料時，就可以讓網站以為我是正常使用者進入他的網站，並讓我得以存取他的資料

	print(response)  # 物件可以print，會得到def __str__(self)設定的內容
	# <Response[200] > 代表存取資料成功
	# <Response [403]> 代表拒絕存取
	# <Response [200]> 代表Not found

	html = response.text
	soup = BeautifulSoup(html)
	tags = soup.find_all('div', {'class': 'sc-ad5a2436-6 hppGke cli-title-metadata'})
	d = {}
	for tag in tags:
		year = tag.text[:4]
		if year not in d:
			d[year] = 1
		else:
			d[year] += 1
	# 接者我們想得到按造上檔次數由小到大的排序，但因dict這個DS沒有資料結構，故須先用.items()把他轉成list of tuple
	# 在透由sorted去排序此list of tuple，最中把排好的結果由for loop印出
	for year, occurrence in sorted(d.items(), key=lambda t: t[1]):
		# sorted這個function必須先知道每筆資料要用哪一個東西作為排序值來排序
		# 若沒有改，則預設是每筆資料的先碰到者為排序值
		# 所以default的key=接的可能是一個針對每個元素取第一個位置者做排序值的函數
		print(year, '->', occurrence)







if __name__ == '__main__':
	main()
