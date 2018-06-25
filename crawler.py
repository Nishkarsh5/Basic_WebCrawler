import requests
from bs4 import BeautifulSoup


def laptop_crawler(max_pages):
	
	page = 1
	
	while page <= max_pages:

		url = 'https://www.flipkart.com/search?q=laptop&marketplace=FLIPKART&otracker=start&as-show=on&as=off&page=' + str(max_pages)

		source_code = requests.get(url)
		only_text = source_code.text
		soup = BeautifulSoup(only_text)

		for link in soup.findAll('a', {'class': '_31qSD5'}):
			href = 'https://www.flipkart.com' + link.get('href')
			print(href)
			l = soup.find('div', {"class": "_3wU53n"})
			title = l.text
			print(title)
			print("\n")

		page += 1


laptop_crawler(1)	