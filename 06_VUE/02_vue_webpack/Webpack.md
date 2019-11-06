# Webpack

- 웹팩은 현재 가장 널리 쓰이는 번들러이다.
- JS 뿐만 아니라, CSS, IMAGE 파일 등 리소스의 의존성들도 관리한다.
- 개발을 편하게 모듈 단위 개발 => 모듈이 엄청나게 많아질수록 모듈끼리 연결(의존성)을 신경쓰기가 어려워짐 => 웹팩아 하나로 만들어줘.

**모듈 번들러**

- 웹 어플리케이션을 구성하는 자원(HTML, CSS, JS, IMG 등)을 모두 각각의 모듈로 보고 이를 조합해서 병합된 하나의 결과물로 만드는 도구

**모듈**

- 어플리케이션을 구성하는 개별적 요소
- 재사용 가능한 코드 조각
- 모듈은 세부사항을 캡슐화한다.
- 특정 기능을 갖는 작은 코드 단위
- 예) Meth 모듈안에 sum, avg, max 등의 기능을 가진 함수들이 있다.

## webpack의 구조

### entry

- 여러 js 파일들의 시작점 -> 웹팩이 파일을 읽어 들이기 시작하는 부분
- 주로 `main.js`

### module

- 웹팩은 JS만 변환 가능하기 떄문에 html, css 등은 모듈을 통해서 웹팩이 이해할 수 있도록 변환이 필요하다.
- 변환 내용을 담는 곳.

### plugins

- 웹팩을 통해서 번들된 결과물을 추가 처리하는 부분

### output

- 여러 js 파일을 하나로 만들어 낸 결과물

------

## 초기 설정

### 웹팩 설치

```bash
$ npm init # 계속 엔터쳐서 기본값으로 설정되게 한다.
$ npm install vue
$ npn i webpack webpack-cli -D
```

### webpack.config.js

- Root directory에 파일명 `webpack.config.js`로 웹팩 설정 파일 생성 및 기본 세팅

### src/main.js

- Root directory에  src 폴더와 그 안에 main.js 생성 및 기본 세팅

### src/App.vue

- `최상위 컴포넌트`
- 3개의 파트로 구성된다. template/script/style

### Vue loader / compiler 설치

- 웹팩은 js코드만 이해 가능하기 때문에 vue 파일(vue-loader) 및 html, css  파일(vue-template-compiler)등을 변환하기 위하여 모듈 설치

```bash
$ npm install vue-loader vue-template-compiler -D
```

### package.json 수정

- `"test": "echo \"Error: no test specified\" && exit 1"` 를 `"build": "webpack"`로 변경

### webpack build하기

```bash
$ npm run build
```

### public / index.html 생성 후 연결 test

```html
...
<body>
  <div id="app">
      
  </div>

  <script src="../dist/app.js"></script>
</body>
```

------

## 컴포넌트 연결

### 하위 컴포넌트 생성

-  src/components/TodoList.vue 생성
- 마찬가지로 template/script/style 3개의 구조이다.
- `script`는 `export default {}` 내부에 작성. 내부의 속성을 전달해준다는 의미

### 하위 컴포넌트 등록  3 steps

- 상위 최상위 컴포넌트(App.vue)에서 하위 컴포넌트를 연결해준다.

1. `<script>`에 등록할 컴포넌트 불러오기 (import)

   ```javascript
   import TodoList from './components/TodoList.vue'
   ```

2. `export default`에 `components`항목에 추가

   ```javascript
   export default {
       components: {
         TodoList,
       }
     }
   ```

3. `<templates>`에서 컴포넌트 사용할 수 있도록 작성

   ```html
   <div>
       <h1>여기는 최상위 컴포넌트입니다.</h1>
       <todo-list category="취업특강"></todo-list>
       <todo-list category="SSAFY"></todo-list>
       <todo-list category="기타"></todo-list>
   </div>
   ```

   

### css loader 설치

- 다시 npm run build하면 에러가 뜸
- vue는 js 밖에 못 읽으므로, css를 처리하기 위한 모듈이 필요하다.

```bash
$ npm install vue-style-loader css-loader -D
```

- 설치 후 `webpack.config.js` 모듈을 등록 후 build 한다.

```javascript
// webpack.config.js
...
module: {
    rules: [
      {
        test: /\.vue$/, 
        use: 'vue-loader',
      },
      {
        test: /\.css$/,
        use: ['vue-style-loader', 'css-loader']
      }
    ]
  },
      ...
```

------

- 위의 과정은 너무 복잡하다.
- 그래서 이미 편리하게 webpack을 구성해주고 vue 프로젝트를 만들 수 있는 vue 프레임 워크가 있다.
- Vue CLI에 대해 배워보자.