

# Django + Vue AWS 서버 배포하기(2)(WSGI, AWS)

## 개요

지난 글에서 Frontend = Nginx / Backend = Gunicorn 에 배포하였고, 외부에서 backend 서버로의 접근을 차단하는 해결책을 찾지 못하였다. 주변의 도움을 받았고 해결책은 생각보다 간단했지만, 전반적인 Nginx에 대한 이해가 적었기 때문에 해결책에 접근을 못했던 것 같다.

그 개념을 잡기 위해선 먼저 Proxy에 대한 이해가 필요하다.

## Proxy Server

> 영어단어 proxy는 '대리'라는 뜻을 가지고 있으며, 네트워크 분야에서 쓰이는 Proxy Server는 클라이언트가 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해주는 컴퓨터 시스템 또는 응용 프로그램을 가리킨다. - Wikipedia

즉, Proxy server는 client와 서버 사이의 중계기 역할이며, 나의 경우에는 Frontend 를 배포한 Nginx가 proxy server의 역할도 할 수 있다.

## 왜 쓸까?

원래 프록시 서버의 목적은 외부 요청에 대한 트래픽을 줄여 병목 현상을 방지함으로써 데이터 전송 시간을 절약하는데에 있다고 한다. 한 번 요청된 내용을 프록시 서버에 **캐시**를 이용하여 저장하고 같은 요청에 대해서는 서버로 접속 없이 저장된 데이터를 보내준다고 한다.

두번째 이유는 보안이다. 나의 경우에는 외부에서 서버의 콘텐츠를 막을 목적으로 사용하였지만, 사실 IP 추적 자체를 막기위해 사용한다.

나는 aws linux 서버에 아직 Domain이 없어 어쩔 수 없이 aws 서버의 public ip를 사용하였지만, Domain이 있다면 아래처럼 공개되는 Request URL을 철저히 가림으로써 IP를 숨길 수 있다.

![image](https://user-images.githubusercontent.com/52814897/79879198-57377800-8429-11ea-90fa-35b007de3cf0.png)

## 본론으로...

### Gunicorn 로컬 재배포

앞서 말했 듯, 나의 목적은 단순히 외부에서 aws서버에 배포된 django 프로젝트의 접근을 차단하는 것이었다. 그러므로 외부에서는 접근도 못하게 그냥 localhost로 배포해 버리자.

```bash
$ sudo vi /etc/systemd/system/gunicorn.service
```

![image](https://user-images.githubusercontent.com/52814897/79961658-fe67ee00-84c1-11ea-9b89-5e9d621e8d00.png)

Gunicorn 설정을 바꿔도 바로 적용되지 않으므로, 기존에 돌아가고 있는 gunicorn 프로세스를 종료시킨 후 재시작 해야한다.

```bash
$ ps aux | grep gunicorn
$ kill [gunicorn 프로세스 번호]
```

재시작

```bash
$ sudo systemctl daemon-reload
$ sudo systemctl start gunicorn
$ sudo systemctl enabel gunicorn
```

변경한 ip로 잘 배포가 됐는지 확인한다.

```bash
$ systemctl status gunicorn.service
```

![image](https://user-images.githubusercontent.com/52814897/80273114-82acb200-870a-11ea-904b-e1f84fc9df43.png)

초록불로 `active (running)`이 뜨면 gunicorn이 로컬로 잘 돌아가고 있는 것이다.

### Ngixn Reverse Proxy 설정

**Reverse Proxy**는 외부에서 내부 서버 접근 시, Proxy server를 통해 요청에 맞는 정보를 매핑시켜 주는 방식이다. Nginx에서는 이러한 Reverse Proxy를 위해 `proxy_pass`라는 환경 변수를 제공한다.

지난 글에서 nginx 설정 파일에서 `location / {...}` 블록이 있었는데, 이는 루트(/), 즉 기본 IP주소로 요청이 들어왔을 때의 응답에 대한 로직이었다.

그렇다면, 아래와 같은 location 블록은 무엇을 의미할까?

```
location /[아무거나]/ {
	...
}
```

위의 코드는 `http://[IP주소]/[아무거나]/`로 요청이 들어왔을 때의 어떤 처리를 할 지에 대한 부분이다.

아래의 코드는?

```
location /[아무거나]/ {
	proxy_pass http://127.0.0.1:8085/[아무거나]/;
}
```

`http://[IP주소]/[아무거나]/`로 요청이 들어오면, linux 서버의 8085포트를 가지는 서버에 매핑시켜준다는 의미이고, 8085포트는 위에서 Gunicorn을 이용해 Django backend 서버가 배포된 포트 번호이다.

따라서, 나의 경우 전체적인 nginx의 설정 파일은 다음과 같아진다.

```
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
    location /recipes/ {
		proxy_pass http://127.0.0.1:8085/recipes/;
	}
}
```

즉, 아래처럼 vue 프로젝트에서 `/recipes/`로 시작하는 요청 주소를 `http://127.0.0.1:8085/recipes/~~~` 주소로 바꿔버린다는 뜻이다.

```javascript
axios.get('http://[public ip]/recipes/~~~')
```

이렇게 하면 axios 요청시 포트번호를 기입할 필요없이 그냥 public ip또는 도메인만 적으면 되므로

![image](https://user-images.githubusercontent.com/52814897/80273858-f18d0980-8710-11ea-85af-8f7cdb6c3b70.png)

위 사진처럼 개발자 도구에서 찍어봐도 실제 내부 서버의 포트번호 또한 공개되지 않는다.

