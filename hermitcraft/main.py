import json
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')

headless_browser = webdriver.Chrome(options=options)
home_page_url = "https://hermitcraft.com/"
home_page_request = headless_browser.get(home_page_url)
hermits_list_element = headless_browser.find_elements_by_class_name('list-group')[0].find_elements_by_tag_name("li");
hermits_list = []
for hermit_element in hermits_list_element:
    hermit_tag = hermit_element.find_elements_by_tag_name('a')[0]
    hermits_list.append({
        "name": hermit_tag.get_attribute('innerHTML').split(">")[1],
        "image": hermit_tag.find_element_by_tag_name("img").get_attribute('src')
    })

print(hermits_list)

with open("hermits.json", 'w', encoding='utf-8') as hermits_file:
    json.dump(hermits_list, hermits_file, ensure_ascii=False, indent=4)