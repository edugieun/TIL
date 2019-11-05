# VUE(뷰)

## Vue란?

- Vue는 JavaScript의 프레임워크이다. (복잡한 코딩 구조나 내용을 미리 규격화 / 모듈화 해둔 도구)
- MVVM 디자인 패턴을 사용한다.

### MVVM 란

- 디자인 패턴이란, 코드를 효율적으로 관리하기 위해 코드의 역할을 나누는 방법을 의미한다.
- 디자인 패턴에는 MVC, MVP, MVVM 등이 있다.
-  https://blog.outsider.ne.kr/672 
-  https://wikidocs.net/17701 
-  https://beomy.tistory.com/43 
-  https://wit.nts-corp.com/2019/02/14/5522 
-  http://jeonghwan-kim.github.io/vue/2017/03/27/vue.html 

## SPA (Single Page Application)

- 페이지 전환이 없다.
- URL 변화가 없다.

장고와 차이라면 장고는 서버까지 관리하는 풀스택 / 뷰는 프론트 쪽에 가깝다.

------

## 뷰 인스턴스의 속성

- 인스턴스의 속성 값들은 정해진 이름이므로, 다르게 명명해서는 안된다.

### el

- Vue 인스턴스와 DOM 을 연결(마운트, mount) 하는 옵션
- View 와 View Model을 연결 시킨다.
- HTML의 id나 class와 마운트가 가능하다.

### data

- Vue 인스턴스의 데이터 객체 또는 인스턴스의 `속성`이라고 부름
- 데이터 객체는 반드시 기본 객체 '{  }'여야 한다.
- 객체 내부의 아이템들은 value로써 모든 타입의 객체를 가질 수 있다. (object, string, integer, array...)
- 정의된 속성은 인터폴레이션(`{{  }}`) 을 통해서 View에서 렌더링 가능
- data에서도 이벤트리스너와 비슷한 이유로 화살표 함수를 작성해서는 안된다.

### methods

- Vue 인스턴스에 추가할 메소드들을 정의하는 곳
- (주의) 메소드를 정의하는데에 화살표함수를 사용해선 안된다.

### computed

- 미리 계산된 값을 반환. (methods는 호출될 때마다 계산한다.)
  - 따라서, methods는 매번 함수처럼 호출해야 하고, 매번 새로 계산된다.
  - 반면 computed 최초 선언시 한번만 계산되고 그 값이 고정되어 있는 변수처럼 사용된다. 따라서, 소괄호`()` 없이 변수 호출처럼 사용한다.
- 종속 대상을 따라 저장(캐싱)되는 특성이 있다.
- 연산이 많이 필요한 경우 템플릿 안에서 연산 표현식을 사용하는 것보다 computed를 사용하는 것을 권장.
- 예) `{{ newTodo.split('').reverse().join('') }}` 이렇게 태그안에 수식을 직접 넣지 말고 아래처럼 JavaScript에서 함수로 만들어 사용한다.

```vue
computed: {
	reversedNewTod: function() {
		return this.newTodo.split('').reverse().join('')
	}
}
```

### watch

- Vue 인스턴스의 data 변경을 관찰하고 이에 반응
- 데이터 변경에 대한 응답으로 비동기 또는 시간이 많이 소요되는 조작을 수행하려는 경우에 적합
- 특정 데이터가 변경되었을 때 정의한 함수를 실행
- 기본적으로 data 속성을 바라보고 있다.
  - 예) data 속성에 변화가 있으면 -> 저장 함수를 실행

#### computed vs watch

- computed: 계산해야 하는 `목표 데이터를 정의하는 방식` (선언형 프로그래밍)
- watch: 감시할 데이터를 지정하고 그 `데이터가 바뀌면 특정 함수를 실행하라는 방식` (명령형 프로그래밍)

### mounted

- 새로고침될 때(DOM과 Vue instance가 연결되는 시점) 실행되는 속성
- 새로고침할 때 최초의 데이터가 아닌 local Storage에 있는 데이터를 가져오는 것.

------

## Vue directive(디렉티브, 지시문)

- 디렉티브는 `v-` 접두사가 있는 특수 속성(attr)이며, 디렉티브 속성의 값은 단일 JS 표현식

### v-for

### v-if / v-else

- 특정 조건을 만족할때만 보여지도록(렌더링되도록)할 수 있다.
- `v-else`는 반드시 `v-if` 엘리먼트 바로 뒤에 와야 인식 가능하다.
- `v-else-if`도 존재.

우선순위

- 동일한 노드에서는 for가 if 보다 높은 우선순위를 가짐
- 즉, v-if는 루프가 반복될때마다 실행! (일부 항목만 렌더링 할 때 유용)

### v-on

- JS에서 이벤트리스터와 비슷한 역할을 한다.
- 이벤트 리스너는 HTML element를 querySelector로 가져와 이벤트를 붙여줬다면, Vue는 HTML element 자체에 이벤트를 붙여준다.
- `v-on:` 뒤에 오는 속성을 `전달인자`라고 한다.
- `:`을 붙여 사용하는 디렉티브 바로 뒤에 붙는 친구들을 지칭한다.

#### v-on 사용법 2가지

- `inline 방식`
- `method 정의`
- shortcut => `@`

### v-bind

- HTML element의 속성 값을 변경할 때 사용
- shortcut => `:`

### v-model

- input tag의 value: View <---> v-model <---> data(VM, ViewModel)
- 서로가 연동되도록 해준다.

## Optional  directive

### v-text

- 인터폴레이션 없이 바로 출력

### v-html

- html 태그가 포함된 문자열을 출력할 때 태그가 적용되게 출력

### v-if / v-show

- v-if: 조건에 맞지 않으면 렌더링 자체를 하지 않음
- v-show: 조건과 관계 없이 일단 렌더링 후에, 조건에 맞이 않으면 CSS display 속성을 토글해서 숨겨버림

## Console 접근

```console
// 속성 접근은 $ 를 붙여서 접근한다.
app.$el
app.$el.firstChild
app.$el.firstChild.innerText = 'ssafy'
```

