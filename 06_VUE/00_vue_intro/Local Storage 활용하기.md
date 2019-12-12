# Local Storage 활용하기

> `02-2_vue_todo_app_ad.html`

- HTML을 이용하여 Todo List를 만들었을 때, 새로고침을 하면 list에 추가한 내용들이 다시 리셋된다.
- Local Storage는 일정 기간 동안 데이터를 web browser에 저장한다.

## 사용방법

- 먼저 local storage에 저장될 key 이름을 정해준다.

```javascript
const STORAGE_KEY = 'vue-todos'
```

- storage에서 실행될 메서드를 선언해준다.
  - (JS) JSON.parse는 `'{"result":true, "count":42}'`와 같이 단순 문자열로 되어있는 객체구조를 진짜 객체 구조로 만들어 key, value 값에 접근할 수 있게 만들어 준다.
  - (DOM) `localStorage.setItem()`으로 저장하고, `localStorage.getItem()`으로 조회한다.

```javascript
const todoStorage = {
  fetch: function () {
    // parse: String -> JSON
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]') // 없다면 빈 배열로 선언
  },
  save: function (todos) {
    // stringify: JSON -> String
    localStorage.setItem(STORAGE_KEY, JSON.stringify(todos))
  }
}
```

- Vue의 mounted 속성을 이용하여 HTML 템플릿 렌더링 직후, Web의 Local Storage에 앞서 선언한 빈 리스트의 storage가 생성되도록 한다.

```javascript
mounted: function() {
  this.todos = todoStorage.fetch()
},
```

- Vue의 watch 속성을 이용하여 새로운 todo list 항목이 생성될 때마다 Vue 인스턴스의 data 변화를 감지한다.

```javascript
watch: {
  todos: {
    // handler: 특정 데이터가 변경되었을 때 실행할 함수
    handler: function(todos) {

      todoStorage.save(todos)
    },
      // deep속성: 객체의 nested item 들도 관찰할지 유무를 설정. true인 경우 내부 요소들도 감시.
      deep: true,
  }
  },
```

- 아래 사진과 같이 Local Storage에 새로운 키가 생겼음을 확인할 수 있다.

![image](https://user-images.githubusercontent.com/52814897/69915577-fcaa7900-1493-11ea-919b-dbe08ca9c320.png)