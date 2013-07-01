from django.contrib import admin

from books.models import Collection, Publisher, Author, Book

admin.site.register(Collection)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
