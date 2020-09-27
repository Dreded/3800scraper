from bs4 import BeautifulSoup

import os
scriptPath = os.path.dirname(os.path.abspath(__file__))
print(scriptPath)

store_name = "The Test Store"


def get_stock():
    page = ""
    with open(scriptPath + "\\test_store.html",'r',encoding='utf-8') as f:
        page = f.read()
    #pass the HTML to Beautifulsoup.
    soup = BeautifulSoup(page,'html.parser')

    main_table = soup.find("div",attrs={'class':'item-cells-wrap'})
    cards = main_table.find_all("div", class_="item-container")
    store = {
        'store_name': store_name,
        'has_stock': False,
        'nostock':[],
        'stock':[],
    }
    for card in cards: 
        description = card.find("a", class_="item-title").text
        url = card.find("a", class_="item-title")['href']
        status = card.find("div", class_="item-button-area").text
        if "3080" in description:
            record = {
                'description':description,
                'url':url
            }
            if "Add" in status:
                store['has_stock'] = True
                store['stock'].append(record)
            else:
                store['nostock'].append(record)
    return store

def printIt(stock):
    print('\nStore: ',stock['store_name'])
    if stock['has_stock']:
        print('THEY HAVE STOCK!!!!!')
    else: print('No Stock!')
    print('\nHas no stock of...\tTotal Items: ',len(stock['nostock']))
    for key in stock['nostock']:
        print("{}: {}".format(key['description'],key['url']))
    if stock['has_stock']:
        print('\nHas Stock of...\tTotal Items: ',len(stock['stock']))
        for key in stock['stock']:
            print("{}: {}".format(key['description'],key['url']))


if __name__ == '__main__':
    stock = get_stock()
    printIt(stock)
