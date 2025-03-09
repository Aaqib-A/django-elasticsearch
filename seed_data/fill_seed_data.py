import os
import sys
import django
import json

# Add the Django project's root directory to sys.path
sys.path.append("../django_elasticsearch")

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_elasticsearch.settings")
django.setup()

from book.models import Book


def open_file(file_name: str):
    with open(file_name, encoding="utf-8") as file:
        data = file.read()
    data = json.loads(data)
    return data


def insert_seed_data():
    file_name = "books.json"
    books = open_file(file_name=file_name)

    for each_book in books:
        # Change the key to match the db
        each_book["image_link"] = each_book.pop("imageLink")

        # Insert into the database
        Book.objects.create(**each_book)

    print("Seed data inserted into the database")


insert_seed_data()
