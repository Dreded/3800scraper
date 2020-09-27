import urllib.request
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
store_name = "New Egg Canada"


store_url = "https://www.newegg.ca/GeForce-RTX-3080-3090/EventSaleStore/ID-10492"



def get_stock():
    #download the URL and extract the content to the variable html 
    request = urllib.request.Request(store_url,headers=headers)
    html = urllib.request.urlopen(request).read()

    #pass the HTML to Beautifulsoup.
    soup = BeautifulSoup(html,'html.parser')

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
