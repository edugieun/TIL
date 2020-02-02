# HTML

## 정의

- Hyper Text Markup Language
- Hyper Text: 기존의 선형적인 텍스트가 아닌 Hyper Link를 통하여 텍스트를 이동, 비선형적으로 이루어진 텍스트
- Markup: 웹 브라우저에 표시되는 글, 이미지 등의 다양한 컨텐츠를 표시하기 위한 문법
- Language: 웹 페이지를 작성하기 위한 역할 표시 언어
- 표준 : W3C(HTML5) / WHATWG(HTML Living Standard)
- HTTP(S) - Hyper Text Transfer Protocol (Secure)
- HTTP는 해킹의 위험이 있음.
- HTTPS는 보안 및 HTTP보다 훨씬 빠름.
- HTML은 `프로그래밍 언어가 아니다.` 텍스트를 보여주기 위한 표시 언어이다.
- 연산, 반복 등이 안됨.
- OG : Open Graph by Facebook :grey_question:

## Style Guide

- 들여쓰기는 2칸
- 속성값은 반드시 큰 따옴표("). (작은 따옴표도 되지만, 표준은 큰 따옴표임.)
- 태그, 속성, 속성값 등에는 모두 소문자만 사용한다. (역시 표준임.)
- 최상위 html 태그에는 lang 속성을 주어 문서의 기본 언어를 지정한다.(스크린 리더는 lang을 통해 언어를 인식하여 자동으로 음성을 변환하거나 해당 언어에 적합한 발음을 제공한다.)
- IE는 특정 META 태그를 사용해 페이지가 특정 버전에 맞게 세팅되도록 지정해준다.
```html
<meta http-equiv="X-UA-Compatible" content="ie=edge">
```
- = 옆에 속성같은 띄지않고 붙인다
- boolean 속성 값은 따로 명시하지 않는다.
```html
<!-- 지양 -->
  <input type="radio" name="sandwich" value="1" checked=true>에그 마요<br>
<!-- 지향 -->
  <input type="radio" name="sandwich" value="1" checked>에그 마요<br>
```

## HTML Tag

### Semantic Tag

- 검색엔진 최적화
- 단순히 보여주기 위한 것을 넘어 의미를 가지는 태그들을 활용하기 위해 노력
- 탄생 배경과 기능
  - HTML5 이전에는 `<div>` 태그 안에 id나 class 속성으로 각자 이름을 지정하였기 때문에 컨텐츠를 분석, 식별하기가 어려웠음. 하지만, 의미를 가지는 시맨틱 태그로 검색 엔진이 더 정확한 검색 결과를 빠르게 처리 가능
- Non semantic(div, span 등)
  - div / span 등

![image](https://user-images.githubusercontent.com/52814897/62177410-cba02780-b37f-11e9-9571-7c81b2c7e513.png)

- Semantic
  - header / nav / aside / section / article / footer / strong (=bold) / em (=i)

![image](https://user-images.githubusercontent.com/52814897/62177391-ba571b00-b37f-11e9-9d88-bc55bbf434de.png)

### Tag

- `<h1~h6>`

- `<strong>` : sementic 강조(bold)
- `<i>` : Italic
- `<em>` : sementic 강조(Italic)
- `<p>` : 단락
- `<pre>` : 폰트변화 없이 글자 그대로 출력
- `<hr>` : 헤드라인
- `<br>` : 한줄 띄기
- `<ol>` : order list
- `<ul>` : unorder list
- `<li>` : 목록
- `<blockquote>` : 들여쓰기. 인용구에 사용

## HTML 문서의 기본 구조

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

## Tag와 DOM TREE (Document Object Model)

- 주석(Comment)

  - `<!-- 주석 내용 -->`
- 요소(Element)

  - `<h1> contents </h1>`
  - `<img src="url"/>` (Self-closing element)
- 속성(Attribute)

  - `<a href(속성명)="https://google.com(속성값)"></a>` 
  - 공백(`" "`) 사용 No!
- HTML DOM Tree
  - DOM - Document Object Model
    - "The HTML DOM is a standard for how to get, change, add, or delete HTML elements." - w3school
  - HTML 문서가 web을 통해 load 될 때, 각각의 태그와 요소들은 객체화되어 아래와 같은 부모, 자식 및 형제 관계를 갖는 tree 구조를 생성하게 된다. 
  - 이런 객체로 이루어진 tree를 추후에 Javascript나 다른 언어들을 통해 접근할 수 있고, html 요소를 추가, 삭제, 수정 할 수 있다.

![image](https://user-images.githubusercontent.com/52814897/69914714-86554900-148a-11ea-8cfe-3c164027a443.png)

<center>출처 - w3school</center>

```html
<body> <!-- body태그와 h1태그는 부모(parent)-자식(child) 관계-->
    <h1> 웹문서 </h1> <!-- h1태그와 ul태그는 형제관계(sibling) -->
    <ul>
        <li>HTML</li>
        <li>CSS</li>
    </ul>
</body>
```

