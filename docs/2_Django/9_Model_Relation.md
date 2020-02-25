# M:N

## Model relationships

1. Many-to-one
2. Many-to-Many

- 모델링은 현실 세계를 최대한 유사하게 반영하기 위해서 해야한다.
- 환자와 의사의 예약 시스템을 구축하라는 프로젝트
- 1:N의 한계가 있기 때문에
- 중개 모델이 필요하다.
- 중개 모델을 직접 거치지 않고 바로 가져올 수는 없을까?
  - `Through` option
  - MTOM 필드는 실제 물리적인 field가 db에 생기는 것이 아니다.
- Doctor 도 patients로 참조할 수 없을까?
  - `related_name`
    - 참조되는 대상이 참조하는 대상을 찾을 때(역참조), 어떻게 불러 올지에 대해 정의한다.
    - 필수적으로 사용하는 건 아니지만, 필수적인 상황이 발생할 수 있다.
  - `related_name`을 쓰면 중개모델은 필요 없는가? 아니다.
    - 예약한 시간 정보를 담는다거나 하는 경우(==추가적인 필드가 필요한 경우)에는 반드시 중개모델을 만들어서 진행을 해야되는 상황도 있다. 다만 그럴 필요가 없는 경우 위와 같이 해결할 수 있다.

------

## Like

- user는 여러 article에 좋아요를 누를 수 있고
- article은 여러 user로부터 좋아요를 받을 수 있다.
- 변수명 혼동하지 말 것.
- `article.user` => 게시글을 작성한 유저 - 1:N
- `article.like_users` => 게시글을 조아요한 유저 - M:N
- `user.like_articles` = > 유저가 좋아요를 누른 게시글(역참조, `related_name`) - M:N
- `user.article_set` => 유저가 작성한 게시글(역참조) - 1:N

-------

## Profile

1. 유저가 작성한 게시글 몰록
2. 유저가 작성한 댓글 몰록
3. 정렬은 모두 최근에 작성한 것 부터
4. 각 게시글의 부가정보까지(좋아요, 댓글 몇 개 달렸는지)

## with template tag

- 복잡한 변수를 더 간단한 이름으로 저장(캐시)하며, 여러번 DB를 조회할 때(특히 비용이 많이 드는) 유용하게 사용 가능하다.

------

## Hashtag

`get_or_create(defaults=None, **kwargs)`

- 주어진 kwargs로 객체를 찾으며 필요한 경우 하나를 만든다.
- `(object, created)` 형태의 튜플을 리턴한다.
- object는 검색 또는 생성된 객체이고, created는 새 객체 생성 여부를 지정하는 boolean 값이다. (새로 만들어진 object라면 True, 기존에 존재하던 object라면 False)
  - `get->False | create->True`
- 단, 이 메서드는 DB가 키워드 인자의 unique 옵션을 강제하고 있다고 가정하고 실행된다.
- 이는 요청이 병렬로 작성될 때 및 중복 코드에 대한 문제 방지로 중복 오브젝트가 작성되는 것을 예방한다.

`unique 옵션` 

- True인 경우 이 필드는 테이블 전체에서 고유한 값이어야 한다.
- 유효성 검사 단계에서 실행되며, 중복 값이 있는 모델을 저장하려고 하면, `.save()`메서드로 인해 `IntegrityError`가 발생한다.
- ManyToManyField 및 OneToOneField를 제외한 모든 필드 유형에서 유용한다.

`수정방법`

- 수정 할 때는 게시글의 모든 해쉬태그를 지우고 다시 찾으면서 등록해야 한다.