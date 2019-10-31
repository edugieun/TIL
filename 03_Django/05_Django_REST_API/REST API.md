# REST API

## dumpdata

```bash
$ python manage.py dumpdata musics > dummy.json
$ python manage.py dumpdata --indent 2 musics > dummy.json
```

## loaddata

`fixture`

- 데이터베이스의 직렬화(serialized)된 내용을 포함하는 파일 모음이다.

- 각 fixture는 고유한 이름을 가지며, 이를 구성하는 파일은 여러 응용 프로그램에서 여러 디렉토리에 배포될 수 있다.

- django는 `loaddata`시 설치된 모든 app 에서 `fixtures`라고 하는 이름의 폴더를 찾는다.

- ```
  musics/
  	fixtures/
  		musics/
  			dummy.json
  ```

- ```bash
  $ python manage.py loaddata musics/dummy.json
  ```

  


API란?

- API(Application Programming Interface, 응용프로그램 프로그래밍 인터페이스)
- API는 명확하게 '어떤 것이다.'라고 규정하기는 어렵지만, 서로 다른 시스템, 장치들이 서로 좀 더 편하고 원활하게 소통할 수 있게 도와주는 인터페이스(서로를 연결해주는 것) 또는 수단이라고 생각할 수 있다.
- 예를 들어, 프로그래밍에서 API는 math, I/O 등의 라이브러리, avg(), max(), min() 같은 내장 함수 등 개발을 하는데 편하게 해주는 기능.
- 운영체제인 window가 chrome이라는 응용프로그램을 여는 행위, google에서 검색 하는 행위.
- 개발자가 지도나 날씨 어플리케이션을 만들 때, 위치 정보, 날씨 정보가 담긴 데이터를 가져오는 방법이나 명령어.
- 이처럼 서로 다른 시스템, 장치들이 서로 소통할 수 있게 해주는 기능 또는 규격을 API 라고 한다.

API 사용 이유

RESTful API란?

-  [https://blog.npcode.com/2017/04/03/rest%EC%9D%98-representation%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80/](https://blog.npcode.com/2017/04/03/rest의-representation이란-무엇인가/) 
- https://mangkyu.tistory.com/46 
- https://brainbackdoor.tistory.com/53 
- https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html 

POSTMAN 사용 이유