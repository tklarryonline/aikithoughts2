from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.fields import TextField
from markdownx.widgets import AdminMarkdownxWidget

from .models import Post


class PostModelAdmin(ModelAdmin):
    formfield_overrides = {
        TextField: {
            'widget': AdminMarkdownxWidget
        },
    }


admin.site.register(Post, admin_class=PostModelAdmin)
