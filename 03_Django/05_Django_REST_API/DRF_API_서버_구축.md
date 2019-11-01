

# DRF(Django Rest Framework)를 이용한 API 서버 구축하기

## 서버 주소 네이밍

api 서버 주소 네이밍

- 먼저 프로젝트의 `urls.py`에서 사용할 API 서버의 기본 주소를 정해준다.
- 알아보기 쉽게 `프로젝트명/version/` 식으로 명명해주면 좋다.

```python
# project/urls.py
urlpatterns = [
    path('api/v1/', include('musics.urls')),
    path('admin/', admin.site.urls),
]
```

## 모델링 (Modeling)

- 만들고자 하는 명세(specifications)에 따라 각각의 model을 작성한다.

```python
# app/models.py
...;

class Movie(models.Model):
    title = models.CharField(max_length=50)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=150)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
...;
```

##  Seed Data 저장

- Seed Data가 있다면 `loaddata`로 데이터를 django DB에 저장한다.
  - seed data가 없다면 test를 위해 django admin 페이지에 직접 데이터를 넣는다.
- 이 때, 위의 seed 파일은 `app/fixtures/` 경로에 위치해야한다.

```bash
$ python manage.py loaddata genre.json
$ python manage.py loaddata movie.json
```

## rest_framework 설치

- 편리하게 API 서버를 구축하기 위해, 장고에서 제공하는 DRF(Djnago Rest Framework)를 사용하자. ( https://www.django-rest-framework.org/ )
- API 서버로 사용할 Django rest_framework를 설치 후 `settings.py`에 추가한다.

```bash
$ python pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS = [
    ...,
    'rest_framework',
    ...,
]
```

## Serialization (직렬화)

- Serialization(직렬화)는 내가 가진 데이터를 다른 환경에서도 쉽게 주고 받기 위해, 동일한 구조로 구성하는 것을 말한다.
- Django DB에 저장된 데이터들을 API 서버를 통하여 외부에서도 참조할 수 있게 일관된 데이터 구조를 갖도록 만들어준다.
- 위에서 작성한 Model 인스턴스 기반의 복잡한 Django DB를 JSON, XML 형태로 만들어준다.

## Genre List 나타내기

`serializers.py`

- 이전에 배웠더 `forms`과 비슷한 형태로, `model`과 `fields`를 지정해준다.

```python
from rest_framework import serializers
from .models import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name',)
```

`views.py`

- 최종적으로 보여질 데이터를 return하는 함수를 작성해야 한다.
- `@api_view`: DRF에서 제공하는 데코레이터로, 어떤 HTTP Method 방식으로 요청을 받을 건지 정할 수 있다.
- `Response` : DRF(Django Rest Framework)는 HTTP 요청(request)에 대해서 `Response`메소드로 응답(response)한다.

```python
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre
from .serializers import GenreSerializer

@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
```

`url.py`

- 사용하고자 하는 주소를 지정해준다.

```python
urlpatterns = [
    path('genres/', views.genre_list),
    ...
]
```

- 서버를 켜서 주소와 페이지가 제대로 작동하는지 확인한다.
- 주소로 접속하면 작성한 DB들이 JSON 형태로 작성되어 있는 것을 확인할 수 있다.

![image](https://user-images.githubusercontent.com/52814897/67998718-e5158000-fc9c-11e9-8b7a-99413e3273c8.png)

## 장르별 영화 나타내기

`serializers.py`

- 각 장르에 따른 영화 데이터를 보여주기 위해서 `Movie` 모델을 직렬화한다.

```python
# Movie DB Serialization
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'audience', 'poster_url', 'description', 'genre_id',)

```


- 이후, 역참조하여 영화 정보들을 불러와 세부 `fields`를 추가해야한다.

```python
class GenreDetailSerializer(GenreSerializer):
    movies = MovieSerializer(source='movie_set', many=True)  
    class Meta(GenreSerializer.Meta):
        fields = GenreSerializer.Meta.fields + ('movies',)
```

`views.py`

- 함수 인자로 장르의 `id`값을 받으며, 해당하는 값이 없을 경우 `404 error`페이지를 표시한다.

```python
@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)
```

![image](https://user-images.githubusercontent.com/52814897/67999204-9c5ec680-fc9e-11e9-82b4-ae5513a328c4.png)

## 영화 리스트와 세부정보(댓글표시)

- 위의 `Genre List 나타내기`와 `장르별 영화 나타내기`를 바탕으로, 영화 리스트와 영화 `id` 값에 따른 세부 영화 정보를 보여주는 api 를 작성할 수 있다.
- 영화의 세부정보에서는 해당 영화에 달린 `review`들도 같이 표시한다.

`serializers.py`

- 앞서 `serializers.py`에 영화에 대한 serializer를 작성하였으므로, review DB를 직렬화한 후

```python
# Review DB Serialization
class ReviewSerialier(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','content', 'score', 'movie_id',)
```

-  영화 세부 내용에 리뷰들도 같이 보이도록 serialization 구조를 재구성 해준다.

```python
class MovieDetailSerializer(MovieSerializer):
    reviews = ReviewSerialier(source='review_set', many=True)
    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ('reviews',)
```

`views.py`

- genre와 같은 방식으로 영화 리스트와 세부 내용에 대한 view 함수를 작성한다.

```python
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)
```

![image](https://user-images.githubusercontent.com/52814897/67999633-7fc38e00-fca0-11e9-87eb-addcf0d4ca05.png)

![image](https://user-images.githubusercontent.com/52814897/67999662-91a53100-fca0-11e9-8b76-49f0f4d29936.png)

## Review 작성

- ## `POST` 방식으로 요청을 받는 리뷰 작성의 경우, 요청 받은 데이터를 받아 유효성 검사 후 저장하게 된다.

`views.py`

```python
@api_view(['POST'])
def reviews_create(request, movie_pk):
    get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerialier(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_pk)
    return Response({'message': '작성되었습니다.'})
```

- `POSTMAN`을 통해 API 요청과 응답을 테스트 해볼 수 있으며, 정상 동작이 API에 새로운 리뷰 데이터가 추가된다.

![image](https://user-images.githubusercontent.com/52814897/67999923-7a1a7800-fca1-11e9-8089-bf54830bc0c6.png)
![image](https://user-images.githubusercontent.com/52814897/67999942-84d50d00-fca1-11e9-9a3d-c44e48212b50.png)

## Review 수정 및 삭제

- 수정과 댓글의 경우 같은 `id` 값을 갖는 댓글에 대해서, 같은 주소의 HTTP Method만 다르게 하여 처리할 수 있다.

`views.py`

```python
@api_view(['PUT', 'DELETE'])
def reviews_update_and_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerialier(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '수정되었습니다.'})
    else:
        review.delete()
        return Response({'message': '삭제되었습니다.'})
```

`urls.py`

```python
urlpatterns = [
    path('genres/', views.genre_list),
    path('genres/<int:genre_pk>/', views.genre_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>', views.movie_detail),
    path('movies/<int:movie_pk>/reviews/', views.reviews_create),
    path('reviews/<int:review_pk>/', views.reviews_update_and_delete),
]
```



- 마찬가지로 POSTMAN에서 `PUT`과 `DELETE`방식으로 요청을 보낸 후 결과를 확인한다.

![image](https://user-images.githubusercontent.com/52814897/68000128-2eb49980-fca2-11e9-9560-0a3b12d19b25.png)
![image](https://user-images.githubusercontent.com/52814897/68000134-370cd480-fca2-11e9-8e34-de99439f8114.png)
![image](https://user-images.githubusercontent.com/52814897/68000152-43912d00-fca2-11e9-939c-43abf3bd29da.png)

## Specification Documents

- API 명세를 보여주는 페이지를 만들기 위해 `drf_yasg`를 설치한 후, `settings.py`에 추가한다.

```bash
$ pip install -U drf-yasg
```

- 공식 사이트( https://github.com/axnsan12/drf-yasg )를 참고하여 `urls.py`에 코드를 작성한다

`urls.py`

```python
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Movie API",
        default_version='v1',
        description="영화 관련 API 서비스 입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gieun625@gmail.com"),
        license=openapi.License(name="SSAFY License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    ...
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

```



![image](https://user-images.githubusercontent.com/52814897/68001663-5c044600-fca8-11e9-9456-98cbba540e8d.png)