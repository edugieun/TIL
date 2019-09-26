from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at', 'article_id',)

admin.site.register(Comment, CommentAdmin)

# decoration 하면 'admin.site.register' 없이 아래와 같이 할 수 있다.
# @admin.register(Comment)
# class CommentAdmin(admin,ModelAdmin):
#     list_display = ('pk', 'content', 'created_at', 'updated_at', 'article_id',)