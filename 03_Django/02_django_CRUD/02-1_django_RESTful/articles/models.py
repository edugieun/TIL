from django.urls import reverse
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        # return reverse('articles:detail', args=[self.pk]) # 리턴값이 문자열로 나옴.
        return reverse('articles:detail', kwargs={'pk':self.pk}) # 마찬가지로 리턴값이 문자열로 나옴.
        # 주의사항
        # reverse 함수에 args 랑 kwargs를 동시에 인자로 보낼 수 없다.

