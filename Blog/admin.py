from django.contrib import admin
from .models import Author,Tag,Post
# Register your models here.

class Postadmin(admin.ModelAdmin):
    list_filter=("author","caption","date",)
    list_display=("title","date","author",)
    prepopulated_fields={"slug":("title",)}


admin.site.register(Post,Postadmin)
admin.site.register(Author)
admin.site.register(Tag)

