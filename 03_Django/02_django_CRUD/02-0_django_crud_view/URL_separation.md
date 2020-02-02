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

  - Django가 먼저 찾는 기본 templates 경로는 앱에 있는 경로 이기 때문에 프로젝트의 templates도 경로로 추가해준다.

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