import requests
from requests import Response
from bs4 import BeautifulSoup


def download():
    URL = "https://pl.wikiquote.org/wiki/Przys%C5%82owia_polskie"
    page = requests.get(URL)
    return page

def scrape(page: Response):
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("div", class_="mw-parser-output")
    all_items = result.select('ul > li:not(li li)')
    proverb_list = []
    for item in all_items:
        saying = item.text.split('.\n')[0]  # proverb
        proverb_list.append(saying)
    return proverb_list

def save(list_to_save: list):
    with open('przyslowia.txt', 'w', encoding='utf-8') as file:
        for item in list_to_save:
            file.write(str(item) + '\n')
def read():
    with open('przyslowia.txt', 'r', encoding='utf-8') as file:
        # Read the contents of the file as a list of lines
        lines = file.readlines()
    proverb_list = [saying.replace('\n', '') for saying in lines]
    return proverb_list

def main():
    # page = download()
    # proverb_list = scrape(page)
    # save(proverb_list)
    proverb_list = read()
    print(len(proverb_list))
    # max = 974 # od 0
    index = 153

    print(proverb_list[index])

if __name__ == '__main__':
    main()



