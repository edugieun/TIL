# sample.py

avengers = [
    {
        "name": "tony stark",
        "gender": "male",
        "appearances": 3068,
        "years since joining": 52
    },
    {
        "name": "robert bruce banner",
        "gender": "male",
        "appearances": 2089,
        "years since joining": 52
    },
    {
        "name": "thor odinson",
        "gender": "male",
        "appearances": 2402,
        "years since joining": 52
    },
    {
        "name": "steven rogers",
        "gender": "male",
        "appearances": 3458,
        "years since joining": 51
    }
]


# 1. csv.DictWriter()
import csv
import pprint
with open('avengers.csv', 'w', newline='', encoding='utf-8') as f: # with 구문
    # 저장할 데이터들의 필드 이름을 미리 정한다.
    fieldnames = ('name','gender')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # 필드 이름을 csv 파일 최상단에 작성한다.
    writer.writeheader()
    a = {}
    # 딕셔너리를 순회하며 key를 통해 한줄씩 (value)를 작성한다.
    for i in avengers[0].keys():
        if i in fieldnames:

        
        # writer.writerow(avenger)


# 2. csv.DictReader()
#import는 이미 위에서 해줬고
"""
with open('avengers.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    # 한줄씩 읽는다.
    for row in reader:
        print(row['name'])
        print(row['gender'])
        print(row['appearances'])
        print(row['years since joining'])
"""