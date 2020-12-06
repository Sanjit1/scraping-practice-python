import requests
import json
from bs4 import BeautifulSoup, NavigableString

home_page_url = "http://books.toscrape.com/index.html"
home_page_request = requests.get(home_page_url)
home_page_soup = BeautifulSoup(home_page_request.content, 'html.parser')
book_list = home_page_soup.find_all('ol', class_='row')[0].children;