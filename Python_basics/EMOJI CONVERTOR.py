message = input(">")
words = message.split(" ")

emojis = {
    ":)": "😁",
    ":(": "😢"
}

for word in words:
    if(emojis.get(word, "error")!= "error"):
        print(emojis[word])