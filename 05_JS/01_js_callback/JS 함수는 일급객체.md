# JS 함수는 일급객체

1. 변수에 담을 수 있다.
2. 인자로 전달할 수 있다.
3. 반환값으로 전달할 수 있다.
   - 함수가 return 값이 될 수 있다. ex) return x => x+1

# 비동기식 처리 모델

- 호출된 함수 (콜백함수)를 미리 매개변수에 전달하고 처리가 종료되면 콜백함수를 호출 하는 것.

# 이벤트 리스너

1. 무엇을 (버튼을) - EventTatget
2. 언제 (클릭했을 때) - Type
3. 어떻게 (콘솔에 로그를) - Listener
4. 한다.

## Function this vs Arrow Function this

- 차이점?
  - Function의 this는 현재 함수가 있는 곳의 스코프
    - 단, 함수 내 함수에 쓰인 this는 무조건 전역객체(window)를 가리킨다.
    - 더글라스 크록포드가 언어 설계상의 오류라고 지적할 만큼 이상한 부분이니 이해하려고 하지 말자.
  - Arrow Function의 this는 현재 함수가 있는 곳의 객체의 상위 스코프
- 이벤트 리스너에서 Arrow Function을 사용하면 안되는 이유는? 
  - `객체.addEventListener()`와 같은 내장함수는 이미 객체를 가르키고 있다.
  - 이 상태에서 콜백함수를 arrow function으로 선언하면 `this`를 사용했을 때 `this`가 가를 키는 건 객체가 아닌 객체의 상위 객체. 즉, 전역객체(window)를 가르키게 된다.

# JS 코드를 body의 최하단에 위치하는 이유

1. JS를 읽는 시간 때문에 BODY안에 있는 HTML 요소들이 브라우저에 그려지는게 지연 될 수 있기 때문.
2. JS에서 특정 HTML 요소들을 읽고 이벤트를 등록해야 할 때, JS 코드가 먼저 해석되면 해당 요소가 없다고 인식되어 이벤트 등록이 되자 않을 수 있기 때문.

`querySelector`

querySelector는 위에서 선택자로 요소를 찾으며 가장 먼저 찾아지는 요소를 반환(단수)

`querySelectorAll`

querySelector는 위에서 선택자로 요소를 찾으며 일치하는 요소들을 모두 반환(복수)