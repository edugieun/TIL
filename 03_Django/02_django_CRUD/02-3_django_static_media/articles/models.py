from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail
from django.urls import reverse
from django.db import models

def articles_image_path(instance, filename):
    return f'articles/{instance.pk}/images/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True)
    # image_thumbnail = ImageSpecField(
    #     source='image', # 원본 ImageField 이름
    #     processors=[Thumbnail(200, 300)],
    #     format='JPEG',
    #     options={'quality': 90},
    # )
    # 나중에 추가된 필드의 경우 blank 속성이 필요함.
    image = models.ImageField(blank=True)
    image = ProcessedImageField(
        # ProcessedImageField에 인자로 들어가 있는 값들은 migrations 이후에 추가되거나 수정되더라고 makemigrations를 하지 않아도 된다.
        processors=[Thumbnail(200, 300)], # 처리할 작업 목록
        format='JPEG', # 저장 포맷
        options={'quality': 90}, # 추가 옵션들
        upload_to='articles/images', # 저장 위치(MEDIA_ROOT/articles/images)
    )
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