from django.contrib import admin
from rango.models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  # Fields to display in the list view
    list_filter = ('category',)  # adding a filter option by category
    search_fields = ('title', 'url')  # allowing searching by title and URL

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin) 
admin.site.register(UserProfile)