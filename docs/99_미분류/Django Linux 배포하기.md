

# Django + Vue AWS 서버 배포하기(WSGI, AWS)

## Runserver 테스트

먼저 기존의 Window에서 작업한 프로젝트가 AWS 서버에서도 잘 동작하는지 확인해야 한다.

나의 경우 DB관련 에러가 났다. Django 프로젝트와 MySQL을 연동하기 위한 mysqlclient를 설치할 때 발생하는 오류이다.

![image](https://user-images.githubusercontent.com/52814897/79877872-bd230000-8427-11ea-84f8-53e9a12a9b3e.png)

mysqlclient를 설치하기 위해서는 추가 패키지 설치가 필요하다.

```bash
$ apt-get install libmysqlclient-dev -y
```

패키지 설치 후 다시 mysqlclient를 설치해준다.

#### ![image](https://user-images.githubusercontent.com/52814897/79878022-e5aafa00-8427-11ea-9e80-80e9c9acb523.png)

우분투에서도 프로젝트가 정상 작동하는 것을 확인했다.

## WSGI 

> **WSGI(Web Server Gateway Interface)**
>
> WSGI는 웹 서버와 웹 어플리케이션의 인터페이스를 위한 파이썬 프레임워크이다. 기존의 파이썬 웹 애플리케이션 프레임워크는 웹서버를 선택하는데 있어 제약이 있었으나, WSGI는 low-level로 만들어져 웹 서버와 웹 애플리케이션, 프레임워크간의 벽을 허물었다. - Wikipedia

즉, 시스템 아키텍쳐에서 Web server와 WAS가 서로 소통하기 위해, 그 사이에 WSGI라는 interface가 들어간다고 생각하면 되겠다.

![image](https://user-images.githubusercontent.com/52814897/79706711-22c29f80-82f5-11ea-85d3-3beb3bb09987.png)

### Gunicorn 설치하기

여기서는 Django에서 WSGI server로 이용되는 프레임워크 중 Gunicorn을 사용하려고 한다. uWSGI보다 좀 더 가벼우면서 속도는 비슷하다고 하는데, 사실 설정이 좀 더 쉬워서 사용하려고 한다.

가상환경 안에서 gunicorn를 설치해준다.

```bash
(venv) $ pip install gunicorn
```

### gunicorn 설정

gunicorn 설치 후 서비스 파일을 생성 및 수정을 해준다. 이는 backend 서버로 사용될 gunicorn을 백그라운드에서 돌리기 위해서이다.

```bash
$ sudo vi /etc/systemd/system/gunicorn.service
```

![image](https://user-images.githubusercontent.com/52814897/79840507-f2602b80-83f0-11ea-9813-fae7eba94b05.png)

IP를 0.0.0.0 설정하여 외부에서도 접속이 가능하게 하였고, 8085포트로 설정하였다. 아래 명령어를 통해 실행 시킨다.

```bash
$ sudo systemctl daemon-reload
$ sudo systemctl start gunicorn
$ sudo systemctl enable gunicorn
```

루트 주소에 routing 해 놓은 것이 없어서 page not found가 뜨긴하지만, public IP를 이용하여 윈도우에서 접속하면 배포가 된 것을 알 수 있다. 

![image](https://user-images.githubusercontent.com/52814897/79877364-1a6a8180-8427-11ea-8056-7134bc93a813.png)

## Nginx 설치 및 설정

Nginx는 Vue 프로젝트 기반의 Frontend 단을 배포할 예정이다. 먼저 설치 후 제대로 작동이 되는 지 확인한다.

```bash
$ sudo apt-get install nginx
$ sudo /etc/init.d/nginx start
$ service nginx status
```

![image](https://user-images.githubusercontent.com/52814897/79878181-1c811000-8428-11ea-9f91-dc3d60ff323d.png)

Web browser로 확인은 할 수 없지만, 일단 잘 돌아가고 있는 것처럼 보인다.

### 설정하기

먼저 Nginx를 세팅하는 데 있어 기억해야할 폴더 2개가 있다.

1. /etc/nginx/sites-available : 실제 라우팅 설정 파일이 있는 곳으로, 초기 설치 시에는 `default`라는 파일이 하나 있을 것이다.
2. /etc/nginx/sites-enabled : `sites-available` 폴더에 있는 파일의 심볼릭 링크 파일(바로가기 파일)을 만들 폴더이다. 설정 파일이 여기 들어와야 활성화가 시작되므로, sites-available에서 설정 파일 작성 후 sites-enabled 폴더에 심볼릭 링크 파일을 만들어야 설정이 완료되는 것이다.(한 번 생성된 심볼릭 링크 파일은 원본의 내용을 수정하면 같이 바뀐다. 물론 그 반대도 적용된다.)

`sites-available` 폴더에서 `default` 파일을 복사하거나 아니면 아무 이름으로 새로운 파일을 만들고 내용은 수정한다. 아래는 필수적인 옵션들만 적어놨다.

```vim
# vue-project
server {
    listen      80;
    server_name [public ip];
    
    charset utf-8;
    
    root    [build 폴더 경로];
    index   index.html index.htm;

    location / {
      try_files $uri $uri/ =404; 
		}
}
```

- listen : 통신에 사용될 서버 포트 번호이다. 주로 80 - http / 443 - https / ssh - 22 / DB - 3306로 사용되는데, 내 경우에는 http 통신이기 때문에 80을 사용하였다.
- server_name : aws ubuntu의 public ip 주소를 써주면 된다.
- root : vue의 경우 dist 폴더의 경로를 써주면 된다.

location block 부분은 요청에 맞는 uri 주소가 있는지 확인하고, 없으면 404 에러를 표시해주는 역할을 한다. 근데 문제는 SPA의 경우 가질 수 있는 uri 주소는 사실 root 하나이고, routing이 아닌 렌더링을 하는 방식이기 때문에 새로고침을 하게 될 경우 항상 404 에러를 발생시킨다.

![image](https://user-images.githubusercontent.com/52814897/79759397-972f2a00-8359-11ea-985e-cbb21d0e4389.png)

아래와 같이 바꿔주면 새로고침을 해도 404 에러가 나지 않는다.

```vim
location / {
      try_files $uri $uri/ /index.html; 
}
```

설정 파일을 만들었으니 이제 심볼릭 링크를 생성해야 한다. 위에서 말한 것과 같이 sites-enabled 폴더에 생성하면 된다.

```bash
$ ln -s /etc/nginx/sites-available/[파일명] /etc/nginx/sites-enabled/[파일명]
```

그리고 nginx를 재시작해준다.

```bash
$ service nginx restart
```

이제 윈도우나 다른 기기에서 public ip 주소로 접속해서 잘 동작하는 확인을 해보자.

![image](https://user-images.githubusercontent.com/52814897/79761274-2b01f580-835c-11ea-97d5-fa85fe0bbe15.png)

![image](https://user-images.githubusercontent.com/52814897/79879198-57377800-8429-11ea-90fa-35b007de3cf0.png)

nginx에 배포된 vue 프로젝트가 axios 요청을 통해 gunicorn에 배포된 backend로 부터 응답을 잘 받으며 정상 동작한다.

## 보완점

Frontend와 Backend 모두 aws ubuntu 서버에서 잘 배포되었는데, 사실 이대로 끝내면 안된다. 내가 원하던 동작이 아니다.

나는 외부에서 nginx로는 접근을 허용해도, gunicorn. 즉, backend에는 접근을 못하게 막고 싶다. Gunicorn 환경설정에서 ip를 내부ip로 바꾸고, localhost로 바꾸기도 해봤지만 실패하였다. proxy pass와 관련된 부분인 것 같은데 nginx 환경 설정에서 proxy_pass를 gunicorn으로 연결했을 경우에 80포트로 접근해도 vue의 index.html을 건너뛰고 무조건 gunicorn 서버로 보내버린다.

위의 마지막 사진처럼 개발자 도구를 찍었을 때, 유저는 웹에서 서버로 어떤 요청(Request URL)을 보내는지 알면 안된다.