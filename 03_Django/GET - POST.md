프로젝트는 crud

setting에서 앱등록하고, 템플릿 폴더 만들고 DIRS 경로 지정

```
'DIRS': [os.path.join(BASE_DIR, '프로젝트명', 'templates')],
```

urls에서 urls import에 include 추가하고

```
from django.urls import path, include
```

앱.urls도 include해줘

```
path('articles/', include('articles.urls')),
```

템플릿에 base.html 생성 후 container랑 block생성

```
<div class="container">
    {% block content %}
    {% endblock %}
  </div>
```

프로젝트는 여기가 끝

------

앱은 articles

urls 부터 연결해줘

```
from django.urls import path
from . import views
```







슈퍼계정 만들기

```bash
$ python manage.py createsuperuser
```



full_clean() : 유효성 검사







### GET -> POST

글을 작성할 때 GET이 아닌 POST를 쓴느 3가지 이유

1. 사용자는 django에게 **HTML 파일을 줘!(GET)**가 아니라 **~한 레코드(글)를 생성해줘!(POST)** 이기 때문에 GET보다는 POST 요청이 더 알맞다.
2. 데이터는 URL에 노출되면 안된다.(우리가 URL에 접근하는 방식은 모두 GET). query의 형태를 통해 DB schema를 유추할 수 있게 되고 이는 보안의 측면에서 매우 취약하게 된다.
3. 모델(DB)를 조작하는 친구는 GET이 아닌 POST 요청! 왜냐? DB를 수정하는 건 매우 중요한 일이고 그에 따른 최소한의 신원 확인이 필요.-> scrf token
   - GET으로 동작하게 된다면, 악성사용자가 URL 만으로 글을 작성, 수정, 삭제할 수 있게된다.

### Redirect

- POST 요청은 HTML 문서에 render하는게 아니라, ~~좀 처리해줘(요청)의 의미이기 때문에 요청을 처리하고 나서의 결과를 보기위한 페이지로 넘겨줘야 한다.
- POST 요청으로 변경 후 변화하는 것
  - form을 통해 전송한 데이터를 받을때도 `request.POST`로 받아야 한다.
  - 글이 작성되면 실제로 URL에 데이터가 나타나지 않게 된다.
  - HTML 문서를 요청하는게 아니기 때문에 HTML 문서를 받아볼 수 있는 다른 페이지로 redirect하게 된다.