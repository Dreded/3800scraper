store_name = "Test Store"


def get_stock():
    store = {
        'store_name': store_name,
        'has_stock': True,
        'nostock': [{'description': 'GeForce RTX 3080 Ventus OC 10GB PCI-E w/ HDMI, Triple DP', 'url': 'https://www.memoryexpress.com/Products/MX00113956'}, {'description': 'GeForce RTX 3080 XC3 ULTRA GAMING 10GB PCI-E w/ HDMI, Triple DP', 'url': 'https://www.memoryexpress.com/Products/MX00113972'}, {'description': 'GeForce RTX™ 3080 Gaming OC 10GB Triple Fan  PCI-E 4.0 w/ Triple DP, Dual HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00113954'}, {'description': 'GeForce RTX™ 3080 Eagle OC 10GB Triple Fan  PCI-E 4.0 w/ Triple DP, Dual HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00113955'}, {'description': 'GeForce RTX 3080 Gaming X Trio 10GB PCI-E w/ HDMI, Triple DP', 'url': 'https://www.memoryexpress.com/Products/MX00113957'}, {'description': 'GeForce RTX™ 3080 FTW3 Ultra Gaming  10GB Triple Fan  PCI-E 4.0 w/ Triple DP, HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00114024'}, {'description': 'GeForce RTX™ 3080 TUF 10G Gaming Triple Fan  PCI-E 4.0 w/ Triple DP, Dual HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00114004'}, {'description': 'GeForce RTX™ 3080 TUF O10G Gaming Triple Fan  PCI-E 4.0 w/ Triple DP, Dual HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00114003'}, {'description': 'GeForce RTX™ 3080 XC3 Black Gaming  10GB ICX3 Triple Fan  PCI-E 4.0 w/ Triple DP, HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00114094'}, {'description': 'GeForce RTX™ 3080 XC3 Gaming 10GB ICX3 Triple Fan  PCI-E 4.0 w/ Triple DP, HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00114095'}, {'description': 'ROG STRIX GeForce RTX 3080 O10G Gaming 10GB PCI-E w/ Dual HDMI, Triple DP', 'url': 'https://www.memoryexpress.com/Products/MX00114092'}],
        'stock': [{'description': 'GeForce RTX 3080 Ventus OC 10GB PCI-E w/ HDMI, Triple DP', 'url': 'https://www.memoryexpress.com/Products/MX00113956'}, {'description': 'GeForce RTX 3080 XC3 ULTRA GAMING 10GB PCI-E w/ HDMI, Triple DP', 'url': 'https://www.memoryexpress.com/Products/MX00113972'}, {'description': 'GeForce RTX™ 3080 Gaming OC 10GB Triple Fan  PCI-E 4.0 w/ Triple DP, Dual HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00113954'}, {'description': 'GeForce RTX™ 3080 Eagle OC 10GB Triple Fan  PCI-E 4.0 w/ Triple DP, Dual HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00113955'}, {'description': 'GeForce RTX 3080 Gaming X Trio 10GB PCI-E w/ HDMI, Triple DP', 'url': 'https://www.memoryexpress.com/Products/MX00113957'}, {'description': 'GeForce RTX™ 3080 FTW3 Ultra Gaming  10GB Triple Fan  PCI-E 4.0 w/ Triple DP, HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00114024'}, {'description': 'GeForce RTX™ 3080 TUF 10G Gaming Triple Fan  PCI-E 4.0 w/ Triple DP, Dual HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00114004'}, {'description': 'GeForce RTX™ 3080 TUF O10G Gaming Triple Fan  PCI-E 4.0 w/ Triple DP, Dual HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00114003'}, {'description': 'GeForce RTX™ 3080 XC3 Black Gaming  10GB ICX3 Triple Fan  PCI-E 4.0 w/ Triple DP, HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00114094'}, {'description': 'GeForce RTX™ 3080 XC3 Gaming 10GB ICX3 Triple Fan  PCI-E 4.0 w/ Triple DP, HDMI', 'url': 'https://www.memoryexpress.com/Products/MX00114095'}, {'description': 'ROG STRIX GeForce RTX 3080 O10G Gaming 10GB PCI-E w/ Dual HDMI, Triple DP', 'url': 'https://www.memoryexpress.com/Products/MX00114092'}],
    }
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
