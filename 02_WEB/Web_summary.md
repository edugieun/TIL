Web Summary

## HTML

### 정의

- Hyper Text Markup Language
- Hyper Text: 기존의 선형적인 텍스트가 아닌 Hyper Link를 통하여 텍스트를 이동, 비선형적으로 이루어진 텍스트
- Markup: 웹 브라우저에 표시되는 글, 이미지 등의 다양한 컨텐츠를 표시하기 위한 문법
- Language: 웹 페이지를 작성하기 위한 역할 표시 언어
- 표준 : W3C(HTML5) / WHATWG(HTML Living Standard)

### HTML 문서의 기본 구조

```html
<!DOCTYPE html> <!-- DOCTYPE 선언부/사용하는 문서의 종류를 선언-->
<html lang="ko"> <!-- html 요소 / 문서의 root이며 head와 body로 구분 -->
<head> <!--head 요소 / 문서 제목, 문자코드(인코딩)와 같이 문서 정보.
		브라우저에 나타나지 않음. CSS 선언, 외부로딩 파일 지정-->
    <meta charset="UTF-8">
    <title>Document</title>
    </head>
<body> <!-- body 요소 / 브라우저 화면에 나타나는 실제 내용-->
    
</body>
</html>
```

#### Tag와 DOM TREE (Document Object Model)

- 주석(Comment)

  - `<!-- 주석 내용 -->`

- 요소(Element)

  - `<h1> contents </h1>`
  - `<img src="url"/>` (Self-closing element)

- 속성(Attribute)

  - `<a href(속성명)="https://google.com(속성값)"></a>` 
  - 공백(`" "`) 사용 No!

- DOM 트리

  - Indent는 Tab(2 space)

  ```html
  <body> <!-- body태그와 h1태그는 부모(parent)-자식(child) 관계-->
      <h1> 웹문서 </h1> <!-- h1태그와 ul태그는 형제관계(sibling) -->
      <ul>
          <li>HTML</li>
          <li>CSS</li>
      </ul>
  </body>
  ```

- 시맨틱 태그(Semantic Tag)
  - 의미 있는 정보의 그룹을 태그로 표현. 의미를 가지는 태그들을 활용하기 위한 노력
  - 탄생 배경과 기능
    -  HTML5 이전에는 `<div>` 태그 안에 id나 class 속성으로 각자 이름을 지정하였기 때문에 컨텐츠를 분석, 식별하기가 어려웠음. 하지만, 의미를 가지는 시맨틱 태그로 검색 엔진이 더 정확한 검색 결과를 빠르게 처리 가능
  - header / nav / aside / section / article / footer / strong (=bold) / em (=i)
- Non-semantic 요소
  
  - div / span 등

#### project

- Table

  - ![image](https://user-images.githubusercontent.com/52814897/62835549-bdfa7400-bc94-11e9-9be6-0e73ebd4704e.png)

  - ```html
    <head>
      <style>
        td {
          border: 1px solid darkgray
        }
      </style>
    </head>
    
    <body>
      <table summary="락 페스티벌 시간표이며 내부 소극장, 외부 잔디마당과 대공장 총 3곳에서 10시부터 17시까지 공연하는 시간표입니다.">
        <caption>
          <h1>2019 타임테이블</h1>
        </caption>
        <thead>
          <tr>
            <th>TIME</th>
            <th>INDOOR</th>
            <th colspan="2">OUTDOOR</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td></td>
            <td>소극장</td>
            <td>잔디마당</td>
            <td>대공연장</td>
          </tr>
    
          <tr>
            <td>10:00</td>
            <td rowspan="2">안녕하신가영</td>
            <td></td>
            <td>10CM</td>
          </tr>
    
          <tr>
            <td>13:00</td>
            <td rowspan="2">선우정아</td>
            <td rowspan="2">참깨와 솜사탕</td>
          </tr>
    
          <tr>
            <td>15:00</td>
            <td></td>
          </tr>
    
          <tr>
            <td>17:00</td>
            <td>크러쉬</td>
            <td></td>
            <td>폴킴</td>
          </tr>
        </tbody>
      </table>
    </body>
    ```

- Form

  - ![image](https://user-images.githubusercontent.com/52814897/62833551-a2cf3a80-bc7b-11e9-988d-cc717eefe21d.png)

  - ```html
    <form action="#">
        <label for="name">이름: </label>
        <input type="text" id="name" placeholder="이름을 입력해주세요."><br>
        <label for="date">날짜: </label>
        <input type="date" id="date" value="2018-01-03">
    </form>
    ```

- Select & Option

  - ```html
    <select>
        <option value="1">허니오트</option>
        <option value="2" disabled>플랫브래드</option>
        <option value="3">하티 이탈리안</option>
    </select>
    ```

- Input

  - ```html
    <label for="name">이름: </label>
    <input type="text" id="name" placeholder="이름을 입력해주세요."><br>
    <label for="date">날짜: </label>
    <input type="date" id="date" value="2018-01-03">
    <input type="radio" name="sandwich" value="1" checked>에그 마요<br>
    <input type="radio" name="sandwich" value="2">이탈리안 비엠티<br>
    <input type="radio" name="sandwich" value="3">터키 베이컨 아보카도
    <input type="number" value="15" step="15" min="15" max="30">
    <input type="checkbox" name="야채/소스" value="1">토마토<br>
    <input type="checkbox" name="야채/소스" value="2">오이<br>
    <input type="checkbox" name="야채/소스" value="3">할라피뇨<br>
    <input type="checkbox" name="야채/소스" value="4">핫 칠리<br>
    <input type="checkbox" name="야채/소스" value="5">바베큐<br>
    <input type="submit" value="submit">
    ```
```
    

------

## CSS

### 정의

- Cascading Style Sheet
- 문서의 컨텐츠, 레이아웃, 글꼴 및 시각적 요소들로 표현되는 문서(HTML)의 외관(디자인)을 분리하기 위한 언어.
- Styling의 정의

### CSS 구조 및 사용법

​```css
h1 { /* -- 셀렉터(selector) */
    color: blue; /* 선언 / 프로퍼티(property): 값(value) */
}
```

- Inline(인라인)

  - `<h1 style="color: blue"> 내용 </h1>` : html 요소의 style에 css 넣기

- Embdding(내부 참조)

  - HTML 내부에 CSS를 포함. 주로 head 내부에 style태그로 사용

  ```html
  <head>
      <style>
          h1 {
              colot: blue;
          }
      </style>
  </head>
  ```

- Link file(외부 참조)

  - 외부에 있는 CSS 파일 로드

  ```html
  <head>
      <link rel="stylesheet" href="mystyle.css">
  </head>
  <body>
      <h1> 내용 </h1>
  </body>
  ```

  ```css
  h1 {
      color: blue;
  }
  ```

#### 단위

- 크기 단위
  - px / %
  - em: 요소에 지정된 사이즈(상속된 사이즈나 디폴트 사이즈)에 상대적인 사이즈
  - rem: 최상위 요소(html) 기준. (default: 16px)
- Viewport 단위
  - 디바이스마다 다른 크기의 화면을 가지기 때문에 상대적인 단위를 사용
  - vw: 너비의 1/100, vh: 높이의 1/100, vmin, vmax: 둘 중 작거나 큰쪽의 1/100
- 색상 표현 단위
  - HEX: #ffffff / RGB: rgb(0, 0, 0) / RGBA: rgba(0, 0, 0, 0.5)

#### Box model

- ![image](https://user-images.githubusercontent.com/52814897/62823988-888d5200-bbd2-11e9-99fc-9c3642aa4eec.png)

- 기본 박스모델 활용

  - ```css
    /* margin, padding(margin과 동일) */
    .margin {
        margin-top: 10px;
        margin-right: 10px;
        margin-bottom: 10px;
        margin-left: 10px;
        /* shorthand
        하나: 상하 / 둘: 상하 좌우 / 셋: 상 좌우 하 / 넷: 상 우 하 좌(시계)
        */
        margin: 10px 20px 30px 40px;
    }
    .margin-padding {
        margin: 10px;
        padding: 30px;
    }
    
    
    /* border */
    .border {
        border-width: 2px;
        border-top-width: 2px; /* 상하좌우 가능 */
        border-style: dashed;
        border-color: black;
        /* shorthand 순서 상관 없음*/
        border: 2px dashed black;
    }
    ```

#### display  속성

- block : 항상 새로운 라인 / 화면 크기 전체의 가로폭 차지 (width: 100%)
  - 너비를 정해주면 정렬도 가능
    - `margin-right: auto;`왼쪽 정렬
    - `margin-left: auto;`오른쪽 정렬
    - 가운데 정렬: 왼쪽, 오른쪽 정렬을 같이 선언
  - 요소 예) div / h1 ~ h6 / p / ol / ul / li / hr / table / form
- inline : 문장 중간에 들어감. content의 너비만큼 가로폭 차지
  - 따라서, width, height, margin-top, margin-bottom 프로퍼티 지정 불가
  - 단, 상하 여백은 `line-height`로 지정 가능
  - 요소 예) span / a / strong / img / br / input / select / textarea / button
- inline-block : block과 inline 레벨 요소의 특징을 모두 갖는다.
  - inline 레벨 요소처럼 한줄에 표시되는 동시에
  - block에서의 width, height, margin(top, bottom) 속성 모두 지정 가능
- none: 해당 요소를 화면에 표시하지 않음. `공간조차 사라진다`

#### visibility 속성

- none은 공간조차 없고, hidden은 보이지 않으나 공간을 차지함.

- ![image](https://user-images.githubusercontent.com/52814897/62824191-6f39d500-bbd5-11e9-9306-be01f4113dc6.png)

#### Font

- `font-family'를 통하여 글꼴 변경 가능

- ```css
  .font-1{
    font-size: 30px;
    font-family: 'Courier New', Courier, monospace;
    font-style: italic;
  ```

#### Position

- static(기본위치, default) : 기본적인 요소의 배치 순서에 따라 배치.
  - 부모 요소 내에 자식 요소로 존재할 때는 부모 요소의 위치를 기준으로 배치
- relative(상대위치) : 기본위치를 기준으로 좌표 프로퍼터(top, bottom, left, right)을 사용하여 위치를 이동(음수도 가능)
  - ![image](https://user-images.githubusercontent.com/52814897/62824673-9a73f280-bbdc-11e9-8e7a-a94d1693c96a.png)
- absolute(절대위치) : 부모 요소 또는 가장 가까운 조상 요소(`static 제외`) 기준
  - 즉, static을 제외한 relative, absolut, fixed 프로퍼티가 선언되어 있는 부모 또는 조상 요소를 기준으로 위치 결정.
  - ![image](https://user-images.githubusercontent.com/52814897/62824706-ec1c7d00-bbdc-11e9-8bb8-8a0a4a324eab.png)
- fixed(고정위치) : 브라우저 viewport를 기준으로 이동.
  - 스크롤이 되더라도 화면에서 사라지지 않고 항상 같은 곳에 위치
  - ![image](https://user-images.githubusercontent.com/52814897/62824724-140be080-bbdd-11e9-9a68-ae8829effe58.png)

------

## Bootstrap

### CDN

- Content Delivery Network(컨텐츠 전송 네트워크)
- 콘텐츠를 효율적으로 전달하기 위해 여러 노드를 가진 네트워크에 데이터 저장 후 제공
- 다른 서버에 저장되어 있는 부트스트랩 데이터를 내 html문서에 불러와 사용

### 사용방법

- ###  (bootstrap 사이트 참조)

- ```html
  <head> <!-- head에 bootstrap link를 선언한다. -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  </head>
  
  <body> <!-- body bootstrap script를 선언한다.-->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
      integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
      integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
      integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
    </script>
  </body>
  ```

### 속성

- margin & padding

  - ![1565508897307](C:\Users\GiEun\AppData\Roaming\Typora\typora-user-images\1565508897307.png)
  - `ml-1` 은 0.25rem(4px)인 점 기억.

- color

  - 색의 이름이 다르다.
  - 텍스트: `text-primary` / 배경: `bg-secondary` / 버튼: `btn-success` 등
  - ![image](https://user-images.githubusercontent.com/52814897/62831195-4dccfd80-bc56-11e9-85c5-a15097b39e4a.png) 

- button

  - ![image](https://user-images.githubusercontent.com/52814897/62831316-0182bd00-bc58-11e9-9398-531052c8d569.png)

  - ```html
    <!-- class 속성에 btn 값 선언 후 -->
    <button class="btn btn-primary" type="submit">Button</button>
    ```

  - 키워드: `btn-primary` `btn-lg (or sm)` `btn-block` 등

- alert

  - ![image](https://user-images.githubusercontent.com/52814897/62831323-1bbc9b00-bc58-11e9-8da9-b9f17d64aa12.png)

  - ```html
    <!-- alert 선언 -->
    <div class="alert alert-primary" role="alert">
      A simple primary alert—check it out!
    </div>
    ```

- border (테두리)

  - ![1565509879455](C:\Users\GiEun\AppData\Roaming\Typora\typora-user-images\1565509879455.png)

  - ```html
    <div class="border border-primary">경계가 파란색</div>
      <div class="border border-warning">경계가 노랑</div>
      <div class="border border-danger">경계가 빨강</div>
      <div class="border border-info">경계가 하늘</div>
      <span class="border">4방향</span>
      <span class="border-top">탑</span>
      <span class="border-right">라이트</span>
      <span class="border-bottom">바텀</span>
      <span class="border-left">레프트</span>
    ```

- display

  - ```html
    <!-- div는 원래 block이지만 inline으로 만들 수 있다.-->
      <div class="d-inline bg-primary text-white">div to inline</div>
      <div class="d-inline bg-primary text-white">div to inline</div>
      <div class="d-inline bg-primary text-white">div to inline</div>
      <!-- span은 원래 inline이지만 block으로 만들 수 있다.-->
      <span class="d-block bg-dark text-white">span to block</span>
      <span class="d-block bg-dark text-white">span to block</span>
      <!-- 반응형 만들기-->
      <div class="m-2 bg-danger d-sm-none d-md-block">보이나? 안보이나?</div>
      <div class="m-2 bg-warning d-md-none d-xl-block">보이나? 안보이나?</div>
      <div class="sticky fixed-top bg-dark"></div>
      <div class="sticky fixed-bottom bg-dark"></div>
    ```

  - 키워드

    ![1565510196279](C:\Users\GiEun\AppData\Roaming\Typora\typora-user-images\1565510196279.png)
  
- font

  - ```html
    <p class="text-left">Left aligned text on all viewport sizes.</p>
    <p class="text-center">Center aligned on all viewport sizes.</p>
    <p class="text-right">Right aligned on all viewport sizes.</p>
    <p class="text-sm-left">Left aligned on viewports with sizes.</p>
    <p class="text-md-center">Left aligned text on viewports. </p>
    <p class="text-lg-right">Left aligned text on viewports </p>
    <p class="text-xl-right">Left aligned text on viewports</p>
    <p class="text-lowercase">Lowercased text.</p>
    <p class="text-uppercase">Uppercased text.</p>
    <p class="text-capitalize">CapiTaliZed text.</p>
    <p class="font-weight-bold">Bold text.</p>
    <p class="font-weight-bolder">Bolder weight text (relative to the parent element).</p>
    <p class="font-weight-normal">Normal weight text.</p>
    <p class="font-weight-light">Light weight text.</p>
    <p class="font-weight-lighter">Lighter weight text (relative to the parent element).</p>
    <p class="font-italic">Italic text.</p>
    <!-- 그대로 출력 -->
    <p class="text-monospace">print('hi, there!0')</p>
    ```

- badge

### Grid

- 기본 사용 방법

  - ```html
    <!-- 1. 그리드의 기본 골격. 보통 3개 합이 12가 되게함. 12는 약수가 많아서 활용이 높음-->
      <div class="container">
        <div class="row">
          <!-- row가 있어야 grid가 작동함. 반드시 필요.
        row는 block 속성인 div를 일렬로 배치 가능하게 해줌-->
          <div class="square col-4">1</div>
          <div class="square col-4">2</div>
          <div class="square col-4">3</div>
        </div>
      </div>
    
      <!-- 2. container-fluid
      여백없이 꽉참 -->
      <div class="container-fluid">
        <div class="row">
          <div class="square col-4">1</div>
          <div class="square col-4">2</div>
          <div class="square col-4">3</div>
        </div>
      </div>
    ```

  - ![image](https://user-images.githubusercontent.com/52814897/62833045-2e909900-bc73-11e9-91b8-4347c7e9180a.png)

### Flex

- ![image](https://user-images.githubusercontent.com/52814897/62833470-415a9c00-bc7a-11e9-9c37-da1ca4706611.png)

- ![image](https://user-images.githubusercontent.com/52814897/62833471-4c153100-bc7a-11e9-8336-7f10ed37d4c1.png)

- ![image](https://user-images.githubusercontent.com/52814897/62833496-b9c15d00-bc7a-11e9-88d4-ddd5332fc3fe.png) ![image](https://user-images.githubusercontent.com/52814897/62833500-bf1ea780-bc7a-11e9-9ba3-4eb496814b4c.png)
  ![image](https://user-images.githubusercontent.com/52814897/62833501-c5ad1f00-bc7a-11e9-908d-ad77a74036a0.png)

  ![image](https://user-images.githubusercontent.com/52814897/62833504-cc3b9680-bc7a-11e9-9c5e-a7de26178e9b.png) ![image](https://user-images.githubusercontent.com/52814897/62833506-d362a480-bc7a-11e9-8664-1b8a6b115d08.png)

  ![image](https://user-images.githubusercontent.com/52814897/62833514-ed9c8280-bc7a-11e9-8bb3-9bd74c629aa8.png) ![image](https://user-images.githubusercontent.com/52814897/62833507-deb5d000-bc7a-11e9-9fc7-1e75a2deec2a.png)

------

## Homework & Workshop

### 09_homework

**1. HTML은 무엇의 약자인가? [정답 : 3]**

1. Hyperlinks and Text Markup Language
2. Home Tool Markup Language
3. **Hyper Text Markup Language**
4. Hyper Tool Markup Language

**2. 다음 중 맞으면 T, 틀리면 F를 작성하시오.**

1. 웹 표준은 만드는 곳은 Mozilla 재단이다. [F] 
   - 웹 표준을 만드는 곳은 W3C이다.
   - Mozilla는 참여 기업 중 하나이다.
2. 표(table)을 만들 때에는 반드시 `<th>` 태그를 사용해야 한다. [F]
   - 반드시는 아니지만 개발자들의 약속인 semantic tag 중의 하나이다.
3. 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다. [T]
4. 인용문을 가리키는 태그는 `<blockquote>` 이다. [T]

**3. 보기 중 콘텐츠의 의미를 명확히 하기 위해 HTML5에서 새롭게 추가된 시맨틱(semantic) 태그를 모두 고르시오.**

​	`header, section, footer`

**4. 아래 이미지와 같이 로그인 Form을 생성하는 HTML 코드를 작성하시오.**

![image](https://user-images.githubusercontent.com/52814897/62197695-4d617680-b3bb-11e9-950c-6e017b024160.png)

```html
<form action="#"> <!-- form 태그는 회원가입 양식이나 검색 창들을 만들 때 사용 -->
  ID: <input type="text"><br> <!-- input 태그를 통해 빈칸 형성 가능 -->
  PWD: <input type="password">
  <input type="submit" value="로그인"> <!-- input 태그를 통해 간단한 버튼도 형성 가능 -->
</form>
```

------

### 09_workshop

**1. 클릭하면 'https://www.ssafy.com/'으로 이동하는 버튼을 만드시오.**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <!-- <a> 태그를 이용하여 원하는 위치로 이동할 수 있다. 속성 href와 사용한다. -->
  <a href="https://www.ssafy.com/ksp/jsp/swp/swpMain.jsp"><img src="images/ssafy.jpg" alt="html image" style="width: 50px; height: 50px"></a>
</body>
</html>
```

**2. 다음 태그에서 잘못된 부분을 찾아 올바르게 수정하시오.**

![image](https://user-images.githubusercontent.com/52814897/62195401-e346d280-b3b6-11e9-9180-ffbb78c1039d.png)

```html
<!-- <img>태그는 속성 src와 함께쓴다. href를 src로 바꿔준다. -->
<img src="https://picsum.photos/200" alt="#">
```

**3. 아래 그림과 같은 폴더 구조가 있다. Resume.html에서 코드를 작성 중일 때, Image 폴더 안의 my_photo.png를 보여주는 img tag를 작성하시오.**

```html
<!-- 상대경로 사용법 -->
<img src="../Image/my_photo.png" alt="#">
```

------

### 10_homework

**1. CSS는 무엇의 약자인가? [2]**

1. Creative Style Sheets
2. **Cascading Style Sheets**
3. Computer Style Sheets
4. Colorful Style Sheets

**2. 다음 중 맞으면 T, 틀리면 F를 작성하시오.**

1. HTML과 CSS는 각자 문법을 갖는 별개의 언어이다. [T]
   - 하지만, HTML은 프로그래밍 언어로 보진 않는다.
2. 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다. [T]
3. 자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속 받는다. [F]
   - 너비, 높이 등 상속을 안 받는 속성도 있다.

**3. 크기 단위 em은 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이즈를 설정한다. 즉, 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데 이를 예방하기 위해 HTML 최상위 요소의 기준으로 삼는 크기 단위는 무엇인가?****

- 정답: rem
  - 1rem = 16px

**4. 다음 예제를 통해 '후손 셀렉터'와 '자식 셀렉터'의 차이를 설명하시오.**

![image](https://user-images.githubusercontent.com/52814897/62272735-bb1ea880-b476-11e9-9eeb-d0f624b3509e.png)

- **자식 셀렉터**는 한 단계 indented 된 태그이며, 접근할 때는 **'>'**
  - div의 바로 아래 자식들 중에 p 태그. 손자나 증손자 안됨.

- **후손 셀렉터**는 두 단계 이상 indented 된 태그이며, 접근할 때는 **' '(공백)**
  - div의 모든 자식들 중에 p(깊이는 상관 없음)

------

### 10_workshop

**1. 아래의 코드를 작성하여 몇 번째 단락이 빨간색으로 변하는지 확인해보자.**

![image](https://user-images.githubusercontent.com/52814897/62273050-88c17b00-b477-11e9-9a2c-d1c2a5597cfe.png)

![image](https://user-images.githubusercontent.com/52814897/62273221-f372b680-b477-11e9-83e1-a1869a211791.png)

- 첫번째 단락만 빨간색으로 변한다.

  

![image](https://user-images.githubusercontent.com/52814897/62273270-18672980-b478-11e9-9c10-f37f79bec2a3.png)

![image](https://user-images.githubusercontent.com/52814897/62273365-58c6a780-b478-11e9-835a-59b185d1f41d.png)

- 두번째 단락만 파란색으로 변한다.

- nth-child 와 nth-of-type의 차이
  - el:nth-child(n)
    - el 태그 부모의 자식들 중, `n번째 자식이 el 이라면 선택.` el 태그가 아니면 동작하지 않음.
  - el:nth-of-type(n)
    - el 태그 부모의 자식들 중 `el 인 것들 중에서 n 번째`를 선택

------

### 11_homework

![image](https://user-images.githubusercontent.com/52814897/62607631-5d3c0600-b939-11e9-8912-d175aee50fca.png)

```html
정답 : button. class="btn btn-danger"
<button type="button" class="btn btn-danger">Danger</button>
```



![image](https://user-images.githubusercontent.com/52814897/62607604-51e8da80-b939-11e9-84ee-6625e7ec7133.png)

```html
정답 : alert. class="alert alert-primary"
<div class="alert alert-primary" role="alert">Hello SSAFY ?!</div>
```



![image](https://user-images.githubusercontent.com/52814897/62608042-1569ae80-b93a-11e9-91a3-9a081bf1273a.png)

```
정답 : (A) 12, (B) 5
col / col-sm / col-md / col-lg / col-xl
<576  >=768    >=768    >=960    >=1200
```



![image](https://user-images.githubusercontent.com/52814897/62608140-41852f80-b93a-11e9-98b4-ca4aae535190.png)

```html
<!-- Grid는 container와 row를 먼저 선언해준다. -->
<div class="container">
    <div class="row">
      <div class="col-3 font-weight-bold">25%</div>
      <div class="col-6 font-weight-bold">50%</div>
      <div class="col-3 font-weight-bold">25%</div>
    </div>
  </div>
```

![image](https://user-images.githubusercontent.com/52814897/62608847-a68d5500-b93b-11e9-9c22-82d663f92603.png)

-------

### 11_workshop

- **웹 만들기**
- **Bootstrap 사용 Component**
  - **Navbar**
  - **Forms**
  - **Card**
  - **사진 출처: http://lorempixel.com/**

![image](https://user-images.githubusercontent.com/52814897/62667750-0af3f700-b9c4-11e9-823d-f901b9c5f83e.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

</head>

<body>
  <!-- Navbar 생성 -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup"
      aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-item nav-link active" href="#">Home <span class="sr-only">(current)</span></a>
        <a class="nav-item nav-link" href="#">Git</a>
        <a class="nav-item nav-link" href="#">Python</a>
      </div>
    </div>
  </nav>

  <br>
  <!-- Form 생성 -->
  <form style = "padding: 0 100px">
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
      </div>
      <div class="form-group">
          <label for="exampleInputPassword1">Password Confirmation</label>
          <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password Confirmation">
        </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>

    <br>
  <!-- Cards 생성 -->
  <div style = "padding: 0 100px" class="row">
    <div class="card col-4" style="width: 18rem;">
      <img src="http://lorempixel.com/400/200/food" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">음식</h5>
        <p class="card-text">음식 사진입니다.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
    <div class="card col-4" style="width: 18rem;">
      <img src="http://lorempixel.com/400/200/animals" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">동물</h5>
        <p class="card-text">동물 사진입니다.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
    <div class="card col-4" style="width: 18rem;">
      <img src="http://lorempixel.com/400/200/cats" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">고양이</h5>
        <p class="card-text">고양이 사진입니다.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>


  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
  </script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
  </script>
</body>

</html>
```

------

### 12_homework

**1. 반응형 웹 디자인이란 하나의 웹사이트에서 PC, 스마트폰, 태블릿 PC 등 접속하는 --(a)--에 따라 가폭이나 배치를 변경하여 가독성을 높이도록 하는 웹페이지 접근 기법이다.**

- #### (a): 디스플레이

**2. 모바일 디바이스에서 반응형 웹이 정상적으로 동작하기 위해서는 head tag 내부에 특정 meta tag를 정의하여야 한다. 여기서 말하는 meta tag의 가장 일반적인 형태를 작성 하시오.**

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**3. Bootstrap에서는 총 5개의 반응형 그룹으로 나누어 화면 크기별로 다른 Layout이 표시된다. 여기서 말하는 5개의 그룹을 구분 짓는 화면 크기의 가로 해상도 4가지를 px단위로 작성하시오.**

- 정답 : 540px, 720px, 960px, 1140px

------

### 12_workshop

![image](https://user-images.githubusercontent.com/52814897/62681471-ba48c200-b9f4-11e9-9998-59de4a431cbb.png)



```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

  <style>
  .square {
    width: 50px;
    height: 20px;
    background-color: pink;
    border: 1px solid black;
  }
  </style>
</head>

<body>

    <div class="container">
        <div class="row">
          <div class="square col-12 col-md-6 col-xl-3">1</div>
          <div class="square col-12 col-md-6 col-xl-3">2</div>
          <div class="square col-12 col-md-6 col-xl-3">3</div>
          <div class="square col-12 col-md-6 col-xl-3">4</div>
        </div>
      </div>


  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
  </script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
  </script>
</body>

</html>
```

![image](https://user-images.githubusercontent.com/52814897/62681571-f5e38c00-b9f4-11e9-8e3b-9a77ae98bda4.png)
![image](https://user-images.githubusercontent.com/52814897/62681591-00058a80-b9f5-11e9-9f6c-de3fd0980c29.png)
![image](https://user-images.githubusercontent.com/52814897/62681611-0d227980-b9f5-11e9-9348-a58a6bf1fd65.png)

------

## Project

### 03_project - HTML/CSS를 활용한 웹 사이트 구성

- **HTML와 CSS를 이용하여 간단한 홈페이지를 구성한다.**
- **CSS 스타일시트 속성에 대해 연습한다.**

주요 속성 및 명령어

- Navigation Bar 

  - **position: fixed; - 스크롤과 상관없이 영역을 항상 특정 위치에 고정시킨다.**
  - **z-index: 1000;  - 영역의 우선순위를 정하며, 높은 숫자일수록 다른 영역 앞으로 위치한다.**
  - **float: right;  - 리스트가 가로 방향으로 배치되도록 한다.**

  ```html
  <!-- 페이지의 최상단 : 로고 및 네비게이션바 -->
  <header>
    <a href="#">
      <img class="logo" src="images/logo.png" alt="logo">
    </a>
    <!-- 네비게이션 바 -->
    <nav>
      <ul class="nav-items">
        <li><a href="#">Main</a></li>
        <li><a href="#">Box office</a></li>
        <li><a href="#">영화 상영작</a></li>
        <li><a href="#">About</a></li>
      </ul> 
    </nav>
  </header>
  ```

  ```css
    header {
    position: fixed; /* 스크롤 내려도 따라오듯이 고정 */
    top: 0; /* 위의 여백을 없앰 */
    z-index: 1000; /* 숫자가 크면 보이는 우선순위가 높다. */
    background-color: gray;
    }
  
    nav {
    /* navigation 항목을 오른쪽으로 정렬 시키세요.*/
    float: right;
  	}
  ```

![image](https://user-images.githubusercontent.com/52814897/62423305-4fe50880-b6fa-11e9-981e-c89cd8c8906d.png)

- Aside
  - **list-style-type: none; - 리스트 앞에 보이는 point를 변경하거나 없앨 수 있다.**
  - **position: absolute; - default 값인 relative와 달리 문서의 원래 위치와 상관없이 가장 가까운 상위 요소를 기준으로 위치가 결정된다.**

```html
<aside>
      <h2>장르 목록</h2>
      <ul class="aside-items">
        <li>액션</li>
        <li>가족</li>
        <li>코미디</li>
        <li>히어로</li>
      </ul>
    </aside>
```

```css
aside {
  /* aside를 부모인 div#content의 영역에 위치시키세요.
  div#content는 position: relative 입니다.
  */
  position: absolute;
  top: 0;
}

.aside-items > li {
  /* li 태그의 bullet point를 제거 해주세요. */
  list-style-type: none;
}
```

![image](https://user-images.githubusercontent.com/52814897/62423457-57f17800-b6fb-11e9-8529-f277dfb9a4cf.png) ![image](https://user-images.githubusercontent.com/52814897/62423467-722b5600-b6fb-11e9-9c99-665528c3d698.png)

![image](https://user-images.githubusercontent.com/52814897/62423528-80c63d00-b6fc-11e9-9fe1-2d3d678807be.png)

![image](https://user-images.githubusercontent.com/52814897/62423535-9176b300-b6fc-11e9-80c4-a950a5c7221c.png)

- Footer
  - **text-align: center; - 영역 내에서 텍스트가 좌우로 가운데 정렬되도록 해준다.**
  - **line-height: 50px; -영역 내 텍스트의 위 아래 위치를 조절할 수 있으며, 이때 영역의 높이만큼 지정해주면 가운데에 위치하게 된다.**

```css
footer {
  position: fixed;
  bottom: 0;
  /* 텍스트를 가운데 정렬 해주세요. */
  text-align: center;
  /* 텍스트가 수직정렬 되도록 해주세요. (footer는 높이가 50px) */
  line-height: 50px;
}
```

![image](https://user-images.githubusercontent.com/52814897/62423558-dd295c80-b6fc-11e9-900c-6826c8f0126a.png)

------

### 04_project - 부트스트랩을 활용한 반응형 웹사이트 구축

- HTML / CSS / Bootsrap을 이용하여 영화 정보 관련 웹사이트 구축
- 브라우저의 크기에 따라 레이아웃이 달라지는 반응형 웹사이트 구축

`01_layout.html`, `01_layout.css`

- Navigation Bar

  - Sticky navigation bar

    - `sticky-top`은 스크롤과 상관없이 영역을 항상 브라우저 상단에 위치하게 해준다.

      ```html
      <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top">
      ```

      ```css
      nav {
        background-color: white;
        font-family: 'Sunflower', sans-serif;
      }
      ```

      

    ![image](https://user-images.githubusercontent.com/52814897/62794914-53b8c680-bb10-11e9-9e8a-43a852ad6bfd.png)

  - Nav list setting

    - `ml-auto`을 통해 영역을 우측 정렬해준다.

      ```html
      <ul class="navbar-nav ml-auto">
      ```

    - `Bootstrap`에서 브라우저의 크기에 따른 반응형 navigation bar source를 활용할 수 있다.

      - width : 900px / navbar 우측 상단 정상 출력

      ![image](https://user-images.githubusercontent.com/52814897/62779508-66ba9f00-baee-11e9-8b60-5e22b53176b5.png)

      - width : 800px / 우측 상단 navbar 숨김

  ![image](https://user-images.githubusercontent.com/52814897/62779542-76d27e80-baee-11e9-909d-30162383bf1b.png)

- Header

  - Background 배경 설정

    - `flex`의 정렬기능을 이용하여 text의 위치를 조절한다.
      - `justify-content`는 영역의 횡축 / `align-items`는 종축을 조절한다.

    ```html
    <header>
      <div class="d-flex justify-content-center align-items-center flex-column" id="header-title">
        <h2>당신에게 어울리는 영화를</h2>
        <h2>추천해드립니다.</h2>
      </div>
    </header>
    ```

    - `background` 속성을 활용하여 사진의 높이와 위치를 정한다.

    ```css
    #header-title {
      background-image: url("images/header.jpg");
      background-size: cover;
      background-position: center; 
      height: 350px;
    }
    ```

    ![image](https://user-images.githubusercontent.com/52814897/62794860-279d4580-bb10-11e9-97ba-0f749bc5cc7a.png)

  

- Footer

  - copyright / home button

    - `justify-content-between` copyright와 button을 양 끝에 배치할 수 있다.

    ```html
    <footer class="d-flex justify-content-between align-items-center">
    ```

    - `home button`으로 브라우저의 맨 상단으로 이동할 수 있으며,
    - `Font awesome` 사이트에서 다양한 Icon을 얻을 수 있으며 아래와 같이 선언 후 사용할수 있다.

    ```html
    <head>
      <script src="https://kit.fontawesome.com/3a687bfd3a.js"></script>
    </head>
    ```

    - Icon에 해당하는 <a> 태그에 `#`을 입력해주면 맨 위로 이동한다.

    ```html
    <footer class="d-flex justify-content-between align-items-center">
      <p class="my-0">ⓒ2019,GIEUN KIM</p>
      <a href="#"><i class="fas fa-arrow-alt-circle-up fa-2x"></i></a>
    </footer>
    ```

    - `footer`의 좌우 마진은 3rem이다.(1rem = 16px)

    ```css
    footer {
      width: 100%;
      height: 50px;
      background-color: gray;
      padding: 0 3rem;
    }
    ```

![image](https://user-images.githubusercontent.com/52814897/62766221-e59ee000-bacc-11e9-83ee-83c34daeec75.png)

- Font 설정

  - `Google Fonts` 사이트에서 다양한 폰트를 사용할 수 있다

  ```html
  <link href="https://fonts.googleapis.com/css?family=Nanum+Pen+Script|Sunflower:300&display=swap" rel="stylesheet">
  ```

  - 사용하고자 하는 영역에 `font-family` 속성을 준다.

  ```css
  header {
    font-family: 'Nanum Pen Script', cursive;
  }
  ```

  ![image](https://user-images.githubusercontent.com/52814897/62766691-09165a80-bace-11e9-9b8b-4352ec870fd8.png)

  ![image](https://user-images.githubusercontent.com/52814897/62766707-0fa4d200-bace-11e9-8be0-4135489706b2.png)

- 01_layout 완성본

  ![image](https://user-images.githubusercontent.com/52814897/62779620-b305df00-baee-11e9-91ea-4cddd9d3c39a.png)

`02_movie.html`, `02_movie.css`

영화목록 레이아웃 제작

- Subtitle

  - 밑줄 만드는 법 `border`의 위나 아래쪽 한쪽에만 값을 줌으로써 생성할 수 있다.

  ```html
  <h3 class="subtitle">영화 목록</h3>
  ```

  ```css
  .subtitle:after {
    content: "";
    display: block;
    width: 70px;
    border-bottom: 1px solid orange;
    margin: 10px auto;
  }
  
  ```

  ![image](https://user-images.githubusercontent.com/52814897/62780158-fad93600-baef-11e9-9d52-f19fde102251.png)

  

- ### Card view / 반응형 리스트

  - `Bootstrap`의 `Cards` 컴포넌트를 통행 다양한 card source를 활용할 수 있다.
  - `grid`를 이용하여 브라우저 크기에 따라 표시되는 리스트의 양을 변경할 수 있다.
  - 576px 이하에서는 1개, 768px 이하에서는 2개, 992px 이하는 3개, 그 이상은 4개를 표시한다.

  ```html
  <div class="contatiner">
      <div class="row">
          <div class="movie col-12 col-sm-6 col-md-4 col-lg-3"> 리스트 </div>
          <div class="movie col-12 col-sm-6 col-md-4 col-lg-3"> 리스트 </div>
          <div class="movie col-12 col-sm-6 col-md-4 col-lg-3"> 리스트 </div>
      </div>
  </div>
  
  ```

  

![image](https://user-images.githubusercontent.com/52814897/62779783-1bed5700-baef-11e9-9707-aa8073c95245.png)

![image](https://user-images.githubusercontent.com/52814897/62779853-417a6080-baef-11e9-8113-69cc67bf6243.png)

- ### 02_movie.html 완성본

![image](https://user-images.githubusercontent.com/52814897/62794334-ca54c480-bb0e-11e9-8235-fcbdda57f290.png)





`03_detail_view.html`, `03_detail_view.css`

- modal / carousel

  - `Bootstrap`의 `modal` 컴포넌트를 활용한다.
  - 우선 이미지를 클릭했을 때 연결될 modal의 target을 정한다.
    - `img` 태그에 `data-toggle`과 `data-target`을 추가해준다.

  ```html
  <img src="images/20184621.jpg" class="card-img-top" alt="영화 포스터" data-toggle="modal" data-target="#exit">
  
  ```

  - `modal` 소스에 id 를 `img` 태그에서 정한 target 명과 같게 한다

    ```html
    <div class="modal" tabindex="-1" role="dialog" id="exit">
    
    ```

  - `modal` 소스 내부에 `carousel`을 추가하여 여러 사진을 넘기며 볼 수 있다.

    - `modal` 내부에 사진이 꽉차게 하려면 class에 `w-100` 속성을 추가해준다.

    ```html
    <bootstrap modal source...>
    <div class="modal-body p-0"> <!-- modal body -->
    	<bootstrap carousel source...>
    		<div class="carousel-item"><img src="images/20184621-01.jpg" ...></div>
            <div class="carousel-item"><img src="images/20184621-02.jpg" ...></div>
            <div class="carousel-item"><img src="images/20184621-03.jpg" ...></div>
    
    ```

    

![image](https://user-images.githubusercontent.com/52814897/62794478-23245d00-bb0f-11e9-8e82-e06473972f9d.png)

- ### 03_detail_view.html 완성본

![image](https://user-images.githubusercontent.com/52814897/62794547-59fa7300-bb0f-11e9-8687-753d7cbe374e.png)

