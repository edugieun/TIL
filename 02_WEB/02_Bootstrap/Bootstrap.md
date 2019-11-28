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