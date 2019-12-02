from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 튜플 값이 하나일 경우 뒤에 ,(쉼표) 가 있어야 한다.
        ordering = ('-pk',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'article_pk': self.pk})

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 아래와 같이 순서를 models에 초기 설정 할 수 있음.
        ordering = ['-pk']

    # 객체 표현
    def __str__(self):
        # return self.content
        return self.content