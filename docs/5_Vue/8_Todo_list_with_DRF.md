# Vue와DRF를 이용하여 Todo list 만들기

## 개요

- Frontend 역할을 하는 Vue가 Backend(Server) 역할을 하는 Django에 요청(Request)를 보내기 위해서는 항상 JWT라는 기술이 필요하다.

### JWT

- 

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
- `vue-session` 플러그인 설치 `$ npm i vue-session` 및 세팅(main.js 파일에 import 해줘야한다.)
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

-------

`splice()`

- 배열의 기존 요소를 삭제 속은 교체하거나 새 요소를 추가하여 배열의 내용을 변경
- `Array.splice(시작 index, 삭제할 요소 수, 배열에 추가할 요소)`
- `splice(start, deleteCount, [item1, item2, item3...])`
- start
  - 배열의 변경을 시작할 인덱스
  - 배열의 길이보다 큰 값이면 시작 인덱스는 배열의 길이로 설정
  - 음수인 경우 배열의 가장 마지막에서 시작
  - 절대 값이 배열의 길이보다 큰 경우는 0으로 설정
- deleteCount
  - 배열에서 제거할 요소의 수
  - 생략할 경우 start부터 모든 요소를 제거
  - 0이하인 경우 어떤 요소도 삭제하지 않음. 이때는 최소한 하나의 츄가할 새로운 요소 저장
- item1, item2...
  - 배열에 추가할 요소
  - 추가할 요소를 지정하지 않으면 요소를 제거만 한다. 즉, 원본 배열의 특정 인덱스에서 몇 개의 요소를 삭제할지 정한다.

`updated`

- type: function
- 데이터가 변경되어 DOM이 re-render되고 patch 되면 호출된다. (DOM 변화에 반응)
- DOM의 변화는 일반적으로 데이터의 변경에 의해 re-render 되는 시점에 일어난다.
- 데이터의 변화(상태의 변화)에 반응하기 위해서는 computed나 watch를 사용하는 것이 좋다.

-------

## Vuex

- State관리를 위해 탄생
- 컴포넌트 간의 통신 혹은 데이터 전달을 유기적으로 관리
- 컴포넌트 간의 통신 혹은 이벤트 등의 관계를 한 곳에서 관리하기 쉽게 구조화

현재 Todo 프로젝트에서는 Auth 정보(로그인 혹은 로그아웃)은 django로 요청을 보낼 때 항상 필요하기 때문에, 요청을 수행하는 모든 컴포넌트에서 알고 있어야 하고 그 정보를 내가 필요한 순간에 활용할 수 있어야 한다.

- State
  - 상태(데이터)
- Getters
  - computed
- Mutations
  - methods
  - state를 변경하기 위해서 반드시 `동기적인 method만` 사용 가능
  - 첫번째 인자는 항상 state이며, commit으로 호출된다.
- Actions
  - 모든 methods 동기, 비동기 처리가 가능한 methods
  - mutations와 구분된 이유는 다양한 컴포넌트에서 vuex를 통해 상태관리, 메서드 호출등을 하게 될텐데 그 때 동기와 비동기를 구분하기 위해.
  - 첫번째 인자는 항상 context(state/commit/dispatch 등)이며, dispatch로 호출된다.

------

- vuex는 `vue-session`의 대체가 아니고 서로 하는 일이 다르다.
- vuex는 메서드와 data의 대체라고 생각하면 된다.