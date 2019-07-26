# .update() 사용법 : 딕셔너리에 키:값 을 추가하거나 키의 값을 변경한다.
a = {}

# 1
a.update(key='value')

# 2
a.update({key: value})
# a.update({row[영화대표코드]: row['영화명(국문)']})


# . env 환경변수 세팅 및 키 가리기. (python-decouple로 설치. 아마 되어있을 거임.)


# .env 파일을 연결해줄 .py에 필요한 모듈
from decouple import config
CLIENT_ID = config(NAVER_CLIENT_ID)
CLIENT_SECRET = config(NAVER_CLIENT_SECRET)

# 1-1 네이버 요청 하는 법 (헤더작업. 대대분 사이트에서 필요한 작업)
import requests
HEADERS = {'X-Naver-Client-Id': CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET}

# 1-2 요청 보내기
url = 'https://openapi.naver.com/v1/search/movie.json'
address = f'{url}?query={movieNm}'
response = requests.get(address, headers=HEADERS).json() # 네이버의 경우 헤더도 같이 보내야한다.


# 2.이미지 파일 저장하기
# 2-1 movie_naver.csv 여기서 영화코드랑 썸네일 url 불러오고
# 2-2 요청보내서 응답을 작성하기
url = 'https://ssl.pstatic.net/imgmovie/mdi/mit110/0315/C1540-01.jpg'

for
    with open(f'images/{영화코드}.jpg', 'wb') as f:
        response = requests.get(url).content
        f.write(image)


# 