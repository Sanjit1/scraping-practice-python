import requests
import json
from bs4 import BeautifulSoup, NavigableString

home_page_url = "http://books.toscrape.com/index.html"
home_page_request = requests.get(home_page_url)
home_page_soup = BeautifulSoup(home_page_request.content, 'html.parser')
book_element_list = home_page_soup.find_all('ol', class_='row')[0].children;
book_object_list = []
for book_element in book_element_list:
    if isinstance(book_element, NavigableString):
        continue
    else:
        book_object_list.append({
            'title': list(book_element.find_all("h3")[0].children)[0]["title"], 
            'url': "http://books.toscrape.com/" + list(book_element.find_all("h3")[0].children)[0]["href"],
            'price': book_element.find_all("p", class_="price_color")[0].getText(),
            'rating': book_element.find_all("p", class_="star-rating")[0]['class'][1] + " Stars"
        })


for book in book_object_list:
    print(book)

with open("books.json", 'w') as books_file:
    json.dump(book_object_list, books_file)