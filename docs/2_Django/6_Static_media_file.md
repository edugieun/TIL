# Static / Media 파일

## STATIC 파일 활용하기

- Static file은 웹 서비스에서 사용하기 위해 개발 과정에서 미리 준비한 파일이다.
  - 예) JS, CSS, Image
- 파일은 실제 경로에 고정되어 있고, 웹 사이트 배포 후 서비스 중에도 추가되거나 변경되지 않는다.
- 홈페이지 상단에 항상 떠 있는 로고나, 어플리케이션 자체 아이콘 등이라고 이해하면 된다.

### static 파일 경로 설정

- Django가 정적 파일을 찾을 때는 `settings.py`에 등록된 앱 순서대로 static 파일의 기본 경로인 `/APP_NAME/static/`**에서부터** 파일을 찾는다.

- 이 때, 앱이 여러개 있을 경우, 파일이름이 같다면 잘못된 파일을 가져올 가능성이 있다.

  - 예를 들어,  app_A 와 app_B가 있고, 각각 dog.jpg 라는 파일을 가지고 있다고 하자.

  - ```
    app_A/								app_B/
    	static/								static/
    		images/								images/
    			dog.jpg								dog.jpg
    ```

  - 위의 폴더 구조에서 `settings.py`에 app_A 가 먼저 등록 되어있다고 해보자.

  - app_A에서 dog.jpg 파일을 불러오기 위해서 기본 경로 이후부터인 `images/dog.jpg`을 검색하고, 존재한다면 파일을 가져온다. 이 경우 최종 전체 경로는 `app_A/static/` + `images/dog.jpg`이다.

  - 이번엔, app_B가 자기 자신 하위 폴더에 있는 dog.jpg 파일을 불러 오려고한다.

  - 마찬가지로, 기본 경로 이후 부터인 `images/dog.jpg`로 파일을 호출하였다.

  - 하지만, 먼저 등록된 app_A에도 같은 경로에 같은 파일이 있었고, Django는 파일을 찾았다고 판단하여 app_B의 dog.jpg가 아닌 app_A의 dog.jpg를 보내주게 된다.

- 따라서, 정확한 경로의 파일을 가져오기 위해 templates 처럼 static도 앱과 같은 이름으로 `namespace`가 필요하다. => `/APP_NAME/static/APP_NAME(Namespace)/`

### static 파일 load

- 실습을 위해 `articles`라는 앱에 static 파일을 하나 넣는다. (`articles/static/articles/images/dog.jpg`)

![image](https://user-images.githubusercontent.com/52814897/68010925-42272b00-fcc9-11e9-8d62-31809c42f41b.png)

- `{% load static %}`으로 static 파일 로드를 선언 한 후, 아래의 `img`태그처럼 사용할 수 있다.

```django
...
{% load static %}

{% block content %}
  <img src="{% static 'articles/images/dog.jpg' %}" alt="static_img" style="width: 300px;">
...
```



### 정적 파일 추가 경로

- 특정 app이 아닌 여러개의 app에서 공용적으로 사용하는 static 파일들의 경우에는 특정 위치에 따로 모아놓는 경우가 편리하다.
- 일반적으로, 프로젝트 폴더 내에 `assets`폴더로 지정하며, 마지막에 아래와 같이 꼭 쉼표를 붙여야 에러가 나지 않는다.

```python
# settings.py
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'PROJECT_NAME', 'assets'), # 마지막 쉼표
]
```



## MEDIA 파일 활용하기(이미지파일 업로드하기)

- `media` 파일은 사용자들이 글을 작성하거나 할 때, 함께 첨부하는 파일을 말한다.

### Media 파일 경로 설정

- static 파일과 마찬가지로 사용자가 media 파일을 업로드할 경우 그 파일이 서버 어디에 저장되어야 하는지를 지정해줘야 한다.
- `MEDIA_URL`: 웹 상에서 media 파일이 있는 위치를 URL 주소로 접근하기 위한 경로를 지정해준다.
- `MEDIA_ROOT`: 사용자가 파일을 업로드할 시 실제 저장되는 서버의 경로를 지정해준다.
  - 일반적으로 프로젝트나 앱 폴더 내부가 아닌, 프로젝트나 앱이 위치한 루트 경로로 지정한다.

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

- 위의 `Media 파일 경로 설정` 과정에서 업로드된 media 파일이 머무르는 곳은 알았지만, 웹 사이트 상에서 저장된 media 파일의 위치에 접근하기 위해선 별도의 처리가 필요하다.
- 장고의 라이브러리 `settings`와 `static`이 이를 제공하며, `urlpatterns` 마지막에 아래와 같이 추가해준다.

```python
# PROJECT/urls.py
...;
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 이미지 파일 업로드하기

#### 모델링(Modeling)

- image 파일을 등록해줄 `image field`가 필요하므로 모델에 추가해준다.
- 단, `ImageField`를 사용하기 위해서는 `Pillow`라는 라이브러리르 설치해줘야 한다.

#### **Install Pillow** 

- Pillow는 이미지 파일 형식을 지원하고 처리하는 오픈 소스 라이브러리이다.
- Pillow를 설치 후 이미지 파일을 처리할 수 있다.

```bash
$ pip install Pillow
```

- `Pillow` 설치 후 모델에 image field를 추가한다.

```python
# app/models.py
class Article(models.Model):
    ...
    image = models.ImageField(blank=True)
    ...
```

- `blank=Ture`: 장고 DB는 데이터 무결성에 따라 `blank`속성이 `False`로 설정되어있다. 따라서, 이미 작성된 글에도 `image field`가 비어 있는 상태로 추가하기위해 blank 속성을 True로 변경한다.

#### HTML / VIEW

- `Create HTML`에 image 파일을 올리기 위한 폼을 수정한다.
- `enctype="multipart/form-data"`: 이미지나 파일을 업로드 할 경우, 반드시 `form`태그의 `enctype` 메서드에 `multipart/form-data` 속성을 설정해줘야 한다.
- `accept="image/*"`는 업로드시 image 파일만 보이도록 선택 목록을 필터링 해준다. 단지 보여주는 목록만 필터링 해줄 뿐, 비디오나 오디오 파일도 선택해서 제출할 수도 있다.

```django
<!-- create.html -->
<form action="" method="POST" enctype="multipart/form-data">
  ...
  <label for="image">IMAGE</label>
  <input type="file" name="image" id="image" accept="image/*"><br>
```

- 업로드 제출한 파일을 view함수에서 처리하여 DB에 저장해야한다.
- `request.FILES.get('image')`만 필드에 담아 저장해주면 된다.

```python
# views.py / def create
...
image = request.FILES.get('image')
article = Article(title=title, content=content, image=image)
article.save()
...
```

- 파일이 정상적으로 업로드된다면, 지정된 폴더에 자동으로 파일이 추가되는 것을 볼 수 있다.

![image](https://user-images.githubusercontent.com/52814897/68082997-ed211b80-fe66-11e9-9a28-57ed964d4e71.png)

### 이미지 파일 불러오기

- 저장된 이미지 파일의 url주소로 접근하여 웹 상에 띄우면 된다.
- `article.image.url`: 이미지 파일의 실제 url 주소
- `article.image`: 이미지 파일의 파일명

```django
<!-- detail.html -->
<img src="{{ article.image.url }}" alt="{{ article.image }}">
```

- 이 때, 이전에 작성한 image 파일이 없는 글의 경우 image 파일의 url 주소를 찾을 수 없기 때문에 에러가 발생하는데, 아래와 같이 처리할 수 있다.

```django
{% if article.image %}
  <img src="{{ article.image.url }}" alt="{{ article.image }}">
{% endif %}
```

### 이미지 사이즈 조절

- 원본 사이즈로 불러온 이미지의 크기를 조절하고 싶을 경우
- `img`태그에서 직접 width와 height를 조절해도 되지만, 용량 문제 때문에 이미지 자체를 resizing 할 필요가 있다.
- 마찬가지로, 오픈 소스 라이브러리를 이용하자.

**Install django-imagekit**

- 우선 `django-imagekit` 설치해야 하는데, 그 전에 `Pillow`와 `pilkit`을 먼저 설치해준다.
- 순서를 지키지 않으면 제대로된 동작을 하지 않을 수 있다.

```bash
$ pip install Pillow
$ pip install pilkit
$ pip install django-imagekit
```

- 설치 후 `settings.py`에 `imagekit`를 추가한다.

```python
# settings.py
INSTALLED_APPS = [
    ...
    'imagekit',
    ...
]
```

**Modeling**

- Model에서 라이브러리를 추가하고 몇 가지 속성을 수정한다.
- 이 때, 원본을 저장하는 않는 방법과 저장하는 방법이 있다.

**원본 저장 X**

- `image field`에 바로 resizing 옵션을 주면 원본 파일은 저장하지 않는다.

```python
# models.py
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Article(models.Model):
    ...
    image = ProcessedImageField(
        processors=[Thumbnail(200, 300)], # 처리할 작업 목록
        format='JPEG', # 저장 포맷
        options={'quality': 90}, # 추가 옵션들
        upload_to='APP_NAME/images', # 저장 위치 
    )
```

- `upload_to`: resizing 된 사진 파일을 저장할 위치를 지정한다. `APP_NAME/images`와 같이 설정할 경우 `MEDIA_ROOT/articles/images` 에 저장되며, 앞서 `MEDIA_ROOT `의 경로는 최상의 폴더의 `media` 폴더로 설정하였다.

![image](https://user-images.githubusercontent.com/52814897/68086092-4ef37c80-fe8b-11e9-8152-5e076886f52e.png)

- 위의 사진처럼, root media 폴더 내부에 따로 `articles`폴더를 만들어 놓지 않아도, 모델부에서 자동으로 `articles/images/`폴더를 만들어 저장한다.

**원본 저장 O**

- 변환된 파일 뿐 아니라 원본 파일도 저장하고 싶다면 새로운 필드를 생성해줘야 한다.
- 

```python
# models.py
from imagekit.models import ..., ImageSpecField
...
class Article(models.Model):
    ...
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
     source='image',  # 원본 ImageField 명
     processors=[Thumbnail(200,300)],    
     format='JPEG',  
     options={'quality': 90},
     )
```

```django
<!-- app/detail.html -->
<img src="{{ article.image_thumbnail.url }}" alt="{{ article.image }}">
```

- `image_thumbnail` 필드에서 이미지를 가져오면 아래와 같이 `CACHE` 폴더 내부에 이미지가 따로 저장된다.

![image](https://user-images.githubusercontent.com/52814897/68086312-ce824b00-fe8d-11e9-81eb-0bfd35e57bf3.png)

- 이 경우 처음 이미지를 불러올 때는 로드 하지만, 다음 부터는 브라우저 CACHE에 저장한 후 꺼내오기 때문에, 다시 로드할 필요없이 빠르게 불러올 수 있다.

![image](https://user-images.githubusercontent.com/52814897/68086353-6718cb00-fe8e-11e9-8ac1-49c3ed90bdbd.png)

## 참고 사항

### Null / Black

- NULL

  - 기본 값: False
  - DB와 관련되어 있다.(databased-related)
  - 주어진 컬럼이 NULL 값을 가질 것인지를 결정.

- blank

  - 기본 값: False
  - 데이터 유효성과 관련되어 있다. (Validation-related)
  - `full_clean()` / `is_valid()` 처럼 유효성 검사 메서드가 호출될 때, 유효성 검사에 사용된다.

- `null=True, bland=False` 와 같이 두개를 동시에 사용하면?

  - DB내에서는 해당 필드가 NULL을 사용하지만, 웹 사이트에서는 HTML INPUT 태그에 `required`속성이 필요하다는 것을 의미한다.

  주의사항

  - 문자열 기반 필드(charField, TextField ...) 에서는 null=True 금지.

  - 이렇게 정의하게 되면 문자열 기반 필드는 `데이터 없음`에 대한 값이 2가지가 된다. None과 빈 문자열을 갖게 된다.

  - 데이터 없음에 대한 조건이 2가지면 중복이기 때문에 문자열 기반 필드는 NULL이 아닌 빈문자열을 사용하는게 장고의 컨벤션이다.

    ```python
    class Person(models.Model):
        name = models.TextField(blank=True) # name은 null=True 금지
        birth = models.DataField(null=True, blank=True)
        # birth는 문자열 기반 필드가 아닌 숫자 필드이기 때문에 가능.
    ```

### Image Update

- 이미지도 edit을 통해 새로운 이미지로 수정할 수는 있지만, text와는 다르게 수정할 때 이미지를 무조건 업로드 하지 않으면 에러가 발생한다.(글만 수정하는 건 안된다는 의미.)
- 이미지는 바이너리 데이터(하나의 덩어리)라서 텍스트처럼 일부만 수정하는게 불가능. 그렇기 때문에 html input태그에 value 속성으로 수정하는 방식이 아니고, 새로우 나진으로 덮어 씌우는 방법을 사용.
  - `<input type="file">`가 `value=""`를 지원하지 않는다.
  - 정말 글만 수정하고 싶다면 이전과 똑같은 이미지를 업로드하면 된다.
- 문제: 이미지 필드 설정 이전에 작성했던 게시글의 detail 페이지가 동작하지 않는다.(article.image.url을 불러오지 못하기 때문)

  - 해결방법1: static 파일로 이미지가 없을 때 대신 사용할 이미지를 미리 넣어둠.
  - 해결방법2: 템플릿에서 {% if %} 문으로 article.image 가 존재하는 경우만 이미지를 출력하도록.
- 이미지 업로드 경로 커스텀
  - `instance.pk`는 `처음(최초)` 레코드가 작성되는 순간에는 pk값이 없기 때문에 `media/articles/None/images`로 저장된다.
    - 따라서, 실제 개발에선 로그인을 통해 유저 정보를 받고, `instance.user.pk`또는 `instance.user.username`처럼 업로드한 유저의 정보로 폴더를 구조화하는 경우가 많다.