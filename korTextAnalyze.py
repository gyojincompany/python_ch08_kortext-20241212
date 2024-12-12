import json
import re  # 정규표현식
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






