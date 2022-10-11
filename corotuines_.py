def searcher():
    import  time
    book = "This is example of code with harry tutorial by aklesh kumar (Akki Raj)"
    time.sleep(2)

    while True:
        text= (yield )
        if text in book:
            print("Text in the book")
        else:
            print("Text is not present in the book")

search = searcher()
print("Search started")
next(search)
search.send("Akki")
print("Press any key..")
search.send("Aklesh")
print("Press any key..")
search.send("isd thia")
print("Press any key..")
search.send("klsa")
print("Press any key..")
search.close()
