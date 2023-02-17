import json


def retrieve_tags():
    tags = []

    with open('data/quotes.json', 'r') as file:
        quotes = json.load(file)

        if quote in quotes:
            if tag in quote['tags']:
                tags.append(tag)

    return tags


def retrieve_author():
    with open('data/authors.json', 'r') as file:
        authors = json.load(file)

    return authors

def retrieve_quote():
    with open('open/quotes.json', 'r') as file:
        quotes = json.load(file)

    return quotes
