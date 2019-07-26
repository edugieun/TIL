import requests
import csv
from decouple import config
from datetime import timedelta, datetime
from pprint import pprint


# 단계별로 가보자.
## 1. 하루치 TOP10을 csv 로 만들자.
### 하루치 영화를 json으로 불러야겠다.
movie_res = requests.get(f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt=20190701&')

## 2. 하루치 영화의 test.csv 파일을 만들자
### key는 movie name만 뽑아보자
### test.csv 파일 생성
with open('test.csv', 'w', newline='', encoding='utf-8') as f:
    # 필드 이름 설정
    fieldnames = ('movieCd', 'movieNm', 'audiAcc')
    # 필드 기록
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # 필드를 csv 파일 최상단에 작성
    writer.writeheader()

# url에 있는 딕셔너리를 movies에 저장
movies = movie_res.json().get('boxOfficeResult').get('dailyBoxOfficeList')

# movieCd, movieNm, audiAcc 3개의 키만 있는 딕셔너리-리스트 만들기.
tmp_empty_list = []
for i in range(10):
    # 딕셔너리 키, 벨류 할당 방법
    ## 빈 딕셔너리 생성 후
    tmp_empty_dic = {}
    ## 아래의 형식으로 값을 넣어줌.
    tmp_empty_dic['movieCd'] = movies[i].get('movieCd')
    tmp_empty_dic['movieNm'] = movies[i].get('movieNm')
    tmp_empty_dic['audiAcc'] = movies[i].get('audiAcc')
    ## 만들어진 딕셔너리를 리스트의 원소로 할당
    tmp_empty_list.append(tmp_empty_dic)



    for movie in movies:
            writer.writerow(movie)






# url 데이터 뽑기
"""
def movie_url(**kwargs):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
    for key, value in kwargs.items():
        base_url = f'{key}={value}&'
    return base_url

api = {
    'key' : '',
    'targetDt' : '20190710'
}
"""



## 최신 누적 관객수만 뽑는 코드는 어디 들어가야 할까?

# 'boxoffice.csv' 파일 생성
"""
# csv 파일 생성
with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
    # 필드 이름 설정
    fieldnames = ('movieCd', 'movieNm', 'audiAcc')
    # 필드 기록
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # 필드를 csv 파일 최상단에 작성
    writer.writeheader()

    # 딕셔너리를 순회하며 key를 통해 한줄씩 value 작성
    for movie in movies:
        writer.writerow(movie)
"""