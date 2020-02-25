# CSS

## 정의

- Cascading Style Sheet
- 문서의 컨텐츠, 레이아웃, 글꼴 및 시각적 요소들로 표현되는 문서(HTML)의 외관(디자인)을 분리하기 위한 언어.
- Styling의 정의
- HTML은 독자적으로 사용가능하나 CSS는 HTML이 없으면 독자적 사용 불가능

## CSS 구조 및 사용법

```css
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
  
- 스타일 적용 우선순위는 Inline, Embedding,  link file 순이지만, 보통 link file을 많이 씀 => 컴포넌트, 모듈화. 재사용 가능.

## Style Guide

- 선택자 우선순위
  
  1. !important
  2. 인라인 선택자
  3. id 선택자 - 일반적으로 중복 사용하지 않고 하나의 텍스트에 하나만 적용
  4. 클래스 선택자
  5. 태그 선택자
6. 전체 선택자

- 들여쓰기 2문자

- 클래스, 아이디명은 케밥 케이스(kebob-case)를 사용한다.

- 다중 선택 시 한 줄에 선택자를 하나씩 작성

  ```ㅊㄴㄴ
  .bold,
  .yelllo,
  .bold {
  	font-weight: bold;
  }
  ```

- 모든 스타일 뒤에는 세미콜론을 붙인다.
- 스타일 지정 시 아이디, 태그 대신에 클래스를 사용한다. (되도록)

- 숫자 0 이후에는 불필요한 단위를 작성하지 않는다.

- @import 대신 <link> 방법을 사용한다.

- 가능한 한 단축어(축약형)를 사용한다.

  - 단, 불필요하게 과용하는 것 피한다.

## 단위

- 크기 단위
  - px / %
  - em: 요소에 지정된 사이즈(상속된 사이즈나 디폴트 사이즈)에 상대적인 사이즈
  - rem: 최상위 요소(html) 기준. (default: 16px)
- Viewport 단위
  - 디바이스마다 다른 크기의 화면을 가지기 때문에 상대적인 단위를 사용
  - vw: 너비의 1/100, vh: 높이의 1/100, vmin, vmax: 둘 중 작거나 큰쪽의 1/100
- 색상 표현 단위
  - HEX: #ffffff / RGB: rgb(0, 0, 0) / RGBA: rgba(0, 0, 0, 0.5)

## Box model

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

## display  속성

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

## visibility 속성

- none은 공간조차 없고, hidden은 보이지 않으나 공간을 차지함.

- ![image](https://user-images.githubusercontent.com/52814897/62824191-6f39d500-bbd5-11e9-9306-be01f4113dc6.png)

## Font

- default font size는 16px

- `font-family'를 통하여 글꼴 변경 가능

  ```css
  .font-1{
    font-size: 30px;
    font-family: 'Courier New', Courier, monospace;
    font-style: italic;
  ```


## Position

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

## Background

- cover 특성
  - 배경이미지의 크기  비율을 유지한 상태에서 부모 요소의 width, height 중 큰 값에 배경 이미지는 맞춘다. 따라서 이미지의 일부가 보이지 않을 수 있다.
- contain
  - 배경이미지의 크기 비율을 유지한 상태에서 부모 요소의 영역에 배경이미지가 보이지 않는 부분까지 전체가 들어갈 수 있도록 이미지 크기를 조절한다.

- attachment: fixed
  - 스크롤 되더라도 배경 이미지는 스크롤 되지 않고 고정시킨다.