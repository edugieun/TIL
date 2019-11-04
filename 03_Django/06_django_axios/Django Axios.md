# Django Axios



> 비동기식 자바스크립트 활용하기 (Ajex)
>
> 좋아요를 눌렀을 때 새로고침되지 않고, 바로 반영되게 하기

## XMLHttpRequest(XHR)

- 브라우저는 XMLHttpRequest 객체를 이용하여 Ajex 요청을 생성하고 전송
- 서버가 브라우저의 요청에 대해 응답을 반환하면 같은 XHR 객체가 그 결과를 처리
- 단 IE 5, 6에서는 ActiveXobject를 사용해야 한다.

Axios CDN 추가

```django
<!-- articles/base.html -->
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

_article.html a태그 삭제 및 수정

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

- `like-button`:  `DOM`객체로 접근하기 위한 클래스를 하나 정해준다.
- `data-`: `data-*속성`은 HTML에 정보를 바로 저장할 수 있도록 해준다.
- `like-count-{{ article.pk }}`: 역시 `DOM` 문법으로 접근하기 위해 지정해주는 id값이다.

index.html axios 요청 작성

- `DOM` 조작으로 `class`가 `.like-button`인 객체를 모두 불러온 후
- 각각의 객체 `이벤트리스너`를 추가해준다.
- `conslo.log(event)`를 이용하여 `article_pk`의 위치를 확인하여 가져온다.

```javascript
// 'articles/index.html'
const likebuttons = document.querySelectorAll('.like-button')
likebuttons.forEach(button => {
button.addEventListener('click', function (event) {
    const articleId = event.target.dataset.id
```

- 좋아요를 `click`했을 때 `axios`로 요청을 보낸다.
  - 만약, POST 방식으로 보내고 싶을 경우 아래와 같은 3가지 설정이 필요하다.

```javascript
// POST 방식으로 보낼 시.
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

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

- `/articles/${articleId}/like/`가 가르키는 view 함수로 요청을 보낸 후, `response`로 응답을 받는다.



view/like 수정 *from* django.http *import* JsonResponse,

- 기존 redirect로인해 index.html로 페이지가 로딩되는 것이 아닌, JSON 형태로 응답 결과를 반환 받기로 변경하는 것
- JSON 데이터에 liked 변수를 만들어서 templates에서 좋아요를 취소할지 추가할지를 판단할 수 있도록 한다.
- 그래서 True / False 값을 통해 좋아요 버튼의 style 값을 변경한다.