import webbrowser

def search_antonyms(word):
    query = f"antonyms of {word}"
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
