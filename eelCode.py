import eel
import datetime

eel.init("web")

itemsnames = ['cola', 'banana', 'tomato', 'cucambre',
              'carrot', 'falafel', 'tormos', 'homus', 'cola', 'banana', 'tomato', 'cucambre',
              'carrot', 'falafel', 'tormos', 'homus', 'cola', 'banana', 'tomato', 'cucambre',
              'carrot', 'falafel', 'tormos', 'homus', 'cola', 'banana', 'tomato', 'cucambre',
              'carrot', 'falafel', 'tormos', 'homus']
itemPrices = [11, 22, 54, 63, 12, 25, 10, 12.90, 11, 22, 54, 63, 12, 25, 10,
              12.90, 11, 22, 54, 63, 12, 25, 10, 12.90, 11, 22, 54, 63, 12, 25, 10, 12.90]
itemtotal = [22, 55, 66, 99, 77, 55, 10, 12.90, 11, 22, 54, 63, 12, 25, 10,
             12.90, 11, 22, 54, 63, 12, 25, 10, 12.90, 11, 22, 54, 63, 12, 25, 10, 12.90]


@eel.expose
def send_data():
    global itemsnames, itemPrices, itemtotal
    eel.recieve2(itemsnames, itemPrices, itemtotal)


@eel.expose
def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


eel.start("index.html")
