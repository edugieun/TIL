# REST ful

## HTTP URI

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

## Method

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

## Model Instance Method

- get_absolute_url()

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

    

    