# [Ubuntu] D 드라이브에 우분투 설치하기

## 부팅 USB 만들기

## 파티션 나누기 및 설치하기

## 우분투 저장소 서버 변경하기

여기까지 우분투를 막 설치를 마쳤으면 가장 먼저 해야할 일이 있다. 바로 우분투의 저장소 서버(kr.archive.ubuntu.com)를 변경해 주는 것이다.

### 왜 변경할까?

가장 큰 이유는 인터넷 속도이다. 서버를 변경하지 않으면 package 등을 설치할 때 아주 느리거나, 아니면 아예 설치가 안된다. 나의 경우 python과 사용할 pip3를 설치하려고 했는데 계속된 설치 오류가 났고, 우분투의 저장소 서버를 한국 서버로 바꿔주니 해결되었다.

### 저장소 변경하기

두 가지 방법이 있다. 둘 중 편한 방법을 사용하자.

#### 터미널 명령어

터미널에서 vi 에디터를 통해 apt를 다운 받는 서버의 리스트를 확인할 수 있다.

```bash
$ sudo vi /etc/apt/sources.list
```

여기서 아래의 리눅스 치환 명령어를 이용해 기존 서버 주소(kr.archive.ubuntu.com)를 변경할 수 있는데, 한국에서는 주로 daum 서버를 사용하는 것 같다.

```vim
# :%s/[바꿀 문자열]/[바뀔 문자열]/g (g는 global의 약자로 현재 파일의 모든 라인에 걸쳐 수행)
:%s/kr.archive.ubuntu.com/ftp.daum.net/g
```

변경 후 적용 및 확인을 위해 update와 upgrade를 해준다.

```bash
$ sudo apt-get update & sudo apt-get upgrade
```

#### GUI 이용

그냥 편하게 GUI를 사용하자. 메뉴에서 `Software & Updates`를 검색해 실행한다.

![image](https://user-images.githubusercontent.com/52814897/79639534-6919e080-81c7-11ea-8569-b78f62028972.png)

실행 후 Download from란의 서버 주소를 클릭 후 `other`을 클릭한다.

![image](https://user-images.githubusercontent.com/52814897/79639572-9f576000-81c7-11ea-9362-e7dfc772e01a.png)

그 후 `select best server`를 클릭하면 알아서 최적의 서버를 찾아준다.