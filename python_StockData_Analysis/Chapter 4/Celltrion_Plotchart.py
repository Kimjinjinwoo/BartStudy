from bs4 import BeautifulSoup
import requests
import pandas as pd
from matplotlib import pyplot as plt

import warnings
warnings.filterwarnings('ignore')

url = 'https://finance.naver.com/item/sise_day.naver?code=068270&page=1'
html = requests.get(url, headers = {'User-agent': 'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml')
pgrr = bs.find( 'td' , class_='pgRR')

s = str(pgrr.a['href']).split('=')

last_page = s[-1]

df = pd.DataFrame()

#전체 페이지 다 읽어오기

sise_url = 'https://finance.naver.com/item/sise_day.naver?code=068270'

for page in range(1 , int(last_page)+1):
        url = '{}&page={}'.format(sise_url , page)
        html = requests.get(url , headers={'User-agent': 'Mozilla/5.0'}).text
        df = df.append(pd.read_html(html, header = 0)[0])

#차트 출력을 위해 데이터프레임 가공하기
df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by='날짜')

#날짜, 종가 컬럼으로 차트 그리기
plt.title('Celltrion (close)')
plt.xticks(rotation = 45)
plt.plot(df['날짜'] , df['종가'],'co-')
plt.grid(color = 'gray',linestyle='--')
plt.show()

