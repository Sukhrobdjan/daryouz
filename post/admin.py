from django.contrib import admin

# Register your models here.
from .models import Post,Category,Link


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Category, CategoryAdmin)
admin.site.register(Link)
