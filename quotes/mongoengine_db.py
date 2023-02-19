import configparser
import os
from pathlib import Path

from mongoengine import connect
from mongoengine import Document, StringField, ListField, ReferenceField,DateTimeField, EmbeddedDocument


path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR , '../config.ini')

config = configparser.ConfigParser()
config.read('config.ini')

m_user = config.get('DB', 'user')
m_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

conn = connect(host = f"mongodb+srv://{m_user}:{m_pass}@{domain}/{db_name}?retryWrites=true&w=majority")

class Tag(Document):
    name = StringField(max_length=25,required=True)

class Author(Document):
    fullname = StringField(max_length=100, required=True)
    born_date = DateTimeField()
    born_location = StringField(max_length=100, required=True)
    description = StringField(max_length=5000, required=True)
    about = StringField()


class Quote(Document):
    quote = StringField(max_length=2500, required=True)
    author = ReferenceField(Author)
    tags = ListField(Tag)


mongo_data = Tag.objects.all()

for item in mongo_data:
    django_model_tag = Tag(
        name = item.name
    )
    django_model_tag.save()


mongo_data = Author.objects.all()

for item in mongo_data:
    django_model_author = Author(
        fullname = item.fullname,
        born_date=item.born_date,
        born_location = item.born_location,
        description = item.description,
        about = item.about,
    )

    django_model_author.save()


mongo_data = Quote.objects.all()

for item in mongo_data:
    django_model_quote = Quote(
        quote = item.quote,
        author = item.author,
        tags = item.tags,
    )

    django_model_quote.save()