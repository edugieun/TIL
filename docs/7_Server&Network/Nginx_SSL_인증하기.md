# Nginx SSL(TLS) 인증하기

## SSL(TLS) 인증하는 이유?

SSL 인증을 하는 이유는 기존의 HTTP 통신을 HTTPS 으로 바꾸기 위함이다.

HTTP(Hyper Text Transfer Protocol)는 웹과 서버가 통신하기 위한 가장 기초적이고 단순한 프로토콜인데 기본적으로 텍스트 교환이며 HTML 페이지 또한 이 텍스트에 포함되어 전달된다.

즉, 암호화가 되어있지 않기 때문에 쉽게 도청이나 해킹의 위협을 받을 수 있다.

반면에, HTTPS(Hyper Text Transfer Protocol over Secure Socket Layer)는 이름에서도 알 수 있듯이 HTTP 통신에 SSL(Secure Socket Layer) 기술을 덧붙여 보안이 강화된 인터넷 통신 프로토콜이다.

정식으로는 SSL 기술 기반으로 표준화시킨 프로토콜인 TSL(Transport Layer Security)를 사용해 암호화된 통신 프로토콜을 HTTPS라고 하나, TSL보다는 SSL라는 용어로 많이 쓰인다.

## Certbot 설치하기

Certbot은 인증서 발급 프로그램이다. 실질적으로 TLS 인증서를 발급해 주는 곳은 **Let's Encrypt**라는 비영리기관이며, Let's Encrypt에서 추천하는 프로그램이자 인증서 발급 과정에서의 복잡한 프로세스를 한 번에 처리할 수 있는 인증서 발급 프로그램이 Certbot이다.

### 서버 버전 확인

먼저 `cat /etc/issue` 명령어로 자신이 사용하고 있는 서버의 버전을 알아보자.

![image](https://user-images.githubusercontent.com/52814897/80793317-c3586f80-8bd1-11ea-84ca-664bc262ba1c.png)

### Certbot 설치

다음으로 Certbot 공식 홈페이지에서 사용하는 Web Server와 서버 버전을 선택해주면

![image](https://user-images.githubusercontent.com/52814897/80793432-0f0b1900-8bd2-11ea-864e-a191587affc9.png)

certbot 레지포토리를 등록하고 해당 웹 서버에 맞는 certbot을 설치할 수 있는 명령어가 나온다.

![image](https://user-images.githubusercontent.com/52814897/80793699-c9028500-8bd2-11ea-9136-78a1da25be67.png)

### 인증서 설치 및 Nginx 자동 설정

나처럼 현재 Nginx를 이용한 Web Server가 HTTP로 배포되어있는 경우, 고맙게도 자동으로 설정해주는 명령어가 존재했다.

![image](https://user-images.githubusercontent.com/52814897/80795697-32d15d80-8bd8-11ea-9d59-d57572bdeedf.png)

명령어를 실행하면 아래처럼 현재 http로 배포되어있는 도메인을 선택할 수 있는 화면이 나온다.

![image](https://user-images.githubusercontent.com/52814897/80795740-57c5d080-8bd8-11ea-987b-39d4f68d0d44.png)

도메인을 선택해주면 다음으로는 http로 요청이 들어왔을 경우 바로 https로 리다이렉트 시켜줄 지 선택하라는 화면이 나온다.

편하게 바로 리다이렉트 해버리자.

![image](https://user-images.githubusercontent.com/52814897/80795827-978cb800-8bd8-11ea-844c-221dd8a65992.png)

다음과 같은 화면이 나오면 성공적으로 https로 변환이 완료된 것이다.

![image](https://user-images.githubusercontent.com/52814897/80795950-ee928d00-8bd8-11ea-9756-38425c659e91.png)

## 확인하기

이제 확인 작업을 해주자. https로 접근했을 경우 정상적으로 페이지가 열리며, http 접근하면 자동적으로 https 주소로 리다이렉트 시켜준다.

![image](https://user-images.githubusercontent.com/52814897/80796164-79738780-8bd9-11ea-9290-9374b415df0e.png)

### 자동 변경된 Nginx 설정 훑어보기

https 변환 후 자동으로 변경된 Nginx 설정이 궁금해진다.

바뀐 곳은 딱 2군데이다.

### 80포트 redirect

먼저, 80포트. 즉, http 들어오는 요청을 https로 redirect(상태 코드 301) 시켜주는 부분이 생겼다.

![image](https://user-images.githubusercontent.com/52814897/80797081-d3754c80-8bdb-11ea-8961-6efa08ff4e53.png)

### 443 포트 및 인증서 경로 설정

두번째로는 내가 기존에 설정한 80포트(listen 80)가 443포트(listen 443)으로 바꼈으며, 그 아래에는 인증서의 경로를 지정해주는 파라미터들이 생성되었다.

![image](https://user-images.githubusercontent.com/52814897/80797278-61513780-8bdc-11ea-967e-669d12bb7980.png)

이처럼 Certbot은 한 번의 명령으로 번거로운 Nginx 설정 작업을 자동으로 해주는 고마운 프로그램이다.

## Mixed Content Error

위의 모든 과정을 마친 후 서비스 기능을 테스트하다보면 아래처럼 혼합 콘텐츠 에러를 마주할 수 있다.

![image](https://user-images.githubusercontent.com/52814897/80796584-8a70c880-8bda-11ea-8e44-50321ef0d043.png)

혼합 콘텐츠 에러는 서로 다른 프로토콜. 즉, https에서 http로 요청을 보내거나 http에서 https로 요청을 보낼 때 발생하는 에러이다.

따라서 우리는 Vue Frontend단에서 axios 요청을 보내는 주소를 변경해줄 필요가 있다.

![image](https://user-images.githubusercontent.com/52814897/80796733-f0f5e680-8bda-11ea-95da-ad041863ac35.png)

기존의 http 주소를 https로만 바꿔주기만 하면 모든 요청과 기능이 정상적으로 동작하는 것을 볼 수 있다.

