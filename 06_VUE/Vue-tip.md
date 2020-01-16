# Vue Tip

## npm shrinkwrap

- `pip freeze > requirements.txt`와 같은 역할을 하며, `npm-shrinkwrap.json`이라는 파일을 생성한다.
- `npm install` 명령어 사용시 원래는 `package.json`의 명세를 따라 `node_module`을 설치하지만, `npm-shrinkwrap.json` 파일이 존재하면 `npm-shrinkwrap.json` 파일의 명세를 따라 설치한다.

## Troubleshooting

### npm install Error

- node_moudles 를 설치하기 위해 `npm install` 진행 시 다음과 같은 에러 발생

![image](https://user-images.githubusercontent.com/52814897/70999112-1a2a4480-211c-11ea-8cfc-10b4596e938d.png)

- `npm cache clean --force` 명령어로 캐시를 지운 후 재설치한다.

## Favicon 변경하기

- `/public/index.html ` 파일에서 favicon을 나타내는 코드는 다음의 코드이다.

```html
<link rel="icon" href="<%= BASE_URL %>favicon.ico">
```

- 기존의 public 폴더에 있는 `favicon.ico` 파일을 다른 사진으로 대체해보고, static 폴더를 만들어 넣어보기도 했지만 적용이 되지 않았고, 기존의 favicon 파일을 지워도 그대로 기존의 favicon이 적용되어 있는 것을 보고, favicon 정보가 다른 곳에 저장되어 있는 것으로 보인다.

- 그곳은 바로 아래 `/public/img/icons` 경로이며 `favicon-16x16 / 32x32` 형태로 저장되어 있다.

  ❓ 보통 image 파일들은 static이나 src에 따로 저장할텐데, 왜 `img/icons` 폴더에 저장되어 있을까?

![image](https://user-images.githubusercontent.com/52814897/72437960-3555a600-37e7-11ea-8007-ec8f52c118d9.png)

- 이 파일들을 지워주고 원하는 favicon이 있는 경로를 설정해준다.

```html
<link rel=icon href=/favicon.ico>
```

## 라인 개수 제한(Line clamp)

### CSS로 자르기

- 글 제목처럼 글을 너비에 따라 한 줄로만 자를 때 사용한다.

```html
<div style="text-overflow:ellipsis; white-space:nowrap; width:200px; overflow:hidden;">{{title}}</div>
```

### vue-clamp 사용하기

- `vue-clamp`라는 라이브러리를 사용하여 라인 개수를 제한하는 방법이다. 공식 홈페이지를 참조하자.
- [공식 홈페이지](https://justineo.github.io/vue-clamp/demo/)

# Firebase와 Vue 연동하기

## npm install error

![image](https://user-images.githubusercontent.com/52814897/72228681-50a89180-35ec-11ea-8a75-dd991b756216.png)

- node_module과 package-lock.json을 지운 후 다시 진행

## Firebase + vue 배포

- npm install -g firebase-tools 설치먼저하고
- 프로젝트 추가
- 앱(web) 추가
- 아래처럼 스크립트를 body에 추가하라는 문구가 뜨면 /public/index.html 의 body안에 추가한다.

![image](https://user-images.githubusercontent.com/52814897/72230050-6f138a80-35f6-11ea-995b-58fd1eb21751.png)

- `.firebaserc` 에 `default`를 firebase `프로젝트 ID` 이름으로 변경한다.

![image](https://user-images.githubusercontent.com/52814897/72230265-8ef77e00-35f7-11ea-9b20-1c73cc3cb163.png)

![image](https://user-images.githubusercontent.com/52814897/72233146-d9cdc180-3608-11ea-9344-c6e856a3d273.png)

- npm run build
- firebase login
- firebase init. (이 부분을 해야하는지 안해도 되는지 애매함. 일단 안해도 db까지 잘 동작하긴 함. 일단 하지 않고 진행한다.)
- firebase deploy

## Database 연동

- Database를 연동하기 위해서는 configuration을 변경해준다.
- 아래처럼 SDK snippet에서 자신의 `firebaseConfig`를 가져와 /src/services/FirebaseService.js 에 있는 firebaseConfig를 수정해준다.

![image](https://user-images.githubusercontent.com/52814897/72230478-10034500-35f9-11ea-9de5-9e82596950e3.png)

- build, deploy하고 에러 뜬다면 아래처럼 cloud resource 지역을 설정해준다.

![image](https://user-images.githubusercontent.com/52814897/72230772-07137300-35fb-11ea-96ab-a6de7fee1708.png)

- Firebase 홈페이지에서 Database 탭을 들어간다.
- 컬렉션을 추가 해준 후,

![image](https://user-images.githubusercontent.com/52814897/72233010-1f3dbf00-3608-11ea-9230-1debb5367021.png)

- 규칙 탭에서 false를 true로 변경해준다.

![image](https://user-images.githubusercontent.com/52814897/72233025-367cac80-3608-11ea-892a-cdad7fb0e47b.png)

