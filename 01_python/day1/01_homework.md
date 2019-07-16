1. Python에서 사용할 수 없는 식별자 예약어 를 찾아 작성하세요

```python
import keyword
print(keyword.kwlist)
```

2.
파이썬에서 float 는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다
(floating point rounding error)
따라서
아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요

```python
import math
a = 0.1 * 3
b = 0.3
math.isclose(a, b)
```

3.이스케이프 문자열 중 1) 줄바꿈 2) 탭 3) \을 작성하세요.

```
1) \n
2) \t
3) \\
```

4안녕 철수야 를 String Interpolation 을 사용하여 출력하세요

```

```

5.
다음 중 형변환시 오류가 발생하는 것은?
1)str (1) 

2) int (‘
3)int (5) 

4) bool(‘
5)int (‘

답:5번