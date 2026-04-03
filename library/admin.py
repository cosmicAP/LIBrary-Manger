from django.contrib import admin
from .models import book , Students , borrowed_records

admin.site.register(book)
admin.site.register(Students)
admin.site.register(borrowed_records)