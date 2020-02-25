# Relationship Fields

- ForeignKey(참조 키, 외래 키)
  - 개념
    - 외래 키는 참조하는 테이블에서 1개의 키(속성 또는 속성의 집합), 참조하는 측의 변수는 참조되는 측의 테이블의 키를 가리킨다.
    - 하나(또는 복수)의 다른 테이블의 기본 키 필드를 가리키는 데이터의 참조 무결성을 확인하기 위해서 사용된다.
  - 특징
    - 외래 키의 값으로는 부모 테이블에 존재하는 키의 값만 넣을 수 있다.
    - 외래 키를 사용하여 부모테이블의 유일한 값을 참조한다.(부모 테이블의 기본 키, 참조 무결성)
- `on_delete`
  - ForeignKey의 필수 인자이며, 참조하고 있는 부모 객체가 사라졌을 때 어떻게 처리할 것인지를 정의.
    1. `CASCADE`: 부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제한다.
    2. `PROTECT`: 참조가 되어 있는 경우 오류가 발생.(삭제 불가)
    3. `SET_NULL`: 부모 객체가 삭제 됐을 때 참조하는 모든 값을 NULL 로 치환.(단, DB 상에 NOT NULL 조건이 있다면 불가능)
    4. `SET_DEFAULT`: 모든 값이 DEFAULT로 설정한 값으로 치환(DB 상에 DEFAULT 조건 값이 있어야 함.)
    5. `SET`: 특정 함수를 호출(직접 만든 함수나 내장 함수)
    6. `DO_NOTHING`: 아무것도 하지 않는다. (단, DB 상에, 필드에 대한 `ON DELETE`제한 조건을 따로 설정해야 한다.)

- Metadata

  - META: 데이터에 대한 데이터

  - `class Meta`와 같이 선언하여 모델에 대한 모델-레벨의 메타 데이터를 선언할 수 있다.

  - 유용한 기능들 중 하나는 쿼리할 때 반환되는 기본 레코드 순서를 제어하는 것이다.(`ordering`)

    ```python
    # 예시
    class Meta:
        # 알파벳순(A-Z) 순으로 content를 정렬한 후,
        # 작성일(created_at) 별로 가장 나중에 작성된 것 부터 정렬
        ordering = ['content', '-created_at']
    ```

## ForeignKey - 1:N

- N 쪽에서 1을 참조하는 건 어렵지 않음.

  - 댓글의 입장에서 `comment.article`이 가능한 이유는 어떠한 댓글이든 반드시 자신이 참조하는 article이 있으므로 이와 같이 접근할 수 있다.

  ```python
  comment.article
  comment.article_id
  ...
  ```

- 역참조(1쪽에서 N을 참조하는 경우)

  - `article.comment` 형태로는 가져올 수없다. 게시글에 몇 개의 댓글이 있는지는 django ORM이 보장할 수 없기 때문. (본질적으로 Article 모델에 Comment와의 관계에 대해 작성된 것이 존재하지 않는다.)
  - `article.comment_set`로 접근할 수 있다.
  
- Comment 관련 추가 사항

  - 댓글 개수 출력

    ```html
    <!-- 댓글 개수 출력 -->
    1. <p><b>{{ comments|length }}개의 댓글</b></p>
    2. <p><b>{{ article.comment_set.all|length }}개의 댓글</b></p>
    3. <p><b>{{ comments.count }}개의 댓글</b></p>
    ```

    - 3번은 count 메서드가 호출되면서 comment로 모델 쿼리를 한번 더 db에 보내기 때문에 매우 작은 차이지만 더 느리다.

  - 댓글이 없는 경우 대체 문장 출력
  
    ```html
    {% empty %}
    <p><b> 댓글이 없어요... </b></p>
    {% endfor %}
    ```