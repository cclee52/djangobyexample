from django.contrib import admin

from .models import Post


# superuser: admin
# password : admin123456
# Register your models here.

# admin.site.register(Post)
# next code replace prevoius this
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # open page to find author after select pass ID of author
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')