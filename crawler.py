import requests
from bs4 import BeautifulSoup


def laptop_crawler(max_pages):
	
	page = 1
	
	#This loop will allow you to crawl till the page you want. 
	while page <= max_pages:

		url = 'https://www.flipkart.com/search?q=laptop&marketplace=FLIPKART&otracker=start&as-show=on&as=off&page=' + str(max_pages)

		source_code = requests.get(url)								#Gets data from the url.
		only_text = source_code.text 								#Gets text from the data.
		soup = BeautifulSoup(only_text)								#Helps dealing with html content

		#Finds link and the title of laptops and prints them.
		for link in soup.findAll('a', {'class': '_31qSD5'}):
			href = 'https://www.flipkart.com' + link.get('href')
			print(href)
			print("\n")
			l = soup.find('div', {"class": "_3wU53n"})
			title = l.text
			print(title)
			print("\n")
			get_specifications(url)
			print("\n")
			print("\n")

		page += 1

def get_specifications(url):
	source_code = requests.get(url)
	only_text = source_code.text
	soup = BeautifulSoup(only_text)

	for sp in soup.findAll('li', {'class': 'tVe95H'}):
		print("--" + sp.string) 

laptop_crawler(1)	
