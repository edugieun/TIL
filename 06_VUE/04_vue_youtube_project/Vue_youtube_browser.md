# Vue - Youtube Browser 화면 구성하기

## 컴포넌트 구성도

![image](https://user-images.githubusercontent.com/52814897/68566626-380be600-049a-11ea-88dd-99c4bb3a6e77.png)

## 데이터 흐름도

- 단방향 데이터 흐름의 이점
  - vue.app의 데이터 흐름을 쉽게 파악할 수 있음
  - 부모 컴포넌트에서 업데이트가 일어나면 자식컴포넌트는 자동 업데이트(즉, 자식 컴포넌트의 상태를 관리하지 않아도 된다.)
  - 하위 컴포넌트가 실수로 부모의 상태를 변경하여 app 데이터의 흐름을 추론하기 어렵게 만드는 것을 방지할 수 있다.
- `props`는 배역, 객체, 함수 등 무엇이든 내려보내는 `속성(properties)`이고, `emit event`는 자식에서 부모로 `이벤트를 발생`시키는 것

![image](https://user-images.githubusercontent.com/52814897/68566644-46f29880-049a-11ea-8ca2-afad58f1c810.png)

## 개발환경 구성

- Vue-CLI는 기본적으로 배포 설정이기 때문에 `console.log()`를 사용못하게 막아 놓는다.(내부 정보가 찍힐 수 있으니까). 따라서 배포 전 개발 단계에서는 console을 사용할 수 있게 `no-console`을 설정해준다. 

```json
// package.json
"eslintConfig": {
    ...
    "rules": {
      "no-console": "off"
    },
    ...
```

## 검색기능 구성

- SearchBar 컴포넌트에서 검색을 위한 input 태그를 만든다.
  - `v-on`속성 `input` - input란의 글자가 바뀔때마다 동작 / `change` - enter를 치면 동작

```html
<input @input="onInput" type="text">
```

### 상위로 이벤트 보내기 (emit)

- 상위로 데이터를 올려 보낼 때는 Event를 발생시키는 방법을 사용한다. => `emit`
- `emit('eventName', value)`을 통해 상위 컴포넌트로 검색어를 올려준다.

```javascript
methods: {
      onInput(e) {
        this.$emit('inputChange', e.target.value)
      }
    }
```

- 사용자가 input 에 값을 입력하면 onInput 함수가 실행
- inputChange 이벤트와 사용자가 입력한 인자(value)가 함께 상위 컴포넌트인 App.vue로 emit 된다.

### 상위에서 이벤트 받기

- App.vue 컴포넌트에 SearchBar에서 보낸 이벤트 `inputChange`를 받고, `inputChange` 이벤트를 받았을 경우 `onInputChange` 메소드를 실행한다.

```html
<search-bar @inputChange="onInputChange"></search-bar>
```

- onInputChange 메소드는 SearchBar 컴포넌트에서 보내준 인자(검색어, inputValue)를 가지며, axios를 이용하여 유튜브 api에 요청을 보내고 비디오 리스트를 응답 받는다.
- 이 때, `params` 속성에 요청에 필요한 조건들을 함께 보낸다.

```javascript
methods: {
    onInputChange(inputValue) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      })
      .then(response => {
        this.videos = response.data.items
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
```

- 요청을 통해 받은 응답(response)를 data에 저장한다.
  - Youtube가 보내주는 데이터가 길이 5의 배열 형태이므로 배열에 저장

```javascript
data() { // 또는 data: function () { 처럼 작성해도 됨.
      return {
        videos: [],
        selectedVideo: null,
      }
  }

```

- `data`는 Vue component 에서는 반드시 Object를 return 하는 함수로 작성.
  - data의 return을 한번더 객체로 감싸줘야 독립적인 return value를 가질 수 있다. (장고의 name space처럼 이해)
- SearchBar => App 흐름
  1. 트리거 : input 값 변경(@input)
     - 인자: event
     - 실행 함수: onInput
  2. 트리거: input 내 $emit(inputChange)
     - 인자: 변경된 값
     - 실행 함수: onInputChange

## 동영상 목록 띄우기

- App에서 저장한 videos를 VideoList 컴포넌트가 참조할 수 있게 바인딩(binding) 해준다.

```html
<video-list :videos="videos"></video-list>
```

- VideoList 컴포넌트의 상위 컴포넌트(App.vue)가 바인딩 해준 변수를 사용할 수 있도록 `props` 속성을 이용하여 변수를 선언한다.

```javascript
props: {
      videos: {
        type: Array,
        required: true,
      }
}
```

- VideoList에서 각각의 동영상(video)을 VideoListItem 컴포넌트로 보내주고(binding), VideoListItem에서는 보여질 각각의 video 정보를 정할 것이다.
  - `v-for`를 사용할 경우 구분할 수 있는 `key`값도 같이 바인딩 해줘야 한다.

```html
<ul>
    <video-list-item
		v-for="video in videos"
		:key="video.etag"
		:video="video"
        >
    </video-list-item>
</ul>
```

- VideoListItem 컴포넌트의 상위 컴포넌트(VideoList)가 바인딩 해준 변수를 사용할 수 있도록 `props` 속성을 이용하여 변수를 선언한다.

```javascript
props: {
      video: {
        type: Object,
        required: true,
      },
}
```

- 이제 보여줄 정보를 띄워 준다.
- `v-html`: 특수문자가 깨지지 않고 그대로 나오도록 encoding 해준다.

```html
<li>
    <img :src="thumbnailUrl" alt="img">
    <p v-html="video.snippet.title"></p>
</li>
```

- `thumbnailUrl`은 `computed` 속성을 이용하여 간소화된 변수이다.

```javascript
computed: {
      thumbnailUrl() {
        return this.video.snippet.thumbnails.default.url
      }
}
```

## 동영상 선택 및 재생

- 상단의 `데이터 흐름도`와 같이 VideoListItem 컴포넌트에서 video 데이터를 VideoListItem->VideoList->App->VideoDetail의 흐름으로 이동시키려고 한다.
- 변수가 많아지면 복잡하기 때문에 2개의 변수(videoSelect, onVideoSelect)로 돌려가면서 전달, 전달한다.
- 최하위 컴포넌트인 `VideoListItem`에서 해당 동영상을 클릭 이벤트가`@click` 발생하면,

```html
<li @click="onVideoSelect">
    ...
</li>
```

- `onVideoSelect` 메소드가 실행되도록 한고, `emit`을 통해 상위 컴포넌트(VideoList)로 보내준다.


```javascript
methods: {
      onVideoSelect() {
        this.$emit('videoSelect', this.video)
      }
},
```

- VideoList 컴포넌트에서는 VideoListItem 컴포넌트의 `onVideoSelect`메소드가 실행될 때 발생하는 `videoSelect`이벤트를 인식할 수 있게 수정한다.

```html
<ul>
    <video-list-item
		v-for="video in videos"
		:key="video.etag"
		:video="video"
		@videoSelect="onVideoSelect"
        >
    </video-list-item>
</ul>
```

- VideoList 컴포넌트에서 `@videoSelect` 이벤트가 발생하면 `onVideoSelect` 메소드를 실행한다.

```javascript
 methods: {
      onVideoSelect(video) {
        this.$emit('videoSelect', video)
      },
}
```

- 마찬가지로, `onVideoSelect` 메소드는 `emit`를 이용하여 상위 컴포넌트(App.vue)로 이벤트와 값을 보내주고, App.vue는 이벤트를 받고, 메소드를 실행하도록 수정한다.

```html
<video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
```

```javascript
methods: {
    ...
    onVideoSelect(video) {
      this.selectedVideo = video
    },
```

- VideoListItem부터 가져온 데이터 video를 `selectedVideo`변수에 담는다.
- 이 때, 어떤 동영상을 선택하기 전의 상태는 변수에 아무값도 없으므로 null로 초기화 해준다.

```javascript
data: function () {
      return {
        ...
        selectedVideo: null,
      }
  },
```

- App 컴포넌트에서 `selectedVideo`에 저장된 데이터를 VideoDetail 컴포넌트에 바인딩해준다. 이 때, 바인딩변수(`:video`)가 하위 컴포넌트에서 쓰일 변수명이다.

```html
<video-detail :video="selectedVideo"></video-detail>
```

- 상위 컴포넌트에서 바인딩하여 받은 데이터를 VideoDetail 컴포넌트에서 props로 저장한다.

```javascript
props: {
      video: {
        type: Object,
      }
},
```

- video가 null 값일 경우 보여주거나 불러올 데이터가 없어 에러가 발생하므로, `v-if`으로 에러를 피한다.

```html
<div v-if="video" class="col-lg-8">
    <div>
      <iframe :src="videoUrl"></iframe>
    </div>
    <div class="details">
      <h4 v-html="video.snippet.title"></h4>
      <p>{{ video.snippet.description }}</p>
    </div>
</div>
```

- `iframe`은 동영상을 보여줄 때 사용하는 HTML 태그이다. 웹 문서 내부에 또 다른 웹 문서나 이미지, 동영상 등을 보여줄 때 사용한다.
- `videoUrl`은 변수명을 줄이기 위한 computed 함수이다.

```javascript
computed: {
      videoUrl() {
        const videoId = this.video.id.videoId
        return `http://www.youtube.com/embed/${videoId}`
      }
    }
```






- 값이 없을 수도 있으니 null로  초기화하고, if문으로 값이 있을 경우만 처리하여 error가 안뜨게 한다.



- 유튜브 API Key 발급받기
- axios 설치 `npm i axios` 및 등록

```javascript
import axios from 'axios'
```





.env.local 파일에 key 넣기

- 반드시 `VUE_APP_`으로 시작해야 한다

```
VUE_APP_YOUTUBE_API_KEY=AIza**
```

- 키 불러오기

```javascript
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
```

여까지 SearchBar

-------

## 다시 최상위 App.vue

- 넘겨 받은 비디오 리스트를 videos라는 배열에 저장한다.

```javascript
data() {
      return {
        videos: [],
      }
  },
methods: {
    onInputChange(inputValue) {
      axios.get(API_URL, {
        ...;
      })
      .then(response => {
        this.videos = response.data.items
      })
```



- - 
- `data` object가 (videos 배열이 있는 곳) 업데이트 되면, 해당 컴포넌트 (App.vue)가 템플릿을 다시 렌더링 한다.
- 그리고 바로 자식 컴포넌트들도 모두 다시 렌더링 된다.
- `VideoList`컴포넌트가 비디오 배열을 받아 화면에 보여주게 된다.



bootstrap 넣는 위치: public/index.html

개인 컴포넌트 스타일 먹이기 : `scoped` 속성 사용

```html
<style scoped>...</style>
```

------

- 배열  videos를 `VideoList` 컴포넌트에 보낸다

```html
<video-list :videos="videos"></video-list>
```

- VideoList에서는 상위 컴포넌트를 받기 위해 `probs`속성을 사용하여 선언한다.

```javascript
props: {
    videos: {
      type: Array,
      required: true,
    }
  }
```

...

- 