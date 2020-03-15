# Redis Cache 사용하기

## 개요

### Cache 사용이유

> 출처 - [위키백과](https://ko.wikipedia.org/wiki/캐시)

캐시(cache)란 데이터나 값을 미리 복사해 놓는 **임시 장소**를 가리킨다. 캐시에 데이터를 미리 복사해 놓으면 더 빠른 속도로 데이터에 접근할 수 있다.

#### 캐시의  종류

##### CPU 캐시

하드웨어를 통해 관리된다.

대용량의 메인 메모리(주로 RAM)로의 접근을 빠르게 하기 위해 CPU 칩 내부나 옆에 탑재하는 작은 메모리이다.

##### 디스크 캐시(또는 디스크 버퍼)

소프트웨어를 통해 관리된다.

대부분의 하드 디스크(HDD)는 디스크 제어와 외부와의 인터페이스를 위해 작은 컴퓨터를 내장하고 있다. 그리고 이 작은 컴퓨터는 디스크에 입출력되는 데이터를 저장하는 작은 메모리를 갖고 있는데, 이를 디스크 캐시라고 한다.

#### 지역성

캐시가 효율적으로 동작하려면, 캐시에 저장할 데이터가 지역성을 가져야 한다. 지역성이란 데이터 접근이 시간적, 혹은 공간적으로 가깝게 일어나는 것을 의미한다.

##### 시간적 지역성

특정 데이터가 한번 접근되었을 경우, 가까운 미래에 또 한번 데이터에 접근할 가능성이 높은 것을 말한다.

메모리 상의 같은 주소에 여러 차례 읽기 쓰기를 수행할 경우 상대적으로 작은 크기의 캐시를 사용해도 효율성을 꾀할 수 있다.

##### 공간적 지역성

특정 데이터와 가까운 주소가 순서대로 접근되었을 경우이다.

CPU캐시나 디스크 캐시의 경우 특정 메모리 주소에 접근할 때, 해당 주소뿐 아니라 해당 주소가 있는 블록 전체를 캐시에 가져오게 된다. 이때 메모리 주소를 오름차순이나 내림차순으로 접근하여 캐시의 효율성을 향상시킨다.

#### Cache의 단점

캐시는 영구적 메모리 공간이 아니기 때문에 언제든 지워질 수 있다.

### Singleton pattern과 Cache

소프트웨어 디자인 패턴에서 싱글턴 패턴(singleton pattern)을 따르는 클래스는, 생성자가 여러 차례 호출되더라도 실제로 생성되는 객체는 하나이고 최초 생성 이후에 호출된 생성자는 최초의 생성자가 생성한 객체를 리턴한다.

이때, 사용되는 것이 캐시이며 최초에 생성된 객체를 캐시에 담고, 같은 요청에 대한 응답으로 캐시에 담긴 객체를 넘겨줌으로써 전체적인 시스템의 처리속도를 향상 시킨다.

## 시스템 아키텍쳐에서 병목현상

![image](https://user-images.githubusercontent.com/52814897/76600552-7dc0e400-654a-11ea-9339-63d6d5a09f36.png)

컴퓨터에서의 병목 현상은 시스템 내 데이터의 집중적인 사용으로 인해, 해당 부분의 성능이 저하되고 전체적인 시스템이 마비되는 현상을 의미한다.

위의 그림처럼 대용량의 DB는 디스크에 저장되어 있고, 디스크는 상대적으로 데이터 처리 속도가 느리기 때문에 시간지연이 발생한다.

## Cache Test 준비

### Django 프로젝트 제작

Cache의 사용과 비교를 위해 간단한 Django 프로젝트 두 개를 준비하였다.

먼저 아래와 같이 HTTP GET 호출을 받았을 경우 모든 글들의 리스트를 보여주는 코드이다.

> 코드 출처 - [nachown](https://nachwon.github.io/redis/)

```python
class PostListView(ListView):
    model = Post
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().values('id', 'title', 'content')
        context = {}
        for i in posts:
            context[f'post_{i["id"]}'] = i
        return JsonResponse(context)
```

이 코드는 매번 HTTP 호출에 대하여 모든 객체를 `context`에 담아 Json 형태로 보여주는 코드이다. 따라서 100번을 호출한다고 하면 100번 모두 context에 모든 글을 담는 동작을 반복하게 된다.

다른 하나는 이런 반복적인 동작을 피하기 위해서 싱글턴 패턴 및 캐시를 사용한 코드이다.

```python
class PostListView(ListView):
    model = Post
    def get(self, request, *args, **kwargs):
        context = cache.get('posts')
        if not context:
            posts = Post.objects.all().values('id', 'title', 'content')
            context = {}
            for i in posts:
                context[f'post_{i["id"]}'] = i
            cache.set('posts', context)
        return JsonResponse(context)
      
#settings.py
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
      # 6379포트를 쓰는 redis 서버의 1번 데이터베이스를 캐시로 사용
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

위 코드 역시 HTTP GET 호출에 대해 모든 글들을 context에 담아 리스트를 보여주는 코드이다. 하지만 캐시를 사용하였기 때문에 최초 1회에 대해서는 기존 코드와 같은 동작을 하지만, 그 이후에는 캐시에 미리 담겨있는 객체를 넘겨주기 때문에 훨씬 효율적이다.

각각 두 개의 프로젝트의 데이터를 넣어준다.

![image](https://user-images.githubusercontent.com/52814897/76603858-0e022780-6551-11ea-985a-ef13d2388fbc.png)

여기까지 Django 프로젝트는 준비가 끝났고, 다음은 Cache로 사용할 Redis를 설정해줘야 한다.

### Redis 활용하기

#### Redis

> 출처 - [위키백과](https://ko.wikipedia.org/wiki/레디스)

레디스(Redis)는 Remote Dictionary Server의 약자로써, 의미 그대로 "키-값" 구조의 데이터를 저장하고 관리하는 오픈 소스 기반의 비관계형 데이터베이스 관리 시스템(NoSQL)이다.

디스크가 아닌 메모리를 기반으로 한 데이터 저장소이기 때문에 동작 속도가 훨씬 빠르고, 상황에 따라 데이터베이스 또는 Cache로 사용할 수 있다.

#### Docker + Redis

여기서는 Docker와 친해지기 위해 Docker 위에 Redis를 올릴 예정이다.

먼저, redis image를 가져와 redis 컨테이너를 기본 포트인 6379번에 올린다.

```shell
docker pull redis
docker run -d -p 6379:6379 --name redis1 redis
```

그 후 `redis-cli` 사용을 위해 redis를 shell로 실행해준다.

```shell
docker exec -it redis1 sh
```

아래와 같이 포트로 접속된 후, `ping`이라는 명령어를 날렸을 때 `PONG`이라는 응답이 오면 정상적으로 접속된 것이다.

![image](https://user-images.githubusercontent.com/52814897/76602492-5ec45100-654e-11ea-9d54-25c2bff26851.png)

Django 프로젝트에서 설정했던 1번 데이터베이스로의 접근을 위해  `SELECT 1`을 입력한다.

![image](https://user-images.githubusercontent.com/52814897/76602720-e14d1080-654e-11ea-9276-dc2cab44fefa.png)

docker의 redis 서버가 켜진 상태에서 두 개의 장고 프로젝트 중에서 redis 서버와 연동된 프로젝트를 킨 후 글들의 리스트를 보여주는 페이지에 직접들어가거나 Postman을 사용하여 요청을 한 번 보내준다.

![image](https://user-images.githubusercontent.com/52814897/76604416-0d1dc580-6552-11ea-9817-17ea14210086.png)

요청을 보냄으로써 해당코드는 실행되었고, redis에도 해당 데이터가 저장되었을 것이다.

저장된 `Key-Value`가 있는지 확인하기 위해 `keys *` 명령어를 입력하면, ":1:posts"라는 Key가 생겼고,

![image](https://user-images.githubusercontent.com/52814897/76604523-32123880-6552-11ea-98c0-23dd601b379a.png)

`get :1:posts` 명령어로 내용도 잘 담기는 것을 확인할 수 있다.

![image](https://user-images.githubusercontent.com/52814897/76604633-7271b680-6552-11ea-9868-a449eaf67d81.png)

redis도 잘 동작하는 것을 확인하였으니 이제 본격적으로 두 개의 django 프로젝트를 비교하고 cache의 사용 유무를 비교해보자.

## JMeter 비교

Cache의 유무가 어떤 영향을 미치는지 확인하기 위해 JMeter를 이용하여 응답 속도를 비교하였다.

### Threads Schedule

- Start Threads Count : 100
- Startup Time : 20sec
- Hold Load For : 30sec

### 데이터 수 - 100개

먼저 데이터 수가 100개일 경우 진행하였다.

#### TPS

- Non-Cache TPS

![1_2](https://user-images.githubusercontent.com/52814897/76605883-96ce9280-6554-11ea-90b6-6e7bec8a7e45.JPG)

- Cache TPS

![2_2](https://user-images.githubusercontent.com/52814897/76605953-b4036100-6554-11ea-9c89-4a26659b1584.JPG)

초당 처리하는 트랜잭션(TPS)의 그래프를 보면 Non-Cache 경우는 초당  약 120개의 트랜잭션을 처리하지만, Cache를 사용했을 경우의 TPS는 변동폭이 크긴하지만 초당 약 200개 수준의 트랜잭션을 처리하였다.

#### Response Time

- Non-Cache Response-Time

![1_1](https://user-images.githubusercontent.com/52814897/76606152-1eb49c80-6555-11ea-91e5-d6201417989e.JPG)

- Cache Response-Time

![2_1](https://user-images.githubusercontent.com/52814897/76606157-1fe5c980-6555-11ea-832e-1d38710b3c66.JPG)

반응 시간(response time)을 살펴보면 Non-cache는 가장 긴 반응시간이 850ms, cache를 사용했을 경우는 520ms로 cache를 사용했을 경우가 300ms이상 빨랐다.

### 데이터 수 - 500개

좀 더 큰 차이를 보기 위해서 데이터를 100개에서 500개로 늘려 한번 더 진행하였다.

#### TPS

- Non-Cache TPS

![1_2](https://user-images.githubusercontent.com/52814897/76606598-e06bad00-6555-11ea-9c0b-00f1ad03f09c.JPG)

- Cache TPS

![2_2](https://user-images.githubusercontent.com/52814897/76606602-e1044380-6555-11ea-9669-f8139d8779f5.JPG)

데이터의 개수를 500개로 늘렸을 경우, 데이터의 양이 많아진 만큼 초당 트랜잭션을 처리하는 개수는 양쪽 모두 줄어들었다.

Non-Cache의 경우 데이터가 100개일 때 120 TPS에 비해 500개의 데이터에 대해서는 절반도 안되는 수준인 50 TPS로 약 60% 가량 감소하였다.

하지만 Cache를 사용했을 경우는 200 TPS에서 150 TPS정도로 약 25% 밖에 감소하지 않았다.

#### Response Time

- Non-Cache Response-Time

![1_1](https://user-images.githubusercontent.com/52814897/76607202-e746ef80-6556-11ea-9363-7db1ea1315a4.JPG)

- Cache Response-Time

![2_1](https://user-images.githubusercontent.com/52814897/76607204-e8781c80-6556-11ea-9a28-4896bf481bde.JPG)

반응 시간에서는 더욱 극적인 차이를 보였다.

Non-Cache의 경우 가장 느린 반응 시간이 약 2,000ms였고, Cache를 사용한 경우는 약 700ms로 약 3배라는 큰 차이가 발생하였다.

## 감상

개발환경이나 목적에 따라 다르겠지만, 이와 같이 단순히 같은 데이터를 읽는 과정에서는 확실히 캐시를 사용하는 편이 유리하다. 교육장에서 배우는 개인 또는 팀 프로젝트의 경우 시간에 쫓겨 일단 완성하는 것을 목표로 두었지, 실제로 내가 만든 코드가 최적화가 필요한지 아닌지 생각해 본 적도 없는 것 같다.

알고리즘 문제를 풀면서도 항상 '파이썬은 어차피 느리니까...'하고 안일하게 생각하고 있었는데, 내가 빠르게 만드려는 노력조차 하지 않았다는 것을 깨달았다. 아직 실전에서 일해본 경험은 없긴 하지만 이번 최적화 프로젝트를 계기로 프로젝트를 진행함에 있어 자원 관리와 효율을 고려한 코딩 스타일이 필요하다고 느꼈다.