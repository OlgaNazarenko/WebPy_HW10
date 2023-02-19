import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')

import django
django.setup()

from pymongo import MongoClient
from django.db import models


from quoteapp.models import Tag, Author, Quote
from quotes import settings


# mongodb+srv://goitlearn:Seoul@cluster0.aksl02l.mongodb.net/test
client = MongoClient("mongodb+srv://goitlearn:Seoul@cluster0.aksl02l.mongodb.net/test")
db = client['mydatabase']

tags = db['tags']
mongo_data = list(tags.find())

for data in mongo_data:
    try:
        tag = Tag(name=data['name'])
        tag.save()
    except Exception as e:
        print(f'An error occurred: {e}')


quotes = db['quotes']
mongo_data = list(quotes.find())

for data in mongo_data:
    try:
        quote = Quote(
            quote=data['quote'],
            author=data['author'],
            tags=data['tags']
        )
        quote.save()
    except Exception as e:
        print(f'An error occurred: {e}')


authors = db['authors']
mongo_data = list(authors.find())

for data in mongo_data:
    try:
        author = Author(
            fullname=data['fullname'],
            born_date=data['born_date'],
            born_location=data['born_location'],
            description=data['description'],
            about=data['about']
        )
        author.save()
    except Exception as e:
        print(f'An error occurred: {e}')


