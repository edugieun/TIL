from django.db import models

# Create your models here.
# model은 객체지향으로 동작할 것이므로 class 를 먼저 선언
class Article(models.Model): # models.Model의 상속을 받는다.
    # 클래스 변수 선언
    # id(프라이머리 키)는 기본적으로 처음 테이블 생성시 자동으로 만들어짐
    # id = models.AutoField(primary_key=True) # AutoField는 글 순서를 자동으로 정해줌.
    title = models.CharField(max_length=10) # 클래스 변수(DB의 필드) / blank=False, null=Flase 이 두개는 default 값이다.
    content = models.TextField() # 클래스 변수(DB의 필드)
    created_at = models.DateTimeField(auto_now_add=True) # 클래스 변수(DB의 필드)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}번글 - {self.title} : {self.content}'