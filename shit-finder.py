import urllib

def read_text():

    quotes = open("/Users/andretonelli/projects/fullstackUdacity/study-python/shit_text.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    check_shit(content)

def check_shit(content):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + content)
    output = connection.read()
    print(output)
    connection.close()

read_text()
