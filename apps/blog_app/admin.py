from django.contrib import admin
from .models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    '''
        Admin View for Post
    '''
    readonly_fields = ('created', 'updated')

class CategoryAdmin(admin.ModelAdmin):
    '''
        Admin View for Category
    '''
    readonly_fields = ('created', 'updated')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
    