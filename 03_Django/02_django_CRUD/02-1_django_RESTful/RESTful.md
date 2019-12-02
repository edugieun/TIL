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

### GET -> POST

글을 작성할 때 GET이 아닌 POST를 쓰는 3가지 이유

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

## Model Instance Method

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
