import urllib.request
from bs4 import BeautifulSoup


store_name = "New Egg Canada"


url = "https://www.newegg.ca/GeForce-RTX-3080-3090/EventSaleStore/ID-10492"

#download the URL and extract the content to the variable html 
request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()

#pass the HTML to Beautifulsoup.
soup = BeautifulSoup(html,'html.parser')

main_table = soup.find("div",attrs={'class':'item-cells-wrap'})
cards = main_table.find_all("div", class_="item-container")

def get_stock():
    store = {}
    for card in cards: 
        title = card.find("a", class_="item-title").text
        url = card.find("a", class_="item-title")['href']
        status = card.find("p", class_="item-promo").text
        if "3080" in title:
            record = {
                'title':title,
                'url':url
            }
            if "OUT" in status:
                no_stock.append(record)
            else:
                stock.append(record)
    return ''
    #return (stock, no_stock, store_name)

def printIt(stock):
    print('Total Cards In Stock: ',len(stock))
    for item in stock:
        print("\n")
        for key in item:
            print('{} : {}'.format(key,item[key]))


if __name__ == '__main__':
    stock = get_stock()
    printIt(stock[0])
    printIt(stock[1])

