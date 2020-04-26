# Django + Vue AWS 서버 배포하기(3) - TroubleShooting

## MySQL 연동 오류

Django 프로젝트와 MySQL을 연동하기 위한 mysqlclient를 설치할 때 발생하는 오류이다.

![image](https://user-images.githubusercontent.com/52814897/79877872-bd230000-8427-11ea-84f8-53e9a12a9b3e.png)

mysqlclient를 설치하기 위해서는 추가 패키지 설치가 필요하다.

```bash
$ apt-get install libmysqlclient-dev -y
```

패키지 설치 후 다시 mysqlclient를 설치해준다.

## PIP Cache 경고

linux에서 pip3 install -r requirements.txt를 진행할 시 발생하는 문제이다. 

![image](https://user-images.githubusercontent.com/52814897/80068402-84e00680-857a-11ea-9abc-3910b00f7333.png)

두 가지의 원인이 있을 수 있다고 한다.

1. cache를 저장할 공간이 부족하여 나타날 수 있다.
2. 이전에 설치된 패키지들에 의해 생성도니 캐시가 새로 설치되는 패키지들과 꼬이는 경우가 있다고 한다.

해결 방법은 캐시를 모두 지우고 다시 설치해주면 된다.

```bash
$ rm -rf ~/.cache/pip
```

## Wheel package 에러

![image](https://user-images.githubusercontent.com/52814897/80069117-c9b86d00-857b-11ea-9ce0-2bd1fba2bb53.png)

윈도우에서는 설치가 필요하지 않았던 `wheel`이라는 package가 없어 발생하는 에러이다.

wheel을 설치해주면 된다.

```bash
$ pip3 install wheel
```

## Open CV 설치 오류

파이썬에서 `import cv2`를 위한 open cv를 설치할 때 발생하는 오류이다.

![image](https://user-images.githubusercontent.com/52814897/80070789-857a9c00-857e-11ea-8d57-d5cdf8960a50.png)

어떠한 python package를 설치하는 과정에서 GUI를 사용하지 않는 Headless 패키지가 포함되어 있고, 그래픽에 관련된 라이브러리를 지워버려서 생기는 에러라고 한다.

필요한 라이브러리를 다시 설치하고 다시 opencv를 설치 해준다.

```bash
$ apt-get update
$ apt-get install -y libsm6 libxext6 libxrender-dev
$ pip3 install opencv-python
```

## 그 외...

위의 에러를 고치를 과정에서 우분투 서버의 가상환경에 여러 패키지를 설치하였다.

그래서 나는 당연히 리눅스와 윈도우의 가상환경 패키지들을 맞춰주고 싶어 `pip3 freeze > requirements.txt`를 이용해 패키지를 저장한 후, 우분투 서버의 requirements.txt를 윈도우 장고 프로젝트에 복사하였다.

그리고 윈도우와 우분투 환경을 일치시키기 위해 장고 프로젝트 가상환경에서도 `pip install -r requirements.txt`를 했는데 아래와 같은 에러가 뜬다.

![image](https://user-images.githubusercontent.com/52814897/80077883-135b8480-8589-11ea-8657-ea5225bdbb4e.png)

원인은 OS가 다르기 때문이다.

우분투에서 추가적으로 설치한 패키지가 윈도우에서는 필요하지도 않고, 존재하지도 않는 패키지일 수가 있다.

OS 자체가 다르기 때문에 윈도우와 리눅스에서 사용되는 Django의 가상환경을 완벽하게 일치시킬 순 없다. 기본적인 필수 패키지 외에는 리눅스와 windows의 가상환경을 다르게 적용해야할 것 같다.

## (추가)

## Error Code 413

![image](https://user-images.githubusercontent.com/52814897/80309763-e40b7880-8811-11ea-8b10-e354d3ef2722.png)

Nginx를 통해 배포된 Frontend단에서 Client가 Image 파일을 업로드 할 때 발생하며, 파일의 용량이 초과하여 발생하는 에러이다.

이상한 점이 있다면 비슷한 용량의 이미지 파일을 Web Brower에서 업로드 했을 경우는 413에러가 발생하지 않았는데, 핸드폰에서 Chrome을 통한 이미지 업로드 시에 위와 같은 에러가 발생했다.

해결 방법은 Nginx에 아래와 같이 `client_max_body_size`에 대한 설정을 해주면 된다.

![image](https://user-images.githubusercontent.com/52814897/80309923-e91cf780-8812-11ea-8d2e-388acd984bf7.png)



