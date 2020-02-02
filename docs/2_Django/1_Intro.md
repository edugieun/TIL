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

## 파이썬 가상 환경 만들기

- 가상환경을 만드는 이유?
  1. 단순히 각 개발 환경에 필요한 plugin들만 설치하기 위해서. 글로벌로 설치하면 모든 프로젝트에 영향을 미칠 수 있으니, 불필요한 용량을 차지할 수 있다.
  2. 두 개의 서로 다른 버전이 필요한 경우. 
     - Django 수업은 3.7 버전이 필요
     - 알고리즘 수업은 3.5 버전만 허용
     - 아래의 경우는 가상환경은 3.7버전, 평상시에는 3.5 버전을 유지하기 위한 설정

```bash
student@DESKTOP MINGW64 ~
$ python -V # 파이썬 버젼보기
Python 3.7.3

student@DESKTOP MINGW64 ~
$ mkdir ~/python-virtualenv

student@DESKTOP MINGW64 ~
$ python -m venv ~/python-virtualenv/3.7.3

$ code ~/.bashrc

export FLASK_ENV=development
alias jp="jupyter notebook"
alias venv="source ~/python-virtualenv/3.7.3/Scripts/activate"

$ source ~/.bashrc

$ venv # 이게 가상환경 키는거
또는 직접 들어가서 source로 실행
$ source venv/Scripts/activate
$ deactivate # 끄는거
```

- 이후 검색- 시스템 환경 변수 편집-환경 변수-위에 path 더블 클릭 ptyhon 3.7을 3.5아래로 내림

- 가상환경은 한번에 2개 킬 수 없으니, 일단 시스템 환경 변수 설정에서 다시 python 3.7.3으로 바꿔줌.

  ``` bash
  # 가상환경 만드는 법
  python -m venv 가상환경 경로+이름
  python -m venv ~/documents/ssafy (이름만 쓰면 현재 폴더에 가상환경 만듬)
  ```

```bash
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
  
- CSRF 사이트 간 요청 위조
  
- 관련 00_django_intro > user_new, user_create, settings.py
  
- 웹 어플리케이션 취약점 중 하나로 사용자가 자신의 의도와 무관하게 공격자가 의도한 행동을 해서 특정 웹페이지의 보안을 무력화 시키거나, 수정, 삭제 등의 강제적인 작업을 하게하는 공격 방법.
  
- django는 최소한의 안전장치를 위해 자신이 부여한 랜덤 hash값을 token으로 부여한다. 이 token 값이 없는 요청은 잘못된 요청이라고 판단하여 접근을 거부한다.(403 error)
  
    - ```python
      <form action="/user_create/" method="POST">
        {% csrf_token %} <!-- POST 방식은 항상 csrf_token을 붙여줄 것-->
      ```
