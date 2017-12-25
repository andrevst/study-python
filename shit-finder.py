import urllib

def read_text():

    quotes = open("/Users/andretonelli/projects/fullstackUdacity/study-python/shit_text.txt")
    content = quotes.read()
    quotes.close()
    check_shit(content)

def check_shit(content):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + content)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Idiot, you wrote a shit.")
    elif "false" in output:
        print("No shit here.")
    else:
        print("Where is my file?")

read_text()
