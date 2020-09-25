import urllib.request
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
store_name = "Memory Express"


url = "https://www.memoryexpress.com/Category/VideoCards?FilterID=0c630011-395b-1ec2-cceb-96794781ab87"

#download the URL and extract the content to the variable html 
request = urllib.request.Request(url,headers=headers)
html = urllib.request.urlopen(request).read()

#pass the HTML to Beautifulsoup.
soup = BeautifulSoup(html,'html.parser')
main_table = soup.find("div",attrs={'data-role':'product-list-container'})
cards = main_table.find_all("div",attrs={'class':'c-shca-icon-item'})

def get_stock():
    baseurl = 'https://www.memoryexpress.com'
    store = {
        'store_name': store_name,
        'has_stock': False,
        'nostock':[],
        'stock':[],
    }
    for card in cards: 
        description = card.find("div", attrs={'class':'c-shca-icon-item__body-name'}).text.strip()
        url = card.find("div", attrs={'class':'c-shca-icon-item__body-name'}).a['href']
        status = card.find("div", attrs={'class':'c-shca-icon-item__body-extras'}).text
        
        if "3080" in description:
            record = {
                'description':description,
                'url': baseurl + url
            }
            if "Backorder" in status:
                store['nostock'].append(record)
            else:
                store['has_stock'] = True
                store['stock'].append(record)
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
