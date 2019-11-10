# 동기식 처리 모델 (Synchronous)

- Blocking
- 직렬적으로 task를 수행
- 즉, task는 순차적으로 실행되며 어떤 작업이 수행중이면 다음 작업은 대기
- 예) 서버에서 데이터를 가져와서 화면에 표시하는 작업을 수행할 때, 데이터가 응답될 때까지 이후 task들은 블로킹(blocking)된다.
- Python 또한 동기식 프로그래밍 언어이다.

# 비동기 처리 모델 (Asynchronous)

- Non-Blocking
- 병렬적으로 task를 수행
- task가 종료되지 않은 상태라 하더라도 대기하지 않고 다음 task를 실행
- 예) 서버에서 데이터를 가져와서 화면에 표시하는 작업을 수행할 때, 데이터가 응답될 때까지 기다리지 않고(non-blocking) 즉시 다음 task를 실행
- JS 대부분의 DOM 이벤트와 Timer 함수, Ajax 요청은 비동기식 처리 모델로 동작

------

# 이벤트 루프

![image](https://user-images.githubusercontent.com/52814897/68541312-51049080-03e1-11ea-8f18-dc44420a739a.png)[출처 -  http://latentflip.com/loupe ]

- 단 한가지의 역할, **콜스택**과 **콜백큐**를 감시하는 역할만 한다.

- 만약 콜스택이 **비어 있으면**(반드시 비어있어야 한다.) 이벤트 루프(감시, 관리 역할)는 콜백큐에서 첫 번째 이벤트를 가져다가 콜스택에 밀어 넣고, 결과적으로 해당 이벤트가 실행된다.

- 이러한 반복은 이벤트 루프에서는 `tick`이라고 한다.

- 이벤트 루프는 호스팅 환경(브라우저 or nodejs 서버)에 내장된 메커니즘. (JS 엔진에 있는게 아니다.)

- 이것은 시간의 흐름에 따라 코드의 수행을 처리하며 그때마다 JS 엔진을 작동 시킨다.

  

`setTimeout(mycallback, msecs)`

- callback함수가 'msec 후에 실행될 것이다' 라는 의미가 아닌, Web APIs에 msec 동안 머물러 있다가 **콜백 큐**에 **'msec 후에 추가될 것이다'**라는 의미이다.
- 만약에 콜백 큐에 mycallback보다 먼저 추가된 이벤트가 있을 수도 있기 때문에, 실제 msec보다 더 오랜시간이 걸릴 수도 있다.

------

# Axios

- `axiosXHR`을 요청(request)으로 보내고 응답 받은 결과를 `Promise 객체` 반환(response) 해주는 라이브러리
- axios는 현재 JS에서 가장 HOT한 라이브러리 중 하나이며, 프론트엔드 프레임워크(react, vue) 에서 데이터를 주고 받을 때 필수적으로 사용되고 있음. (프론트엔트 프레임워크 <-> api 서버)
- 장고에서는 axios를 CDN 방식으로 사용했었는데, HTML 없이 순수 `.js` 파일에서 사용할 때는 npm 설치 후 사용 가능하다.
-  [출처 - https://github.com/axios/axios]

```bash
npm install axios
```

```javascript
// 1. axios 설치해서 사용하기
const axios = require('axios')
axios.get('http://jsonplaceholder.typicode.com/posts')
  .then(response => {
    console.log(response)
  })
  .catch(err => {
    console.log(err)
  })
```

