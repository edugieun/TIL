# REST API

## dumpdata

```bash
$ python manage.py dumpdata musics > dummy.json
$ python manage.py dumpdata --indent 2 musics > dummy.json
```

## loaddata

`fixture`

- 데이터베이스의 직렬화(serialized)된 내용을 포함하는 파일 모음이다.

- 각 fixture는 고유한 이름을 가지며, 이를 구성하는 파일은 여러 응용 프로그램에서 여러 디렉토리에 배포될 수 있다.

- django는 `loaddata`시 설치된 모든 app 에서 `fixtures`라고 하는 이름의 폴더를 찾는다.

- ```
  musics/
  	fixtures/
  		musics/
  			dummy.json
  ```

- ```bash
  $ python manage.py loaddata musics/dummy.json
  ```

  
------

없어도 서버 열리는데 왜 생성하는 거지?

API 서버와의 통신을 위한 데이터 표현 파일(JSON, XML, YAML)을 생성한다.

```bash
$ python manage.py dumpdata --indent 2 musics > dummy.json
```

![image](https://user-images.githubusercontent.com/52814897/67958543-ad75ec00-fc3a-11e9-8680-92011f6f8aae.png)

- 생성된 파일을 다음의 폴더 경로를 생성한 후 넣는다.

```
musics/ 
	fixtures/
		musics/
			dummy.json
```

------

API란?

- API(Application Programming Interface, 응용프로그램 프로그래밍 인터페이스)
- API는 명확하게 '어떤 것이다.'라고 규정하기는 어렵지만, 서로 다른 시스템, 장치들이 서로 좀 더 편하고 원활하게 소통할 수 있게 도와주는 인터페이스(서로를 연결해주는 것) 또는 수단이라고 생각할 수 있다.
- 예를 들어, 프로그래밍에서 API는 math, I/O 등의 라이브러리, avg(), max(), min() 같은 내장 함수 등 개발을 하는데 편하게 해주는 기능.
- 운영체제인 window가 chrome이라는 응용프로그램을 여는 행위, google에서 검색 하는 행위.
- 개발자가 지도나 날씨 어플리케이션을 만들 때, 위치 정보, 날씨 정보가 담긴 데이터를 가져오는 방법이나 명령어.
- 이처럼 서로 다른 시스템, 장치들이 서로 소통할 수 있게 해주는 기능 또는 규격을 API 라고 한다.

API 사용 이유

RESTful API란?

-  [https://blog.npcode.com/2017/04/03/rest%EC%9D%98-representation%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80/](https://blog.npcode.com/2017/04/03/rest의-representation이란-무엇인가/) 
- https://mangkyu.tistory.com/46 
- https://brainbackdoor.tistory.com/53 
- https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html 

POSTMAN 사용 이유

------

api 서버 주소 네이밍

- 먼저 프로젝트의 `urls.py`에서 사용할 API 서버의 기본 주소를 정해준다.
- 알아보기 쉽게 `프로젝트명/version/` 식으로 명명해주면 좋다.

```python
# 프로젝트/urls.py
urlpatterns = [
    path('api/v1/', include('musics.urls')),
    path('admin/', admin.site.urls),
]
```

모델링

- 가수와 가수의 음악, 그리고 음악에 코맨트 정보를 담을 모델링을 한다.

```python
# models.py
class Artist(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.TextField()
    def __str__(self):
        return self.title

class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)        
    content = models.TextField()
    def __str__(self):
        return self.content
```

데이터 생성 및 데이터 표현 파일 생성

- 장고 admin 페이지에서 가수, 음악, 코맨트의 간단한 DB를 추가한다.

```python
# admin.py
admin.site.register(Artist)
admin.site.register(Music)
admin.site.register(Comment)
```

![image](https://user-images.githubusercontent.com/52814897/67957293-b960ae80-fc38-11e9-8964-40c47c575f06.png)



API 서버 구축

DRF 설치

- 보다 편리하게 API 서버를 구축하기 위해, 장고에서 제공하는 DRF(Djnago Rest Framework)를 사용하자. ( https://www.django-rest-framework.org/ )

```bash
$ pip install djangorestframework
```

- 설치후 `settings.py`에서 `rest_framework`를 추가해준다.

Serialization(직렬화)

- 직렬화는 내가 가진 데이터를 다른 환경에서도 쉽게 주고 받기 위해, 동일한 구조로 구성하는 것을 말한다.
- 위에서 작성한 Model 인스턴스 기반의 복잡한 Django DB를 JSON, XML 형태로 만들어준다.

```python
# 앱/serializers.py
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)
        
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id',)
```

view 작성

- 최종적으로 보여질 데이터를 return하는 함수를 작성해야 한다.
- `@api_view`는 DRF에서 제공하는 데코레이터로, 어떤 HTTP Method 방식으로 요청을 받을 건지 정할 수 있다.
- 클래스(Artist, Music)에 담긴 모든 객체들을 불러와, `serializers.py`에서 작성한 직렬화된 데이터 구조로 반환(응답, Response)한다.

```python
# 앱/views.py
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

```

url 작성

- API 서버에 접속한 URL 주소를 작성한다.

```python
urlpatterns = [
    path('artists/', views.artist_list),
    path('musics/', views.music_list),
]
```

API 서버 확인

- 주소로 접속하면 작성한 DB들이 JSON 형태로 작성되어 있는 것을 확인할 수 있다.

![image](https://user-images.githubusercontent.com/52814897/67971903-018bcb00-fc51-11e9-9365-43137372f7a6.png)

