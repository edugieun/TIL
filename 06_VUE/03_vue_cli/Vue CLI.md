# Vue CLI

- Vue-CLI는 Vue Commend Line Interface의 약자이며, 이름 그대로 Vue 프로젝트를 터미널의 커맨드 라인 명령을 통하여 쉽고 편하게 기본 vue 프로젝트 개발 환경을 제공해주는 도구이다.
- Vue-CLI는 내부적으로 Webpack을 활용하기 때문에, webpack 또한 자동으로 만들어주고 그에 대한 기본 세팅을 해준다.

## Vue CLI 설치 및 세팅

- 먼저 vue cli를 설치한다.

```bash
$ npm i -g @vue/cli
```

- vue 프로젝트를 생성한 후 서버가 열리는지 확인한다.

```bash
$ vue create todo-vue-cli
$ cd todo-vue-cli
$ npm run serve
```

- 프로젝트를 생성하니, 웹팩을 직접 작성했을 때 만들었던 `webpack.config.js`가 보이지 않는다.
- 이는 3.x 버전부터는 노출되지 않고 @vue/cli-service에 의해 자동으로 로드되는 선택적 구성파일로 변경 되었다.
- 추가적으로 webpack에 대한 설정을 변경하기 위해서는 `webpack.config.js`가 아닌 `vue.config.js`라는 이름으로 루트 디렉토리에 만들어서 작성해야한다.

## 컴포넌트 연결

- 이제부터 CLI을 쓰기 전과 동일한 과정으로 하위 컴포넌트를 만들고 상위 컴포넌트와 연결시키면 된다.

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

   