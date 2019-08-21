from django.contrib import admin
from .models import Article     # 명시적 상대경로 표현
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # 튜플이나 리스트로 작성. 주로 튜플
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    list_filter = ('created_at',) # 하나인 튜플은 항상 뒤에 콤마(,)가 있어야 튜플임.
    list_display_links = ('content',)
    list_editable = ('title',)
    list_per_page = 2 # 기본값 = 100

admin.site.register(Article, ArticleAdmin)