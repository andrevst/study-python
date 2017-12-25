def read_text():

    quotes = open("/Users/andretonelli/projects/fullstackUdacity/study-python/shit_text.txt")
    content = quotes.read()
    print(content)
    quotes.close()

read_text()
