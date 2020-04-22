

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

