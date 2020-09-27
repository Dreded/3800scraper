import urllib.request
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

store_name = "B&H Photo/Video"


store_url = "https://www.bhphotovideo.com/c/products/Graphic-Cards/ci/6567/N/3668461602?filters=fct_nvidia-geforce-series_5011%3Ageforce-rtx-3080"


def get_stock():
    #download the URL and extract the content to the variable html 
    request = urllib.request.Request(store_url,headers=headers)
    html = urllib.request.urlopen(request).read()

    #pass the HTML to Beautifulsoup.
    soup = BeautifulSoup(html,'html.parser')
    main_table = soup.find("div",attrs={'data-selenium':'listingProductDetailSection'})
    cards = main_table.find_all("div",attrs={'data-selenium':'miniProductPageProduct'})
    baseurl = 'https://www.bhphotovideo.com'
    store = {
        'store_name': store_name,
        'has_stock': False,
        'nostock':[],
        'stock':[],
    }
    for card in cards: 
        description = card.find("span", attrs={'data-selenium':'miniProductPageProductName'}).text
        url = card.find("a", attrs={'data-selenium':'miniProductPageProductNameLink'})['href']
        status = card.find("button", attrs={'data-selenium':'addToCartButton'})
        if status:
            status = status.text
        else: status = 'No Stock'
        if "3080" in description:
            record = {
                'description':description,
                'url': baseurl + url
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
