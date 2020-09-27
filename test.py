import multiprocessing
import glob
import time
start_time = time.time()

stores = {}
_pool = None

def process_plugin(plugin):
    get_stock = __import__(plugin[2:-3].replace('\\','.'), fromlist=[None]).get_stock
    return get_stock()

def index():

    plugins = glob.glob('./store_plugins/store_*.py')
    output = _pool.map(process_plugin, plugins)
    for i,plugin in enumerate(plugins):
        #stores[plugin[22:-3]] = process_plugin(plugin)
        stores[plugin[22:-3]] = output[i]

    context = {
        'title': '3080 Stock Tracker',
        'stores': stores,
    }
    return context
if __name__ == '__main__':
    _pool = multiprocessing.Pool()
    print(index())
    print("--- %s seconds ---" % (time.time() - start_time))
    _pool.close()
    _pool.join()