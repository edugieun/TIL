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

  

- 