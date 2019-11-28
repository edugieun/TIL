# 1. Flex

- Flex container와 Flex item을 사용함.
- x 축 justify (단 column이 기준이 되는 순간 justify는 y축, align이 x축으로 바뀜)
- y축 align
- 한줄 - items
- 여러줄 - content
- 개별 요소 - self

## 1.1. Flex 명령어 + 속성

- flex-direction:
  - row;
  - row-reverse;
  - column;
  - column-reverse;
- align-content:
  - flex-start;
  - flex-end;
  - center;
  - space-between;
  - space-around;
  - stretch; 요소사이가 멀어지는게 아니라, 요소 길이 자체가 늘어남.
- justify-content:
  - flex-start;
  - flex-end;
  - center;
  - space-between;
  - space-around;
- align-items: / align-self:
  - flex-start;
  - flex-end;
  - center;
  - baseline;
  - stretch;
- flex-wrap:
  - nowrap;
  - wrap;
  - wrap-reverse;
- flex-flow:
  - flex-direction과 flex-wrap의 숏핸드임.
- order: