from django.contrib import admin

from .models import category, post,Author
from .models import blogComment

# Register your models here.
admin.site.register((category,Author,blogComment))

@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js=('tinymce.js')



