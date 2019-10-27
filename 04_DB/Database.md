# DataBase

- 데이터베이스: 체계화된 데이터의 모임
  - 자료들을 조직적으로 통합하여 중복을 없애고 구조화시킨 자료의 집합체

## DB 장점

- 데이터 중복 최소화
- 데이터 무결성
  - 결함이 없는 정확한 정보를 보장
- 테이터 일관성
- 데이터 독립성
  - 물리적 독립성과 논리적 독립성
- 데이터 표준화
- 데이터 보안 유지

## RDBMS

- 관계형 데이터베이스 관리 시스템(Relational Database Management System)
- 관계형 모델을 기반으로 하는 DB 관리 시스템
  - 예) MySQL, SQLite, ORACLE 등
- 관계형 데이터베이스(Relational DB)
  - 관계를 표현하기 위하여 2차원의 표 사용

## 기본 용어 정리

- 스키마(schema): 자료의 구조, 표현방법, 관계 등을 정의한 구조
- 테이블(table): 열(컬럼/필드)와 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합
- 열(Column), 컬럼: 각 열에는 고유한 데이터 형식이 지정
- 행(Row), 레코드: 테이블의 데이터를 저장
- PK(기본키): Primary Key, 각 행(레코드)의 고유값으로 반드시 설정.

## SQL 개념

- SQL(Structured Query Language)는 RDBMS의 데이터를 관리하기 위해 설게된 특수 목적의 `프로그래밍 언어`

### DDL-데이터 정의 언어

- 데이터를 정의하기 위한 언어. 테이블 및 스키마의 구조를 정의

- CREATE / DROP / ALTER

- ```sqlite
  # 테이블 생성
  CREATE TABLE classmates(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  --> PRIMARY KEY를 작성하지 않으면 자동은로 rowid 컬럼을 정의한다.
  --> PK는 INTEGER 만 사용가능
  --> AUTOINCREMENT는 이미 사용했던 pk번호는 뛰어넘고 다음 번호를 사용한다.
  name TEXT NOT NULL);
  --> 필요한 정보는 공백으로 비워두면 안되므로 NOT NULL 조건을 붙인다.
  
  # 테이블 삭제
  DROP TABLE classmates;
  
  # 테이블 명 변경
  ALTER TABLE classmates
  RENAME TO new_classmates;
  
  # 새로운 컬럼 추가
  ALTER TABLE classmates
  ADD COLUMN col_name datatype NOT NULL DEFAULT 1;
  ```

### DML-데이터 조작 언어

- 데이터를 저장, 수정, 삭제, 조회

- INSERT / UPDATE / DELETE / SELECT

- ```sqlite
  # 중복 없이 가져오기
  SELECT DISTINCT column FROM table;
  ```

- 

### DCL-데이터 제어 언어

- DB 사용자의 권한을 제어
- GRANT / REVOKE / COMMIT / ROLLBACK

### Datatype

- BOOLEAN은 없으며, 대신 정수 0, 1으로 저장
- INTEGET / TEXT / REAL / NUMERIC / BLOB