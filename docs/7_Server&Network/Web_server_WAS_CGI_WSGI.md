# Web Server, WAS, WSGI 이해하기

프로젝트를 진행하면서 내가 개발하는 프로젝트의 전반적인 구성에 대한 이해가 필요하다고 느꼈다.

Frontend 개발자로 첫 프로젝트를 했을 때는 그저 Backend를 담당한 팀원이 '이 IP로 axios 요청 보내'라고 하면 그러려니 생각했는데, 두번째 프로젝트에서 Backend 개발자로 서버를 구축하다보니 '생각보다 뭐가 좀 많다...'라고 느꼈다. 그래서 Web Application 개발에 있어서 얕게나마 그 구성에 대해 살펴보려 한다.

## 시스템 아키텍처(System Architectur)

> 시스템 아키텍처(system Architecture)는 시스템의 구조, 행위, 더 많은 뷰를 정의하는 **개념적 모형(conceptual model)**이다. 시스템 목적을 달성하기 위해 시스템의 각 컴포넌트가 무엇이며 어떻게 상호작용하는지, 정보가 어떻게 교환되는지를 설명한다.
>
> 시스템 아키텍처에 대한 정의는 다양한데, 종합하면 다음의 기본 요구 사항이 있다.
>
> - 시스템 구성 및 동작 원리를 나타내고 있다.
> - 시스템 구성 요소(부품)에 대한 설계 및 구현을 지원하는 수준으로 자세히 기술된다.
> - 구성 요소 간의 관계 및 시스템 외부 환경과의 관계가 묘사된다.
> - 요구 사양 및 시스템의 전체 수명주기를 고려한다.
> - 시스템 전체(하드웨어와 소프트웨어를 포괄한 것)에 대한 논리적인 기능 체계와 그것을 실현하기 위한 구성 방식. 시스템의 전체적인 최적화를 목표로 하고 있다.
>
> 출처 - Wikipedia

위키피디아를 읽어봐도 사실 시스템 아키텍처의 개념이 잘 각인되지 않는다. 블로그나 이미지를 봐도 너무 다양하고 다른 구성도를 가지고 있다. 정말 다양하다.

**개념적 모형(conceptual model)**이란 것은 구성도, 도표, 모형, 패턴처럼 시각화된 것일 수도 있고, 계획, 설명같이 글로 되어 있을 수도 있고 또는 수학 공식으로 되어 있을 수도 있다. 너무나도 어렵다.

그래서 이 한 줄로 시스템 아키텍처를 이해하기로 했다.

> 시스템 아키텍처에 대한 정의는 다양하다. - Wikipedia

확실한 건 누군가가 내가 그린 **시스템 아키텍처**라는 것을 봤을 때, 예를 들면 내가 만든 웹 어플리케이션의 구성도를 봤을 때, '프론트앤드와 백앤드가 뭘로 만들고 어떻게 구성되어 있구나.' 라고 생각하게 만들어야 한다는 것은 이해하였다.

### 웹 어플리케이션 시스템 아키텍처

![image](https://user-images.githubusercontent.com/52814897/79706711-22c29f80-82f5-11ea-85d3-3beb3bb09987.png)

## Web Server

> 웹 서버(Web Server)는 HTTP를 통해 웹 브라우저에서 요청하는 HTML 문서나 오브젝트(이미지 파일 등)을 전송해주는 서비스 프로그램을 말한다. - Wikipedia

웹 서버는 클라이언트(웹 브라우저)와 직접적인 통신을 하는 프로그램이다. 주로 그림, CSS, Javascript, HTML 문서 등 **정적 콘텐츠**를 클라이언트에게 제공해준다. 물론 동시에 클라이언트로부터 콘텐츠를 전달 받는 역할도 한다.

자원을 효율적으로 사용하고, WAS로의 부하를 줄이기 위해 사용된다고도 하며 그 외에도 Virtual Hosting, 대용량 파일 지원, Bandwidth Throttling, Server-side scripting 등의 기능을 수행한다.

자주 사용하는 Web Server Program은 아파치, IIS, Nginx, GWS 등이 있다.

## WAS(Web Application Server)

> 웹 애플리케이션 서버(Web Application Server, WAS)는 웹 애플리케이션과 서버 환경을 만들어 동작시키는 기능을 제공하는 소프트웨어 프레임워크이다. - Wikipedia

> An application server runs behind a web Server(e.g. Apache or Microsoft Internet Information Services (IIS)) and (almost always) in front of an SQL database (e.g. PostgreSQL, MySQL, or Oracle). - wikipedia

영어권에서는 Application Server라고도 부른다. 주로 웹 서버가 할 수 없는 로직처리나 DB 조회 등 **동적 콘텐츠**를 제공하는 역할을 한다.

자바 기반의 아파치 톰캣처럼 웹 어플리케이션을 서비스할 수 있는 환경이나 서버 자체를 만들어 준다.

파이썬으로 따지면 uWSGI나 Gunicorn 처럼 Django, Flask가 구동될 수 있는 환경을 만들어 준다.

서버 또는 환경 그 자체를 말하기도 하며, 영문 Wikipedia의 정의처럼 Web Server와 WAS를 별개의 서버 구성으로 보기도 하고, Web Server를 포함한 개념으로도 사용된다.

## WSGI

> 웹 서버 게이트웨이 인터페이스(WSGI, Web Server Gateway Interface)는 웹 서버와 웹 애플리케이션의 인터페이스를 위한 파이썬 프레임워크다. - Wikipedia

WSGI는 웹 서버와 통신하기 위한 일종의 통신 규약이며 주로 파이썬으로 구성된 Web application과 웹 서버의 통신을 위해 사용된다.

### WSGI Server

uWSGI나 Gunicorn과 같이 WSGI 규약을 사용하여 구성된 서버나 환경으로 WAS와 같거나 비슷한 개념으로 봐도 무방할 것 같다.

Flask 공식 홈페이지에서는 다음과 같이 설명한다.

> uWSGI is both a protocol and an application server. - Flask Web Site

즉, uWSGI나 Gunicorn으로 생성된 서버가 통신 규약인 동시에 WAS라고 말하고 있다.

Web Server, WAS, WSGI Server의 관계를 시스템 아키텍처로 그려보자면 아래 두 개 정도의 느낌이라 생각된다.

물론 정확하진 않다..

![image](https://user-images.githubusercontent.com/52814897/80385514-19cb6280-88e1-11ea-9b08-e3fd6cb1585b.png)

![image](https://user-images.githubusercontent.com/52814897/80385452-091aec80-88e1-11ea-8a31-a59da44d65d7.png)

현업에 대한 경험이 없어서 그런지, 시스템 아키텍처도 그렇고 WAS도 그렇고 뭔가 수학 공식처럼 딱 맞아떨어지는 듯한 정의가 아닌 개념에 대한 설명 같은 느낌이라 이해하기가 어려운 것 같다.