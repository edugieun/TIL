# Django

- 6가지 특징
  - Vesatile(다용도) / Secure / Scalable(확장성) / Complete / Maintanable / Portable
- 성격
  - 최근 프레임 워크들은 대부분 독선적(간결하고 빠름). Django - 다소 독선적
  - 독선적(프레임워크에 맞춰야함. 간결하나 자유도는 떨어짐) vs 관용적(최소한의 도움. 자유도 높음. 간결하지 못할 수 있음)
- Dynamic Web(또는 Web APP)
- 의존성

  - 본인의 컴퓨터에서 잘 작동하던 프로그램도 다른 프로그램에 설치 했을 때 잘 동작하리라는 보장이 없음.
  - 파이썬도 같은 버전, 같은 모듈을 쓴다는 보장이 없다.
  - 특정 프로그램만을 실행하기 위한 파이썬 환경을 따로 만들어서, 그 환경속에서만 모듈을 관리하고, 앱을 실행시키기 위해 가상환경을 성절한다.
  - 다른 앱을 실행시키는 일이 생기면 그 가상환경을 빠져나와 다른 환경을 만드는 방식으로 진행한다.

- 대부분 MVC(Model View Controller) (Controller가 중간 관리자)인데, Django는 MTV(Model Template View) (View가 중간관리자) / Modle = 데이터 관리 / Template = 사용자가 보는 화면 / View = 중간 관리자

## 설치 및 기초명령어

가상환경 설정

- 가상환경은 한번에 2개 킬 수 없으니, 일단 시스템 환경 변수 설정에서 다시 python 3.7.3으로 바꿔줌.

- ``` bash
  # 가상환경 만드는 법
  python -m venv 가상환경 경로+이름
  python -m venv ~/documents/ssafy (이름만 쓰면 현재 폴더에 가상환경 만듬)
  ```

  - ```bash
    # 원하는 폴더에서 git bash키고
    python -m venv venv # gitignore 설정상 venv로 설정되어있느니 그냥 가상환경 이름은 venv로 함
    # 이름 바꾸면 gitignore에서도 가상환경 이름 추가해주면 됨.
    source venv/Scripts/activate
    pip list
    쓰고 뜨는 update 명령어 복붙 (python -m pip install --upgrade pip)
    pip list
    버젼 확인
    끄는법은 deactivate
    하고 명령어 복사해서 module update 한번 해줌 (따로 설치하란 말 안뜨면 안해도 됨.)
    ```

- VS CODE에서 가상환경 켜기

  - 00_django_intro(venv 폴더가 있는 위치)에서 VS CODE 열고  ctrl+shift+p 누르고 python:select interpreter 에서 3.7.3  가상환경으로 킴

  - vscode에서 ctrl + ` 눌러서 터미널 키고 activate 

    - 터미널 안켜질 경우

      - ctrl+shif+p로 json수정

        - ```json
          {
              "terminal.integrated.cwd": "${workspaceFolder}",
              "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
              "editor.fontFamily": "Souce Code Pro, Hack, Consolas, 'Courier New', monospace",
              "[html]": {
                  "editor.tabSize": 2
              },
              "[css]": {
                  "editor.tabSize": 2
              }
          }
          ```

      - shortcut설정 들어가서 integrated 검색후 ctrl + ` 설정

- vscode 터미널에서 장고 설치 `pip install django` 후 버전 확인 `python -m django --version`

### 프로젝트 생성 및 작성

- 프로젝트 생성: `django-admin startproject django_intro .` 마침표(.)을 붙이지 않으면 django_intro폴더안에 또 django_intro가 있어서 번거롭게 2번 들어가야됨.
- 서버 켜기: `python manage.py runserver` 터미널 번호가 1번이어야 에러 안뜰거임.

- 앱 만들기: `python manage.py startapp pages` 여기서 앱 이름을 pages로 정했는데, 통상적으로 앱 이름은 복수형으로 만듬.

- 앱 등록: settings.py 에서 `pages.apps.PagesConfig`를 추가 및 한글화

  - ```python
    # Application definition
    """
    app 등록 순서
    1. local apps(우리가 만든거)
    2. Third party apps
    3. Django apps(기본적으로 세팅되어 있는 애들)
    """
    INSTALLED_APPS = [
        #`pages', 만 써도 되는데, 나중에 제약적인 요소가 있어서 아래처럼함.
        'pages.apps.PagesConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ...
  LANGUAGE_CODE = 'ko-kr'
    
    TIME_ZONE = 'Asia/Seoul'
    ```
    
  - 한글화: `LANGUAGE_CODE = 'en-us'`  를 `LANGUAGE_CODE = 'ko-kr'`로 바꾸고 시간도 `TIME_ZONE = 'Asia/Seoul'` 로 바꿔

- **코드 작성 순서**
  
  - view: 만들고자 하는 view 함수 작성
  - url: views에서 만든 함수에 주소를 연결
    - `url.py` 파일에서 먼저 `*from 앱이름 import views` 를 선언하여 앱 안에 views파일을 읽겠다고 선언해야 함.
- temlplates: 해당 view 함수가 호출 될 때. 보여질 페이지
  
- **DTL**
  
  - Django Template Language
  - django template에서 사용하는 내장 template system
- 조건, 반복, 변수 치환, 필터 등 많은 기능을 제공한다.
  
- **CSRF 사이트 간 요청 위조**
  
- 관련 00_django_intro > user_new, user_create, settings.py
  
- 웹 어플리케이션 취약점 중 하나로 사용자가 자신의 의도와 무관하게 공격자가 의도한 행동을 해서 특정 웹페이지의 보안을 무력화 시키거나, 수정, 삭제 등의 강제적인 작업을 하게하는 공격 방법.
  
- django는 최소한의 안전장치를 위해 자신이 부여한 랜덤 hash값을 token으로 부여한다. 이 token 값이 없는 요청은 잘못된 요청이라고 판단하여 접근을 거부한다.(403 error)
  
    - ```python
      <form action="/user_create/" method="POST">
        {% csrf_token %} <!-- POST 방식은 항상 csrf_token을 붙여줄 것-->
      ```

------

### 정적파일(static)

- image / css / js 파일과 같이 해당 내용이 고정되어 응답을 할 때 별도의 처리 없이 그대로 보여주면 되는 파일들

### URL 로직 분리

### Django namespace

- templates / static 분리

### 상속



------

190816 수업 정리

1. Form(GET/POST)
2. POST - csrf_token
3. static(load, {% static %})
4. URL 로직(프로젝트 & 앱)
5. Namespace(template, static)
6. 상속(Block)



VS Code 안에서 django 버젼같은거 똑같이 설치하는 법

-의존성 기록(구성환경 리스트 목록 만들기)

pip freeze > requirements.txt

-의존성 설치

pip install -r requirements.txt

------

190821

## ORM

- 자세한 내용은 PDF 참고
- SQL과 개발자가 사용하는 언어 사이를 해석해주고 이어줌.

장점

1. SQL을 몰라도 db 사용이 가능하다.
2. SQL의 절차적인 접근이 아닌 객체 지향적 접근 가능
3. 매핑 정보가 명확하여 ERD를 보는 것에 대한 의존도를 낮출 수 있다.
   - ERD: DB 구축시 필요한 다이어그램
4. ORM은 독립적으로 작성되어 있고, 해당 객체들을 재활용 할 수 있다. 개발자는 객체에 집중함으로써 해당 DB에 종속될 필요 없이 자유롭게 개발할 수 있다.

단점

1. ORM 만으로 완전히 거대한 서비스를 구현하기가 어렵다.
   - 사용하기는 편하지만, 설계는 매우 신중하게 해야함.
   - 프로젝트의 규모가 커질 경우 난이도가 올라가게 된다.
   - 순순 SQL보다 약간의 속도 저하가 생길 수 있다.

2. 이미 프로세스가 많은 시스템에서는 ORM으로 대체하기가 어렵다.

결론 - 그럼에도 ORM을 사용하는 이유는?

- 생산성. ORM을 사용하여 얻게되는 생산성은 약간의 성능저하나 다른 단점들을 상쇄할 만큼 뛰어나기 때문.
- 장점으로 인한 생산성 증가가 훨씬 크기 때문에, 현대에는 대부분의 프레임워크들이 ORM을 사용하고 있다.
- 즉, 우리는 DB를 객체(object) - 인스턴스(instance)로 조작하기 위해 ORM을 배운다.

### model

모델의 개념

- 모델은 단일한 데이터에 대한 정보를 가지고 있다.
- 필수적인 필드(컬럼, 열)와 데이터(레코드, 행)에 대한 정보를 포함한다. 일반적으로 각각의 **모델(클래스)**는 단일한 데이터베이스 **테이블과 매핑(연결, 연동)**된다.
- 모델은 부가적인 메타데이터를 가진 **DB의 구조(layout)를 의미**
- 사용자가 저장하는 데이터들의 **필수적인 필드와 동작(behavior)을 포함**

#### Field

https://docs.djangoproject.com/en/2.2/ref/models/fields/#charfield

- CharField()
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - `max_length`는 필수 인자이다. 필드의 최대 길이(문자)이며, DB와 django의 유효성 검사(값 검증)에서 사용된다.
  - 텍스트 양이 많을 경우 `TextField()`로 사용
- TextField()
  - 글의 수가 많을 때 사용
  - max_length 옵션을 줄 수 있지만, 모델과 실제 DB에는 적용되지 않는다. 길이 제한을 주고 싶다면 CharField()를 사용해야 한다.
- DateTimeFiled()
  - 시간과 날짜를 기록하기 위한 필드
  - `auto_now_add=True`: django ORM이 **최초 INSERT**(테이블에 데이터 입력)시에만 현재 날짜와 시간을 작성. 즉, 최초 생성 일자
  - `auto_now=True`: django ORM이 SAVE를 할 때마다 현재 날짜와 시간 작성. 즉, 최종 수정 일자.

model 로직

- DB 컬럼과 어떠한 타입으로 정의할 것인지에 대해 `django.db` 모듈의 `models`의 상속을 받아서 적용된다.

- 각 모델은 **`django.db.models.Model` 클래스의 서브 클래스**로 표현된다.(자식 클래스)
- 모든 필드는 **기본적으로 NOT NULL 조건**이 붙는다.(NULL 값이 들어갈 수 없다.)
- 각각의 **클래스 변수**들은 **모델의 데이터베이스 필드**를 나타낸다.

### Migrations

1. migrations

   - ```bash
     $ python manage.py makemigrations
     ```
     
   - ```bash
      #해당 migrations 설계도가 SQL 문으로 어떻게 해석되어서 동작할지 미리 볼 수 있다.
      $ python manage.py sqlmigrate app_name 0001
      
      # migrations 설계도가 migrate 됐는지 안됐는지 확인
      $ python manage.py showmigrations
      
      
      ```
      
   - ons모델(model.py)을 작성/변경한 사항을 django 에게 알리는 작업.  (ORM에 보낼 python 코드 설계도를 작성)
   
   - 테이블에 대한 설계도(django ORM이 만들어 줌)를 생성.


2. migrate

   - migrations로 만든 설계도를 기반으로 실제 DB 테이블을 만듦. ( `db.sqlite3`)
   
   - 모델에서의 변경사항들과 DB 스키마가 동기화를 이룬다.
   
   - ```bash
     $ python manage.py migrate
     ```

- SQL 들어가기

  - ```bash	
    $ sqlite3 db.sqlite3
    
    # 테이블 확인
    >>> .tables
    # 나가기
    >>> .exit
    ```

history

```bash
498  python -m venv venv
499  source c:/Users/student/Desktop/TIL_gieun/03_Django/01_django_orm_crud/venv/Scripts/activate
500  pip list
501  python -m pip install --upgrade pip
502  pip list
503  pip install django
504  django-admin startproject crud .
505  python manage.py startapp articles
506  python manage.py runserver
507  python manage.py makemigrations
508  python manage.py sqlmigrate articles 0001
509  python manage.py makemigrations
510  python manage.py migrate
511  python manage.py showmigrations
```

------

### Model 변경 시 작성 순서

1. `models.py`: 작성 및 변경(생성 / 수정)
2. `makemigrations`: migrations 파일 만들기(설계도)
3. `migrate`: 실제 DB에 적용 및 동기화(테이블 생성)

- 테이블의 이름은 app 이름과 model에 작성한 class 이름이 조합되어 자동으로 만들어진다.(**모두 소문자**)
- 모델의 클래스 변수들은 반드시 **소문자**로 작성한다.

**망했을 때 데이터베이스 테이블 다 날리는 법**

- `0001,0002.py` 등의 설계도 다 지우고
- `db.sqlite3` 지우면 됨

-------

### CRUD

- DB API 조작

1. Django Shell
   - django 프로젝트 설정이 로딩된 파이썬 shell.
   - 일반 파이썬 shell 로는 django 환경에 접근 불가
   - 즉, django 프로젝트 환경에서 파이썬 shell을 활용한다고 생각하면 됨.

QuerySet 기본 개념

- 전달 받은 객체의 목록

  - `QuerySet`: 쿼리 set 객체
    - `objects`를 사용하여 다수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체
    - 단일한 객체를 반환(리턴)할 때는 테이블(class)의 인스턴스로 리턴 됨.
  - Query: 단일 객체

- DB로부터 데이터를 읽고, 필터를 걸거나 정렬 등을 수행

- **Query를 던지는 Language(django ORM)를 활용해서 DB에게 데이터에 대한 조작을 요구한다.**

  - ```ipython
    In [1]: from articles.models import Article
    
    In [2]: Article.objects.all()
    # DB에 쿼리를 날려서 인스턴스 객체 전부를 달라고 하는 뜻
    # SELECT*FROM articles_article; 와 같은 말인데, sql이 아닌, ORM을 이용한 방법임
    Out[2]: <QuerySet []>
    ```

- `objects`
  - Model Manager와 Django Model 사이의 Query연상의 인터페이스 역할을 해주는 친구.
  - 즉, `models.py`에 설정한 클래스(테이블)을 불러와서 사용할 때 DB와의 인터페이스 역할(쿼리를 날려주는)하는 매니저이다.
  - 쉽게 이해하려면 ORM의 역할이라고 생각하면 된다.
  - DB---------objects--------Python Class(models.py)
  - Manager(objects)를 통해 특정 **데이터를 조작(메서드)**할 수 있다.

#### CREATE

데이터 객체를 만드는(생성, CREATE)하는 3가지 방법

1. 첫번째 방법

   ```python
   $ python manage.py shell
   
   # 만약 ORM없이 SQL로만 작성한다면 아래와 같음.
   # INSERT INTO table (column1, column2, ...) VALUES (value1, value2, ...)
   # INSERT INTO articles_article (title, content) VALUES('first', 'django!')
   
   # ORM으로 작성
   >>> article = Article() # Article class 로부터 article 인스턴스 생성
   >>> article.title = 'first' # 인스턴스 변수(title)에 값을 할당
   >>> article.content = 'django!' # 인스턴스 변수(content)에 값을 할당
   # save를 하지 않으면 아직 DB에 값이 저장되지 않음
   >>> article
   <Article: Article object (None)>
   >>> Article.objects.all()
   <QuerySet []>
   # save를 하고 확인해보면 저장된 것을 확인할 수 있음.
   >>> article.save()
   >>> article
   <Article: Article object (1)>
   >>> Article.objects.all()
   <QuerySet [<Article: Article object (1)>]>
   
   #인스턴스 article을 활용하여 변수에 접근할 수 있다.(저장된 값 확인)
   >>> article.title
   'first'
   >>> article.content
   'django!'
   >>> article.created_at
   datetime.datetime(2019, 8, 21, 2, 43, 56, 271842, tzinfo=<UTC>)
   >>> article.updated_at
   datetime.datetime(2019, 8, 21, 2, 43, 56, 271842, tzinfo=<UTC>)
   ```

2. 두번째 방법

   ```PYTHON
   # 첫번째 방법을 한 줄에 쓰는 것
   In [15]: article = Article(title='second', content='djnago!!')
   In [16]: article
   Out[16]: <Article: Article object (None)>
   In [17]: article.save()
   In [18]: article
   Out[18]: <Article: Article object (2)>
   In [20]: Article.objects.all()
   Out[20]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
   ```

3. 세번째 방법

   - `create()`를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한번의 스텝으로 끝난다.
   - 단, 바로 저장하기 때문에 **유효성 검사가 불가능**하기 때문에, 수업에선 잘 사용하지 않을 예정

   ```python
   # 가장 짧은 방식. save()메소드도 포함되어 있다.
   In [21]: Article.objects.create(title='third', content='django!!!')
   Out[21]: <Article: Article object (3)>
   ```

유효성 검사

- save 전에 `full_clean()` 메서드를 통해 article 이라는 인스턴스 객체가 검증(validation)에 적합한지를 알아 볼 수 있다.
- `models.py`에 필드 속성과 옵션에 따라 검증을 진행한다.

#### READ

```python
# 1. SELECT * FROM articles.article; # SQL
# 1. DB에 있는 모든 글 가져오기
>>> Article.objects.all() # ORM

# 2. SELECT * FROM articles_article WHERE title = 'first';
# 2. DB에 저장된 글 중에서 title이 first인 글만 가져오기 # SQL
>>> Article.objects.filter(title='first') # ORM

# 3. SELECT * FROM articles_article WHERE title='first' LIMIT 1;
# 3. DB 내의 title이 'first'인 글 중에서 첫번째 글만 가져오기
>>> Article.objects.filter(title='first').first()
>>> Article.objects.filter(title='first').last()

# 4-1. SELECT * FROM articles_article WHERE id=1;
# 4-1. DB에 저장된 글 중에서 PK 가 1인 글만 가져오기
>>> Article.objects.get(pk=1)

# PK만 .get()으로 가져올 수 있다. (.get() 은 값이 중복이거나 일치하는 값이 없으면 에러를 발생시킨다.) 즉, pk에만 사용하자.

# 4-2. filter 의 경우 존재하지 않으면 에러가 아닌 빈 쿼리셋을 반환한다. 마치 딕셔너리에서 value를 꺼낼 때 []방식으로 꺼내냐 혹은 .get으로 꺼내냐 하는 차이와 유사
>>> Article.objects.filter(pk=100)

# 4-3. filter / get
# filter 자체가 여러 값을 가져올 수 있기 때문에 django가 개수를 보장하지 못한다. 그래서 0개, 1개라도 무조건 쿼리셋으로 반환한다.

# 5-1. 오름차순
# SELECT * FROM articles_article ORDER BY title ASC;
>>> Article.objects.order_by('pk')

# 5-2. 내림차순
# SELECT * FROM articles_article ORDER BY title DESC;
>>> Article.objects.order_by('-pk')

# 6. 쿼리셋은 리스트 자료형은 아니지만, 리스트에서 할 수 있는 인덱스 접근 및 슬라이싱이 모두 가능하다.
>>> Article.objects.all()[2]
>>> Article.objects.all()[1:3]

# 7. LIKE / startswith / endswith
# django ORM은 이름(title)과 필터(contains)를 더블언더스코어(__)로 구분한다.
# 더블언더스코어 == 던더(dunder)스코어

# LIKE
>>> Article.objects.filter(title__contains='fir')
# startswith
>>> Article.objects.filter(title__startswith='fir')
# endswith
>>> Article.objects.filter(title__endswith='!!!')
```

------

#### UPDATE

- 업데이트 후 항상 저장을 해야 DB에 적용된다.

```python
# article 인스턴스 객체의 인스턴스 변수에 들어있는 기존 값을 변경하고 저장
>>> article = Article.objects.get(pk=1)
>>> article.title = 'byebye'
>>> article.save()
```

------

#### DELETE

```python
# article 인스턴스 객체를 생성 후, .delete() 메서드를 호출
>>> article = Article.objects.get(pk=1)
>>> article.delete()
```

------

### ADMIN

https://docs.djangoproject.com/en/2.2/ref/contrib/admin/

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지.
- `models.py`에 작성한 클래스를 `admin.py`에 등록하고 관리.
- record 생성 여부 확인에 매우 유용하고 직접 레코드를 작성할 수도 있다.
- CRUD 로직을 모두 관리자페이지에서 사용할 수 있다.

관리자 변경 목록(change list) 커스터마이징

1. list_display
   - admin 페이지에서 우리가 `models.py`에 정의한 각각의 속성(컬럼)들의 값(레코드)을 보여준다.
2. list_filter
   - 특정 필드에 의해 변경목록을 필터링 할 수 있게 해주는 Filter 사이드바를 추가한다.
   - 표시되는 필터의 유형은 필드이 유형에 따라 다르다.
3. list_display_links
   - 목록 내에서 링크로 지정할 필드 적용(설정하지 않으면 기본값을 첫번째 필드에 링크가 적용)
4. list_editable
   - 목록 상에서 직접 수정할 필드 적용
5. list_per_page
   - 한 페이지에 표시되는 항목 수를 제어 (default=100)

------

### Django Extensions

https://django-extensions.readthedocs.io/en/latest/

```
pip install django-extensions
```

- Django-extension은 커스텀 확장 tool이다.
- Django app 구조로 되어 있기 때무넹 프로젝트에서 사용하기 위해서는 app등록 과정을 거쳐야 한다.

## URL 분리

- 프로젝트 URL 수정

  - ```python
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('articles/', include('articles.urls')),
        path('admin/', admin.site.urls),
    ]
    ```

- 앱 urls.py 생성

  - ```python
    from django.urls import path
    
    urlpatterns = [
        
    ]
    ```

- 프로젝트에 templates폴더와 base.html 생성

  - base.html에 부트스트랩 및 {% block %} 추가

- 템플릿 경로 설정

  - ```python
    'DIRS': [os.path.join(BASE_DIR, 'crud', 'templates')],
    ```

- 앱 view.py 함수 추가

  - ```python
    from django.shortcuts import render
    
    # Create your views here.
    def index(request):
        return render(request, 'articles/index.html')
    # articles/를 안 써줄 경우 namespace 문제 발생
    # 앱이 2개일 경우 먼저 등록된 것만 읽힘. 따라서 명시 해줘야 함.
    ```

- requirements.txt
  - 모듈 저장
    - `pip freeze > requirements.txt`
  - 모듈 불러오기
    - `pip install -r requirements.txt`

------

## URL Namespace

- 하드코딩 URL 제거
  - `{% url %}` template tag
  - 내부적으로 `reverse()` 사용하며, 리턴 값으로 문자열 반환
  - 인자가 필요할 경우 공백으로 구분
    - `{% url 'articles:update' articel.pk %}`
  - 문제점: app이 여러개가 되면, 단순히 url name만 가지고는 어떤 app의 url인지 알 수 없다.
- URL namespace 설정
  - `app_name`을 붙여준다.

------

## REST ful

### HTTP URI

- URI은?
  - 인터넷에 자원을 나타내는 유일한 주소
  - 인터넷에서 요구되는 기본조건으로서 http에 항상 붙어 다닌다.
- URL은?
  - 인터넷 상에서 자원이 어디 있는지 알려주기 위한 규약
- 예제
  - https://www.google.com
    - 서버주소. URL이면서 URI 이다.
  - https://github.com/ss-02-djpy2/TIL/blob/master/03_django/markdown/Django_01.md
    - 주소 + 디렉토리 파일의 주소(자원의 위치)
    - URL이면서 URI
  - https://www.google.com/search?q=삼성
    - 주소 + 특정 문자열(query string)(`search?q=`)
    - seach까지가 URL + `q=삼성` 이라는 `식별자`가 필요하므로 URI 이지만 URL은 아니다.

### Method

- GET / POST / PATCH(PUT) / DELETE

- 실제로 HTTP에서는 공식적으로 GET, POST만 공식적으로 사용된다.

- 같은 주소로 들어가는데 GET이냐 POST냐에 따라 행동을 다르게 할 것이다.

  - 예) NEW+CREATE 두개를 합쳐서.

  - `if` 문을 이용하여 `GET`일 경우와 `POST`일 경우의 액션을 다르게 줌

    - ```python
      def create(request):
          # CREATE
          if request.method == 'POST':
              title = request.POST.get('title')
              content = request.POST.get('content')
              article = Article(title=title, content=content)
              article.save()
              return redirect('articles:detail', article.pk)
          # NEW
          else:
              return render(request, 'articles/new.html')
      ```

- form tage에 action이 없다면, 현재 머물고 있는 URL로 요청을 보낸다.

### Model Instance Method

- get_absolute_url()

  - 특정 모델에 대해 detail view를 작성할 경우, detail url을 완성하자마자 사용하는 것을 권장한다.
  - 반복되는 코드가 줄고 보다 간결해진다.
  - `redirect`를 통해서 모델 인스턴스의 get_absolute_url() 함수를 자동으로 호출

- URL Reverse를 수행하는 함수들

- reverse()

  - 리턴 값: string(문자열)

    ```python
    reverse('articles:index') # '/articles/'
    ```

- redirect()

  - 리턴 값: HttpResponseRedirect(객체)

  - 내부적으로 `resolve_url()`을 사용

  - view 함수에서 특정 url로 돌려보내고자 할 때 사용

    ```python
    redirect('articles:article') # 리턴 값이 아래와 같이 객체
    # <HttpResponseRedirect status_code=200,"text/html; charser ...">
    ```