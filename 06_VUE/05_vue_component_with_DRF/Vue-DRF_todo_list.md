# Vue와 DRF를 이용하여 Todo list 만들기
## 흐름도

1. (Django) 회원 가입
2. (Vue->Django) POST방식 유저정보(credentials)를 통해 로그인 시도
3. (Django) Vue에서 받은 유저정보에 해당하는 고유한 Web Token(JWT) 발급
4. (Django->Vue)Access Token(JWT) 발급 후 발급된 JWT Token을 전달
5. (Vue)JWT를 vue-session을 통해 저장(이 시점부터 vue에서는 로그인 성공 상태)
6. (Vue->Django) 다시 한번, Autherization header에 vue-session에 저장된 토큰을 붙여서 django에 로그인 요청을 보냄
7. (Django)JWT를 해석하여 정보 확인. 최초로 보낸 토큰과 일치하는지 여부를 확인 후 로그인 처리
8. (Django->Vue)응답 response

## BackEnd(Django) 개발 환경 설정

- `todo-front`: Vue-CLI로 Vue 개발 환경 생성 `vue create todo-front`

### CORS - JWT 사용 설정

- djangorestframework 설치 `pip install djangorestframework` 및 앱등록
- djangorestframework-jwt 설치 및 세팅 `pip install djangorestframework-jwt`
  - [https://jpadilla.github.io/django-rest-framework-jwt/]

```python
# settings.py
# DRF JWT 설정
REST_FRAMEWORK = {
    # 로그인 여부를 확인하는 클래스
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 인증 여부를 확인하는 클래스
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
```

```python
# urls.py
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    ...
```



## FrontEnd(Vue) 개발 환경 설정

- `todo-back`: `todo-back` 폴더 생성 후 내부에서 Django를 위한 환결 설정
  - 가상환경 생성 / 장고 설치 / 프로젝트 및 앱 생성
- `vue ui`에서 현재 폴더 경로가 잘 지정되어 있는지 확인 후, 다르다면 프로젝트 매니저로 경로 재설정
- ` @vue/cli-plugin-router ` 플러그인 설치  후, `history mode` 사용 체크(URL 주소에서 해쉬 뱅(#!)을 사용하지 않는다는 뜻)

# TodoBack

## CORS - JWT  사용 설정

- djangorestframework-jwt 설치 및 세팅 `pip install djangorestframework-jwt`
  -  https://jpadilla.github.io/django-rest-framework-jwt/ 



- django-cors-headers 설치 및 세팅 `pip install django-cors-headers`
  -  https://github.com/adamchainz/django-cors-headers 

## Modeling

- `User` 정보를 `외래키`로 사용하기 위해 User 모델을 불러온 후,

```python
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

- `settings.py`에서 `AUTH_USER_MODEL`을 재선언해준다.

```python
AUTH_USER_MODEL = 'todos.User'
```
# TodoFront

## Login Component

### LoginForm component

- 로그인 폼 만들기
- axios로 장고에 요청하기
- `vue-session` 플러그인 설치 `$ npm i vue-session` 및 세팅
  -  https://www.npmjs.com/package/vue-session 
  - JWT Token에 접근할 수 있게 해준다.
- ` this.$session.start() `
  - session-id 초기화. 만약 세션이 없이 저장하려고 하면 vue-session 플러그인이 자동으로 새로운 세션을 시작
  - `.start()`를 통해 `session-id:sess + Data.now()`가 만들어짐
  - `.set()`을 통해 `jwt: jwt`값이 만들어짐
- ` this.$session.set(key,value) `
  - session에 해당 key에 맞는 값을 저장
-  `this.$session.has(key) `
  - key(JWT)가 존재하는지 여부를 확인
- ` this.$session.destroy() `
  - 세션을 삭제

npm i jwt-decode

------

## Vue 의 라이플 사이클

1. Vue instance 생성(create)
2. DOM에 부착(mounted)
   1. 업데이트(update)

------

FormData

- 기존 키에 새로운 값을 추가하거나 키가 없는 경우 새로운 키를 추가.
  - `FormData.append(name, value)`
  - name: value에 포함되는 데이터 필드 이름
  - value: 필드 값