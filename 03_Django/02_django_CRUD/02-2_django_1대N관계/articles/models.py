from django.urls import reverse
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #객체 표현: 이 객체, 인스턴스가 불렸을 때 어떻게 보여질까, 출력될까를 설정.
    def __str__(self):
        return self.title
        

    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        # return reverse('articles:detail', args=[self.pk]) # 리턴값이 문자열로 나옴.
        return reverse('articles:detail', kwargs={'article_pk':self.pk}) # 마찬가지로 리턴값이 문자열로 나옴.
        # 주의사항
        # reverse 함수에 args 랑 kwargs를 동시에 인자로 보낼 수 없다.


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 아래와 같이 순서를 models에 초기 설정 할 수 있음.
        ordering = ['-pk']

    # 객체 표현
    def __str__(self):
        # return self.content
        return f'<Article({self.article_id}): Comment({self.pk})-{self.content}'