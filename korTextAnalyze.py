import json
import re  # 정규표현식
from audioop import reverse

import matplotlib.pyplot as plt  # 시각화
from collections import Counter  # 빈도수 분석
from konlpy.tag import Okt  # 형태소 분석 후 품사 태깅
from wordcloud import WordCloud  # 워드 클라우드

# 그래프 내에서 한글 깨짐 방지
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

data = json.loads(open("data/etnews.json","r",encoding="utf-8").read())  # json 파일을 불러오기
print(data)
print(len(data))

news_message = ""  # 빈 문자열

# sum = 0
# for i in range(1, 11):
#     sum = sum + i ->sum:55 1+2+3+...10

for item in data:
    news_message = news_message + re.sub(r"[^\w]"," ", item["message"])
    # \n 과 같이 줄바꿈 기호 등을 모두 공백 1칸으로 변경 한 후 한개의 큰 문자열로 누적

print(news_message)

nlp = Okt()  # 형태소 분석 후 품사 태깅 클래스
message_noun = nlp.nouns(news_message)  # news_message 문자열 내의 형태소 분석 후 명사 품사만 찾아내서 list 타입으로 반환
print(message_noun)

count = Counter(message_noun)  # 빈도수 계산 결과 반환
print(count)

word_count = dict()

for tag, counts in count.most_common(50):  # 상위 50개만 추출
    if(len(tag)>1):  # 단어의 길이가 2글자 이상인 단어들만 추출
        word_count[tag] = counts

print(word_count)

del word_count["산업혁명"]  # 검색어인 산업혁명 단어는 삭제

print(word_count)

sorted_keys = sorted(word_count, key=word_count.get, reverse=True)  # value의 내림차순으로 key를 정렬
print(sorted_keys)
sorted_values = sorted(word_count.values(), reverse=True)  # value의 내림차순 정렬
print(sorted_values)

# 돗수분포 그래프(bar graph)
plt.bar(range(len(word_count)), sorted_values, align="center")
plt.xticks(range(len(word_count)), list(sorted_keys), rotation=85)
plt.show()

wc = WordCloud(width=800, height=600, background_color="ivory", font_path="c:/Windows/Fonts/batang.ttc")
cloud = wc.generate_from_frequencies(word_count)
plt.imshow(cloud)
plt.axis("off")  # 축 제거
plt.show()

cloud.to_file("data/wordCloud.jpg")  # 이미지 파일로 저장