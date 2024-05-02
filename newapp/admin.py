from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'categoryType', 'postCategory')
    list_filter = ('postCategory',)
    search_fields = ('title', 'dateCreation')


class PostTranslationAdmin(TranslationAdmin):
    model = Post

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)

