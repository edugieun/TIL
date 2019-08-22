from django.db import models

# Create your models here.
# 모델 할때는 서버를 꺼놓고 한다.
class Article(models.Model): # model은 클래스로 선언. models에 있는 Model을 상속 받아.
    title = models.CharField(max_length=20, blank=True) # 캐릭터 필드는 길이제한 / blank는 유효성 검증에서만 동작하며, 기본값은 false이다.
    content = models.TextField(blank=True) # 텍스트필드는 길이 제한 없음
    created_at = models.DateTimeField(auto_now_add=True) # 최초만 추가
    updated_at = models.DateTimeField(auto_now=True) # 수정될 때마다

    # 객체표현
    def __str__(self):
        return self.title