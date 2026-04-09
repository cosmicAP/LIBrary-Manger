from django.contrib import admin
from .models import Book , Students , BorrowedRecords

admin.site.register(Book)
admin.site.register(Students)
admin.site.register(BorrowedRecords)