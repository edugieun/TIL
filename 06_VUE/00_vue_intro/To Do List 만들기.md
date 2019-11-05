# Vue 활용하기 - To Do List 만들기

## Vue CDN 가져오기

- Vue를 사용하기 위하여 HTML body에 CDN을 추가해준다.
-  https://kr.vuejs.org/v2/guide/installation.html#CDN 

```html
...
<body>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</body>
```

## 기본 구조

- Vue

- 새 할일 추가하기
- 완료목록 안보이게 하기
- 드랍박스 만들기(분기시키기)
- style 꾸미기
- localStorage 활용하기
  - View와 VM을 하다가 localstorage를 위하여 Model을 활용하는 과정이다.
  - 명령어
    - getItem(key)
    - setItem(key, value)
    - removeItem(key)