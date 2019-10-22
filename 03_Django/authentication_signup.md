## http에서 쿠키와 세션 생긴 이유

- 비연결지향(connectionless)
- 상태정보 유지 안함(stateless, 무상태): 연결이 끊어지는 순간 클라이언트와 서버간의 통신이 끝남(각각 완벽하게 독립적)
- 이런 현상들을 막기 위해 쿠키와 세션이 생김
- 쿠키(cookie): 클라이언트 로컬에 파일로 저장
  - 브라우저에 저장
  - 클라이언트의 로컬에 저장되는 키-값의 작은 데이터파일
  - 웹페이지에 접속하면 요청한 웹페이지를 서버로부터 받고 쿠키를 로컬에 저장하고, 클라이언트가 재요청시 웹페이지 요청과 함께 쿠키 값도 함께 전송
  - 예) 아이디 자동완성 / 공지 메세지 하루 안 보기 / 팝업 안보기 / 비로그인 장바구니에 담기 등 편의를 위하되 지워지거나 유출되도 큰 일은 없을 정보들을 저장
- 세션(session): 서버에 저장(이때 session id는 쿠키의 형태로 클라이언트의 로컬에 저장)
  - 사이트와 특정 브라우저(클라이언트) 사이의 상태를 유지시키는 것
  - 일정 시간동안 같은 브라우저로부터 들어오는 일련의 요구를 하나의 상태로 보고 상태를 유지하는 기술
  - 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키를 사용하여 저장. 클라이언트가 다시 서버에 접속하면 해당 쿠키(session id가 담긴)를 이용해 서버에 session id를 전달한다.
  - Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아낸다. 실질적인 session의 database에 기본 설정 값으로 저장된다. (이는 쿠키 안에 데이터를 저장하는 것보다 더 보안에 유리하고, 쿠키는 악의적인 사용자들에게 취약하기 때문)
  - 세션을 남발하면 사용자가 많은 서버일 경우 서버 부하가 발생한다.
  - 쿠키를 지우면 왜 로그아웃?
    - 서버에서는 session에 사용자 로그인 정보를 가지고 있지만, 그것이 내 것이라는 걸 증명할 session id가 쿠키에서 사라졌기 때문.
- 캐시(cache)
  - 가져오는데 비용이 드는 데이터를 한 번 가져온 뒤에는 임시로 저장.
  - 사용자의 컴퓨터 또는 중간 역할을 하는 서버에 저장.

## Sign up

- user를 create

Authentication(인증) - 신원 확인

- 자신이 누구라고 주장하는 사람의 신원을 확인하는 것

Authorization(권한, 허가) - 권한 부여

- 가고 싶은 곳으로 가도록 혹은 원하는 정보를 얻도록 허용하는 과정

## Login

## Logout

### 로그인 사용자에 대한 접근 제한

- django는 세션과 미들웨어를 통해 인증 시스템을 request 객체에 연결한다.
- request는 현재 사용자를 나타내는 모든 요청에서 `request.user`를 제공한다.
- `is_authenticated`
  - User model의 속성(attributes)들 중 하나.
  - 사용자가 인증 되었는지 알 수 있는 방법
  - User에는 항상 True
  - Anonymous user에 대해서만 항상 False
  - 단, 이것은 권한과는 관련이 없으며, 사용자가 활동중(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않는다.
  - 일반적으로 request.user에서 이 속성을 사용하여 미들웨어의 `django.contrib.auth.middleware.AuthenticationMiddleware` 를 통과했는지 확인한다.

`next` query string parameter

- `@login_required`데코레이터가 기본적으로 인증 성공 후 사용자를 리다이렉트 할 경로를 next 라는 문자열 매개 변수에 저장한다.
- 우리가 url로 접근하려고 했던 그 주소가 로그인하지 않으면 볼 수 없는 곳이라서, django가 로그인 페이지로 강제로 redirect 했는데, 로그인을 다시 정상적으로 하고 나면 원래 요청했던 주소로 보내주기 위해 keep 해두는 것.

------

**@required_POST가 있는 함수에 @login_required가 설정된다면 로그인 이후 "next"매개 변수를 따라 해당 함수로 다시 redirect되면서 @required_POST 때문에 405에러가 발생.**

------

## 회원 탈퇴

## 회원 정보 수정

`get_user_model()`

- `User`를 직접 참조하는 대신 `django.contrib.auth.get_user_model()` 를 사용하여  User model을 참조해야 한다.
- 이 함수는 현재 활성화(active) 된 User model을 return 한다.

## 비밀번호 변경

- 비밀번호 변경 후 로그아웃되는 현상
- 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 버렸기 때문.

`update_session_auth_hash`

- 현재 사용자의 인증 세션이 무효화 되는 것을 막고, 세션을 유지한 상태로 업데이트.
- 현재 request와 새로운 session hash가 생긴 업데이트 된 user 객체를 적절히 업데이트.

## django 서버가 켜질 때 초기화 순서

1. `INSTALLED_APPS`의 각 항목을 imports 한다. (`위에서 아래로`)
   - 이 과정에서 직간접적으로 모델을 import 해선 안된다.
   - 1번 단계에서 app을 import하는 동안에 불필요한 제약들을 피하기 위해 이 단계에서는 모델을 가져오지 않는다.
2. 각 어플리케이션의 models를 import 한다.
   - 2단계가 완료가 되면, `get_model()`과 같은 모델에서 작동하는 APIs를 사용할 수 있게 된다. 
   - `articles` / `accounts`처럼 2개의 app을 사용할 때, models.py에서 User class를 가져올 때 `get_user_model()` 대신 `settings.AUTH_USER_MODEL`를 사용하는 이유도 여기 있다.
   - 2단계가 끝나야 `get_user_model()`을 사용할 수 있는데, 아직 accounts app이 INSTALLED_APP의 작성 순서 때문에 아직 IMPORT가 완료되지 않은 상황이라, `get_user_model()`이 어떤 User model을 return 해야 하는지 django가 알 수 없는 상황이다.
   - 결론: 모든 곳에서 User model을 호출할 때는 `get_user_model()`을 사용한다. 단, `models.py`에서만 `settings.AUTH_USER_MODEL`을 사용한다.
3. `AppConfig`의 `ready()`메서드를 실행한다.

------

## gravatar 프로필 이미지

1. ModelForm Custom
2. Custom template tags and filters

------

## Model relationships

1. Many-to-one
2. Many-to-Many

- 모델링은 현실 세계를 최대한 유사하게 반영하기 위해서 해야한다.
- 환자와 의사의 예약 시스템을 구축하라는 프로젝트
- 1:N의 한계가 있기 때문에
- 중개 모델이 필요하다.
- 중개 모델을 직접 거치지 않고 바로 가져올 수는 없을까?
  - `Through` option
  - MTOM 필드는 실제 물리적인 field가 db에 생기는 것이 아니다.
- Doctor 도 patients로 참조할 수 없을까?
  - `related_name`
    - 참조되는 대상이 참조하는 대상을 찾을 때(역참조), 어떻게 불러 올지에 대해 정의한다.
    - 필수적으로 사용하는 건 아니지만, 필수적인 상황이 발생할 수 있다.
  - `related_name`을 쓰면 중개모델은 필요 없는가? 아니다.
    - 예약한 시간 정보를 담는다거나 하는 경우(==추가적인 필드가 필요한 경우)에는 반드시 중개모델을 만들어서 진행을 해야되는 상황도 있다. 다만 그럴 필요가 없는 경우 위와 같이 해결할 수 있다.

------

## Like

- user는 여러 article에 좋아요를 누를 수 있고
- article은 여러 user로부터 좋아요를 받을 수 있다.
- 변수명 혼동하지 말 것.
- `article.user` => 게시글을 작성한 유저 - 1:N
- `article.like_users` => 게시글을 조아요한 유저 - M:N
- `user.like_articles` = > 유저가 좋아요를 누른 게시글(역참조, `related_name`) - M:N
- `user.article_set` => 유저가 작성한 게시글(역참조) - 1:N
- 