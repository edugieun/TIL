

# Django + Vue AWS 서버 배포하기(WSGI, AWS)

## Runserver 테스트

먼저 기존의 Window에서 작업한 프로젝트가 AWS 서버에서도 잘 동작하는지 확인해야 한다.

나의 경우 DB관련 에러가 났다. Django 프로젝트와 MySQL을 연동하기 위한 mysqlclient를 설치할 때 발생하는 오류이다.

![image](https://user-images.githubusercontent.com/52814897/79425381-94040900-7ffc-11ea-9dbf-bcf6938839ee.png)

mysqlclient를 설치하기 위해서는 추가 패키지 설치가 필요하다.

```bash
$ apt-get install libmysqlclient-dev -y
```

패키지 설치 후 다시 mysqlclient를 설치해준다.

#### ![image](https://user-images.githubusercontent.com/52814897/79705972-89928980-82f2-11ea-9003-c8bae0c168f6.png)

우분투에서도 프로젝트가 정상 작동하는 것을 확인했다.

## WSGI  설치하기

> **WSGI(Web Server Gateway Interface)**
>
> WSGI는 웹 서버와 웹 어플리케이션의 인터페이스를 위한 파이썬 프레임워크이다. 기존의 파이썬 웹 애플리케이션 프레임워크는 웹서버를 선택하는데 있어 제약이 있었으나, WSGI는 low-level로 만들어져 웹 서버와 웹 애플리케이션, 프레임워크간의 벽을 허물었다. - Wikipedia

즉, 시스템 아키텍쳐에서 Web server와 WAS가 서로 소통하기 위해, 그 사이에 WSGI라는 interface가 들어간다고 생각하면 되겠다.

![image](https://user-images.githubusercontent.com/52814897/79706711-22c29f80-82f5-11ea-85d3-3beb3bb09987.png)

가상환경 안에서 uwsgi를 설치해준다.

```bash
(venv) $ pip install uwsgi
```

### uWSGI 동작 테스트

uWSGI 설치 후, 정상 동작하는지 테스트가 필요하다. 

```bash
$ uwsgi --http :[port] --module [프로젝트명].wsgi
```

[port]에는 열고 싶은 포트를 적거나, 123.45.6.7:8080 와 같이 실행할 ip 주소를 직접 적어줘도 된다. [프로젝트명]은 `wsgi.py` 파일이 들어있는 경로. 즉, `createproject` 명령어를 통해 만든 자기 자신의 프로젝트 이름이다.

Window에서 잘 접속이 되는지 확인하고 싶을 경우 우분투에서 uWSGI를 이용해 private IP로 포트를 열고, public IP를 이용하여 윈도우에서 접속하면 된다.

![image](https://user-images.githubusercontent.com/52814897/79708715-2822e880-82fb-11ea-8246-b8771ffc2dd3.png)

## Nginx 설치 및 설정

이제 Clinet의 요청을 직접 받을 Web server인 Nginx와 WSGI를 연동시켜줘야 한다. 먼저 nginx가 잘 설치되는지 확인하자.

```bash
$ sudo apt-get install nginx
$ sudo /etc/init.d/nginx start
$ service nginx status
```

![image](https://user-images.githubusercontent.com/52814897/79715253-34fd0780-830e-11ea-8577-052a14fa86ee.png)

Web browser로 확인은 할 수 없지만, 일단 잘 돌아가고 있는 것처럼 보인다.

`/etc/nginx/sites-available` 폴더로 이동하여 `[아무 이름].conf` 파일을 생성해준다.



### uWSGI와 Nginx 연동

`/etc/nginx`에 있는 `uwsgi_params` 파일을 프로젝트 폴더에 복사한다.

https://twpower.github.io/41-connect-nginx-uwsgi-django

https://nachwon.github.io/django-deploy-3-nginx/

## Vue + Nginx 배포하기

https://medium.com/@thucnc/deploy-a-vuejs-web-app-with-nginx-on-ubuntu-18-04-f93860219030