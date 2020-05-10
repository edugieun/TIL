# 소켓(Socket) 통신 (1) - 개요 및 개념이해

첫번째 프로젝트에서 마크다운 기반 텍스트의 실시간 전달을 위한 기능을 만들 필요가 있었다. 나는 Vue를 이용해서 Frontend를 담당했고, Backend를 맡은 팀원은 Spring boot를 사용했다. 당시 소켓 통신이 뭔지도 모르고 일단 프로젝트 완성에 급급하여 구글을 뒤져가며 구현을 하긴 했는데, 자소서를 쓰다 소켓 통신에 대해 언급하려고 하니 개념조차 모르고 있다는 걸 깨달았다. Backend에선 어떤 원리로 소켓 통신을 처리하는지 몰랐기 때문인 것 같다.

때문에, 소켓 통신에 대한 이해도 하고 복습도 할 겸, Django와 Vue를 이용하여 간단한 소켓 통신을 구현하려 한다.

## 소켓(Socket)이란?

소켓은 2가지의 의미를 가지고 있다.

### 물리적 소켓

나처럼 전자, 전기과를 나온 사람에게 소켓이라 함은 IC 칩을 쉽게 꽂고 빼기 위한 이런 소켓을 생각할 것 같다.

![image](https://user-images.githubusercontent.com/52814897/81397462-58271400-9162-11ea-91aa-fe7a6b097ea2.png)

나 역시 소켓 통신이 센서(Sensor) 통신처럼 소켓이라는 물리적 장치를 통해 통신을 하는 것이라고 생각하고 있었다.

### 네트워크 소켓(인터넷 소켓)

> 네트워크 소켓(network socket)은 컴퓨터 네트워크를 경유하는 **프로세스 간 통신의 종착점**이다. - Wikipedia

소켓 통신에서 말하는 소켓은 네트워크 소켓에 관한 개념이다.

소켓은 프로세스가 실행될 때 생성되는 **통신 접속점**이다. 좀 더 쉬운 이해를 위해 은행에 비교하자면, 은행 업무 처리를 위해 은행원과 만나게 되는 창구가 소켓이라고 이해하면 될 것 같다.

## 소켓의 구성

소켓은 크게 3가지로 구성된다.

- 인터넷 프로토콜 : TCP, UDP, Raw IP
- IP 주소 : 로컬(나의 IP) + 원격(상대방 IP)
- Port 번호 : 로컬(나의 포트번호) + 원격(상대방 포트번호)

또한 프로토콜에 따라 TCP 또는 UDP 두 개의 타입으로 분류할 수 있는데, 이는 프로토콜에 대한 글에서 따로 다룰 예정이다.

## 왜 사용할까?

그렇다면 소켓 통신은 언제 사용할까?

글에서 처음 언급했던 것처럼 진행했던 프로젝트에서 클라이언트와 서버의 요청/응답에 상관없이 데이터를 1:N으로 실시간 전송하는 기능을 필요로 했다. 비슷하게 채팅 서비스에서도 많이 사용된다.

### 그냥 HTTP 통신으로는 안될까?

## Socket과 WebSocket

https://www.google.com/search?q=socket+websocket+difference&oq=sock&aqs=chrome.0.69i59l2j69i57j69i59j0j69i60l3.3303j1j4&sourceid=chrome&ie=UTF-8

https://stackoverflow.com/questions/16945345/differences-between-tcp-sockets-and-web-sockets-one-more-time

### Socket 통신

- 소켓 통신은 일반적으로 TCP/IP 또는 UDP 프로토콜을 이용한다.
- 소켓 통신은 WebSocket을 이용할 수도 있다.

### WebSocket 통신

- WebSocket은 TCP, UDP를 사용하는 Transport Layer에서 실행되는 소켓이 아닌 HTTP를 사용하는 Application Layer에서 실행되는 소켓이다.
- 기존 단방향 통신인 HTTP 통신을 보완하기 위해, Polling 방식을 이용해 실시간 통신처럼 **보이게 하는** 통신 방법이다.
- 이후 실제로 실시간 양방향 통신이 가능한 웹소켓이 2011년 표준화되었다. HTTP 풀링과 같은 반이중방식이 아닌 전이중방식을 사용하는 새로운 프로토콜이다.
- 웹소켓은 TCP 80, 443포트를 사용하며, HTTP 프로토콜과 호환된다.
- 웹소켓이 기존 HTTP 통신을 대체하지는 않는다.
- 웹소켓은 소켓 통신과는 다른 별개의 프로토콜이다.

### 공통점

- IP와 Port를 통해 통신한다.

### HTTP와의 차이

- HTTP는 반이중 통신 / 웹소켓은 전이중 통신이다.



https://www.slideshare.net/deview/django-websocket

https://channels.readthedocs.io/en/latest/

