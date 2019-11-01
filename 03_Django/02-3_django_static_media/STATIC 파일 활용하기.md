# STATIC 파일 활용하기

- Static file은 웹 서비스에서 사용하기 위해 개발 과정에서 미리 준비한 파일이다.
  - 예) JS, CSS, Image
- 파일은 실제 경로에 고정되어 있고, 웹 사이트 배포 후 서비스 중에도 추가되거나 변경되지 않는다.

## static 파일 경로 설정

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

## static 파일 load

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



## 정적 파일 추가 경로

- 여러개의 app에서 공용적으로 사용하는 static 파일들의 경우에는 특정 위치에 따로 모아놓는 경우가 편리하다.