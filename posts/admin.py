from django.contrib import admin
from .models import *


# Register your models here. 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)   

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date')
    list_filter = ('category','date',)
    list_editable = ('category', )
    search_fields = ('title', 'author', 'category', 'date')   

admin.site.register(Post, PostAdmin)



