# Django Axios - 비동기식 웹 브라우저

> JavaScript와 Axios를 이용하여 '좋아요'를 눌러도 새로고침이 되지 않는 비동기식 웹 브라우저 만들기

## 사전 지식

### Axios 

- HTTP 통신을 위한 JavaScript 라이브러리이며 문법, 함수 등 XHR 요청을 쉽게 사용할 수 있도록 도와주는 라이브러리이다.

### XMLHttpRequest(XHR)

- 웹 브라우저는 XMLHttpRequest 객체를 이용하여 AJAX 요청을 생성하고 전송한다.
- 서버가 브라우저의 요청에 대해 응답을 반환하면 같은 XHR 객체가 그 결과를 처리한다.
- 단 IE 5, 6에서는 ActiveXobject를 사용해야 한다.

### AJAX

- Asynchronous JavaScript and XML
- 웹 사이트에서 비동기식 기능을 구현하기 위한 기법이다.
- 예를 들어, 좋아요를 눌렀을 때 새로고침되지 않고 바로 좋아요가 반영되게 하는 것이다.

------

## Axios CDN 추가

- Axios 설치하지 않고 사용하기 위해 CDN을 추가해준다.

```django
<!-- articles/base.html -->
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

## Template 수정

### _article.html a태그 삭제 및 수정

- a태그는 더이상 필요가 없다.

```django
<!-- articles/_article.html -->
{% if user in article.like_users.all %}
    <i class="fas fa-heart like-button" style="color: crimson; font-size: 20px;" data-id="{{ article.pk }}"></i>
    {% else %}
    <i class="fas fa-heart like-button" style="color: black; font-size: 20px;" data-id="{{ article.pk }}"></i>
    {% endif %}
    <span id="like-count-{{ article.pk }}">{{ article.like_users.all|length }}</span> 명이 좋아함.
```

- `like-button`:  `DOM`문법으로 접근하기 위한 클래스를 하나 정해준다.
- `data-`: `data-*속성`은 HTML에 정보를 바로 저장할 수 있도록 해준다.
- `like-count-{{ article.pk }}`: 역시 `DOM` 문법으로 접근하기 위해 지정해주는 id값이다.

## Axios 요청과 응답

### Axios 요청

- index.html에서 `DOM` 조작으로 `class`가 `.like-button`인 객체를 모두 불러온 후
- 각각의 객체에 `이벤트리스너`를 추가해준다.
- `conslo.log(event)`를 이용하여 `article_pk`의 위치를 확인하여 가져온다.

```javascript
// 'articles/index.html'
const likebuttons = document.querySelectorAll('.like-button')
likebuttons.forEach(button => {
button.addEventListener('click', function (event) {
    const articleId = event.target.dataset.id
    ...
```

- 좋아요를 `click`했을 때 `axios`로 요청을 보낸다.
  - 만약, POST 방식으로 보내고 싶을 경우 아래와 같은 3가지 구문이 필요하다.

```javascript
// 'articles/index.html'
// POST 방식으로 보낼 시 필요한 3가지 구문
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

axios.post(`/articles/${articleId}/like/`)
        .then(response => {
    	...
```

### Axios 응답

- `url`주소를 통해서 생성된 요청은 다시 `view`함수를 거쳐 `response`로 반환되는데, `view` 함수에서 어떤 값을 반환하는지 확인하자.
- view의 like 함수에서 `request`객체의 `is_ajax()`메소드를 통해, 받은 요청이 AJAX 요청인지 확인한다. (그렇지 않을경우 `Bad Request: 400` 에러 처리)

```python
# 'articles/views.py'
from django.http import JsonResponse, HttpResponseBadRequest
...
@login_required
def like(request, article_pk):
    if request.is_ajax():
        ...;
        if ...:
            liked = False
        else:
            ...
            liked = True
        context = {'liked': liked, 'count': article.like_users.count(),}
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()
```

- axios를 통해 받은 ajax 요청을 JSON형식(`return JsonReponse`)으로 하였으며, 내부에 해당되는 data를 `context`에 담아 반환하였다.

## Axios 구문 처리

- 다시 `index.html`로 돌아와서.
- axios 구문의 `.then`과 `.error`는 각각 요청`request`에 대한 응답`response`를 정상적으로 받았을 경우의 처리 구문과, 아닐 경우의 에러처리 구문이다.

```javascript
// 'articles/index.html'
axios.post(`/articles/${articleId}/like/`)
        .then(response => {
          document.querySelector(`#like-count-${articleId}`).innerText = response.data.count
          if (response.data.liked) {
            event.target.style.color = 'crimson'
          } else {
            event.target.style.color = 'black'
          }
        })
        .catch(error => {
          console.log(error)
        })
```

- DOM 문법으로 HTML Tag 내부에 id 값으로 `like-count-{{ article.pk }}`을 가지는 태그의 내용('좋아요'의 개수)을 `.innerText`를 이용하여 변경할 수 있다.
- 또한 `event.target.style.color` 처럼 객체의 style을 직접 변경할 수도 있다.