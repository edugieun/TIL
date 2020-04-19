# [Ubuntu] D 드라이브에 우분투 설치하기

## 부팅 USB 만들기

먼저 ubuntu 설치를 위한 USB를 만들어야 한다. 우분투 공식 홈페이지에서 LTS버전을 다운 받는다.

[Ubuntu 공식 홈페이지](https://ubuntu.com/#download)

![image](https://user-images.githubusercontent.com/52814897/79689679-566bde00-8291-11ea-9943-ce609bf89a4e.png)

Rufus라는 프로그램을 이용하여 부팅 및 다운로드용 USB를 만든다.

[Rufus.ie](https://rufus.ie/)

![image](https://user-images.githubusercontent.com/52814897/79689719-90d57b00-8291-11ea-970e-193a0b6109d4.png)

다운 받은 ubuntu.iso 파일을 선택 한 후, 시작을 누르면 자동으로 부팅 usb를 만들어준다.

![image](https://user-images.githubusercontent.com/52814897/79689801-0e00f000-8292-11ea-9f3b-d757462172ff.png)

부팅 usb가 준비되었다면 usb로 부팅을 해야 하는데, 컴퓨터를 다시시작 한 후, `boot menu`로 들어가는 키를 누르면 된다. 이는 메인보드마다 차이가 있으므로 컴퓨터 부팅 시 나오는 키 안내를 보거나, 구글에 검색해보자. ASRock의 경우는 `del` 키를 이용하면 부트 메뉴로 들어갈 수 있다. 부트 메뉴에서 우분투가 설치된 USB를 선택한다.

## 파티션 나누기 및 설치하기

### 디스크 볼륨 축소하기

나의 경우 C드라이브는 Windows10을 유지하고, D드라이브의 반은 개인적인 파일을 보관할 저장소, 나머지 반에 해당하는 용량에 우분투를 설치하고자 했다.

그러기 위해서 먼저 통으로 잡혀있는 D드라이브의 용량을 축소시켰다. windows10을 기준으로 윈도우 아이콘을 오른쪽 클릭하면 디스크 관리에 들어갈 수 있다.

![image](https://user-images.githubusercontent.com/52814897/79690077-90d67a80-8293-11ea-8d24-b5a8ac4de11e.png)

나처럼 디스크의 일부분만 우분투로 사용하고 싶을 경우에는 통으로 잡혀있는 저장소의 볼륨 축소를 통해 우분투 용량을 확보해야 한다.

### 파티션 나누기 및 우분투 설치하기

부트 메뉴를 통해 우분투 설치 화면까지 왔다면 다음은 파티션을 나누는 부분인데, 파티션 분할의 기준은 사람마다 많이 차이가 있다. 파티션을 나누고 안 나누고는 개인 취향인데, 파티션을 나누지 않을 경우 파일 보관이나 포맷할 상황이 올 경우 난감해질 수 있다.

일반적으로 4가지 구역으로 분할한다.

1. Boot Partition : Primary/Ext4. booting시 필요한 파일들이 들어가 있는 파티션이다. 용량을 많이 차지하지 않기 때문에 500MB ~ 1GB 정도 할당한다.
2. Swap area : Primary/swap area. RAM의 용량이 가득 찼을 때 사용되는 여유 공간으로  보통 RAM 메모리의 2배라고 해서 나는 10GB 정도 잡았는데... 이는 옛날 얘기라고 한다. 예전에 RAM이 작을 때나 넉넉하게 2배라고 했지, 요즘은 메모리 용량이 하도 커서 swap area를 아예 안 잡는 사람도 있고, 잡아도 최대 2GB를 넘지 않게 잡는다고 한다.
3. Root(/) Partition : Logical/Ext4. 윈도우의 C:/Windows의 개념이라고 한다. 나중에 더 많은 파티션으로 확장이 가능하며 현재 사용 가능 용량에 따라 5~20GB 정도로 할당한다.
4. Home Partition : Logical/Ext4. 윈도우의 D 드라이브 또는 C:/Program Files. 즉, 사용자가 실질적으로 설치하는 응용프로그램들이 설치되는 공간이다. 나머지 용량을 모두 할당한다.

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