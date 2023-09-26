#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install folium
#!pip install xgboost
#!pip install lightgbm
#!pip install tensorflow


# In[2]:


import pandas as pd
from glob import glob
from tqdm.notebook import tqdm
from sklearn import preprocessing
import requests
from bs4 import BeautifulSoup


# In[3]:


# 그래프를 출력할 때 한글 글씨체 사용
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


# # 지역별 가로등 개수

# ### 경기도 가로등 개수

# In[4]:


Gyeonggi_lamp = pd.read_csv('./경기_가로등현황.csv', encoding='euc-kr')
Gyeonggi_lamp2 = Gyeonggi_lamp
Gyeonggi_lamp2


# In[5]:


# 결측값 처리
Gyeonggi_lamp2 = Gyeonggi_lamp2.fillna(0)
Gyeonggi_lamp2


# In[6]:


# 기타 컬럼의 ","을 제거한 후 float형으로 바꿈
Gyeonggi_lamp2['기타'] = Gyeonggi_lamp2['기타'].str.replace(",","")
Gyeonggi_lamp2['기타'] = Gyeonggi_lamp2['기타'].astype(float)
Gyeonggi_lamp2


# In[7]:


# 가로등의 총 합계
Gyeonggi_lamp_sum = Gyeonggi_lamp2.sum()
Gyeonggi_total = 0
for i in Gyeonggi_lamp_sum[1:] :
    Gyeonggi_total += int(i)
Gyeonggi_total


# ### 서울 가로등 개수

# In[8]:


seoul_lamp = pd.read_csv('./서울_가로등현황.csv', skiprows=1)

seoul_lamp2 = seoul_lamp.copy()
seoul_lamp2 = seoul_lamp2.iloc[1:, -3:-2]
seoul_lamp2['가로등'] = seoul_lamp2['가로등'].astype(int)
# seoul_lamp2['가로등']의 row수가 가로등 개수
seoul_total = seoul_lamp2['가로등'].sum()
seoul_total


# ### 부산 가로등 개수

# In[9]:


busan_lamp = pd.read_csv('./부산_가로등현황.csv', encoding='euc-kr')

busan_lamp2 = busan_lamp.copy()
busan_lamp2


# In[10]:


# 데이터의 전체 합계 수가 가로등 개수
busan_lamp_sum = busan_lamp2.sum()
busan_total = 0
for i in busan_lamp_sum[1:] :
    busan_total += int(i)
busan_total


# ### 대구 가로등 개수

# In[11]:


daegu_lamp = pd.read_csv('./대구_가로등현황.csv',encoding='euc-kr')

daegu_lamp2 = daegu_lamp.copy()
# 전체 row수가 가로등 개수
daegu_total = daegu_lamp2.shape[0]
daegu_total


# ### 인천 가로등 개수

# In[12]:


incheon_lamp = pd.read_csv('./인천_가로등현황.csv',encoding='euc-kr')

incheon_lamp2 = incheon_lamp.copy()
# 가로등 컬럼만 불러온다
incheon_lamp2 = incheon_lamp.iloc[:, -1]
incheon_total = incheon_lamp2.sum()
incheon_total


# ### 광주 가로등 개수

# In[13]:


# 광주 가로등 폴더에 있는 모든 csv 파일을 불러옴
gwangju_files = glob('./광주 가로등/*.csv')

gwangju_lamp = pd.DataFrame()
# 오류가 났을 때 파일 확인을 위한 tqdm 사용
for file_name in tqdm(gwangju_files):
    try :
        temp = pd.read_csv(file_name, encoding='euc-kr')
    except:
        temp = pd.read_csv(file_name)
    gwangju_lamp = pd.concat([gwangju_lamp, temp]) # 모든 csv 데이터를 합침
# 합친 csv 파일의 row값 = 가로등 개수
gwangju_total = gwangju_lamp.shape[0]
gwangju_total


# ### 대전 가로등 개수

# In[14]:


daejeon_lamp = pd.read_csv('./대전_가로등현황.csv', encoding='euc-kr')

daejeon_lamp2 = daejeon_lamp.copy()
# row 값 = 가로등 개수
daejeon_total = daejeon_lamp2.shape[0]
daejeon_total


# ### 울산 가로등 개수

# In[15]:


ulsan_lamp = pd.read_csv('./울산_가로등현황.csv', encoding='euc-kr')

ulsan_lamp2 = ulsan_lamp.copy()
ulsan_lamp2


# In[16]:


ulsan_lamp3 = ulsan_lamp2['지형지물부호'] == '가로등'
ulsan_total = 0
# 지형지물부호가 가로등인 row만 count
for i in ulsan_lamp3 :
    if i == True :
        ulsan_total += 1
ulsan_total


# ### 세종 가로등 개수

# In[17]:


sejong_lamp = pd.read_csv('./세종_가로등현황.csv', encoding='euc-kr')

sejong_lamp2 = sejong_lamp.copy()
# row값 = 가로등 개수
sejong_total = sejong_lamp2.shape[0]
sejong_total


# ### 강원, 제주 가로등 개수

# In[18]:


# 자료 x, 기사를 통해 정보 얻음
gangwon_total = 98482
jeju_total = 34683


# ### 경북 가로등 개수

# In[19]:


# 경북 가로등 폴더에 있는 모든 csv 파일을 불러옴
Gyeongsangbuk_files = glob('./경북 가로등/*.csv')

Gyeongsangbuk_lamp = pd.DataFrame()
# 오류가 났을 때 파일 확인을 위한 tqdm 사용
for file_name in tqdm(Gyeongsangbuk_files):
    try :
        temp = pd.read_csv(file_name, encoding='euc-kr')
    except :
        temp = pd.read_csv(file_name)
    Gyeongsangbuk_lamp = pd.concat([Gyeongsangbuk_lamp, temp]) # 모든 csv 파일을 합침
# 합친 csv 파일의 row수 = 가로등 개수
Gyeongsangbuk_total = Gyeongsangbuk_lamp.shape[0]
Gyeongsangbuk_total


# ### 경남 가로등 개수

# In[20]:


# 경남 가로등 폴더에 있는 모든 csv 파일을 불러옴
Gyeongsangnam_files = glob('./경남 가로등/*.csv')

Gyeongsangnam_lamp = pd.DataFrame()
# 오류가 났을 때 파일 확인을 위한 tqdm 사용
for file_name in tqdm(Gyeongsangnam_files):
    try :
        temp = pd.read_csv(file_name, encoding='euc-kr')
    except:
        temp = pd.read_csv(file_name)
    Gyeongsangnam_lamp = pd.concat([Gyeongsangnam_lamp, temp]) # 모든 csv 파일을 합침
# 합친 csv 파일의 row수 = 가로등 개수
Gyeongsangnam_total = Gyeongsangnam_lamp.shape[0]
Gyeongsangnam_total


# ### 충남 가로등 개수

# In[21]:


# 충남 가로등 폴더에 있는 모든 csv 파일을 불러옴
Chungcheongnam_files = glob('./충남 가로등/*.csv')

Chungcheongnam_lamp = pd.DataFrame()
# 오류가 났을 때 파일 확인을 위한 tqdm 사용
for file_name in tqdm(Chungcheongnam_files):
    try :
        temp = pd.read_csv(file_name, encoding='euc-kr')
    except:
        temp = pd.read_csv(file_name)
    Chungcheongnam_lamp = pd.concat([Chungcheongnam_lamp, temp]) # 모든 csv 파일을 합침
# 합친 csv 파일의 row수 = 가로등 개수
Chungcheongnam_total = Chungcheongnam_lamp.shape[0]
Chungcheongnam_total


# ### 충북 가로등 개수

# In[22]:


# 에러
# 해결 정민님 감사합니다!!
# 충북 가로등 폴더에 있는 모든 csv 파일을 불러옴
Chungcheongbuk_files = glob('./충북 가로등/*.csv')

Chungcheongbuk_lamp = pd.DataFrame()
# 오류가 났을 때 파일 확인을 위한 tqdm 사용
for file_name in tqdm(Chungcheongbuk_files):
    try :
        temp = pd.read_csv(file_name, encoding='euc-kr')
    except :
        try :
            temp = pd.read_csv(file_name)
        except :
            temp = pd.read_csv(file_name, encoding='cp949') # euc-kr, utf-8 인코딩 모두 오류시 cp949 인코딩
    Chungcheongbuk_lamp = pd.concat([Chungcheongbuk_lamp, temp]) # 모든 csv 파일을 합침
# 합친 csv 파일의 row수 = 가로등 개수
Chungcheongbuk_total = Chungcheongbuk_lamp.shape[0]
Chungcheongbuk_total


# ### 전북 가로등 개수

# In[23]:


# 전북 가로등 폴더에 있는 모든 csv 파일을 불러옴
Jeollabuk_files = glob('./전북 가로등/*.csv')

Jeollabuk_lamp = pd.DataFrame()
# 오류가 났을 때 파일 확인을 위한 tqdm 사용
for file_name in tqdm(Jeollabuk_files):
    try :
        temp = pd.read_csv(file_name, encoding='euc-kr')
    except:
        temp = pd.read_csv(file_name)
    Jeollabuk_lamp = pd.concat([Jeollabuk_lamp, temp]) # 모든 csv 파일을 합침
# 합친 csv 파일의 row수 = 가로등 개수
Jeollabuk_total = Jeollabuk_lamp.shape[0]
Jeollabuk_total


# ### 전남 가로등 개수

# In[24]:


# 전남 가로등 폴더에 있는 모든 csv 파일을 불러옴
Jeollanam_files = glob('./전남 가로등/*.csv')

Jeollanam_lamp = pd.DataFrame()
# 오류가 났을 때 파일 확인을 위한 tqdm 사용
for file_name in tqdm(Jeollanam_files):
    try :
        temp = pd.read_csv(file_name, encoding='euc-kr')
    except:
        temp = pd.read_csv(file_name)
    Jeollanam_lamp = pd.concat([Jeollanam_lamp, temp]) # 모든 csv 파일을 합침
# 합친 csv 파일의 row수 = 가로등 개수
Jeollanam_total = Jeollanam_lamp.shape[0]
Jeollanam_total


# In[25]:


# 전국 가로등 개수를 리스트에 추가
total_lamp = [seoul_total, busan_total, daegu_total, incheon_total, gwangju_total, daejeon_total, ulsan_total, sejong_total, 
              Gyeonggi_total, gangwon_total, Chungcheongbuk_total, Chungcheongnam_total, Jeollabuk_total, Jeollanam_total, 
              Gyeongsangbuk_total, Gyeongsangnam_total, jeju_total]
total_lamp


# # 지역별 범죄 건수

# In[26]:


crime = pd.read_csv('./지역별 범죄 건수, 지역별 인구수.csv', encoding='euc_kr')

# 원본 훼손 방지를 위해 copy
crime2 = crime.copy()
crime2.columns = ['지역', '2017', '2018', '2019', '2020', '2021']
crime2 = crime2.set_index(["지역"])
crime2


# In[27]:


crime.info()


# In[28]:


# 결측치 확인
pd.isna(crime2)


# In[29]:


# 중앙값 열 추가
crime2.loc[:,'중앙값'] = crime2.median(axis=1)
crime2


# In[30]:


# 수의 차이
# 각 항목의 최소값을 0, 최대값을 1로 설정하고 범위 안에서 비교

col =  ['2017', '2018', '2019', '2020', '2021','중앙값']
x = crime2[col].values
scaler = preprocessing.MinMaxScaler()             # 정규화 시켜준다.
x_scale =scaler.fit_transform(x.astype(float))
crime_minmax = pd.DataFrame(x_scale, columns=col, index = crime2.index)
crime_minmax


# ## 월별 범죄 발생 건수

# In[31]:


monthCrime = pd.read_csv('./월별 범죄 발생 건수.csv', encoding='euc_kr')

# 원본 훼손 방지를 위해 copy
monthCrime2 = monthCrime.copy()

monthCrime2.columns = ['월', '2017', '2018', '2019', '2020', '2021']
monthCrime2


# In[32]:


# 칼럼값을 프레임 내에 넣기 위해 stack
monthCrime2 = pd.DataFrame(monthCrime2.stack()).reset_index()
monthCrime2


# In[33]:


monthCrime2 = monthCrime2.rename(columns={'level_0' : '월', 'level_1' : '연도', 0 : '총 범죄수'})
monthCrime2['월'] = monthCrime2['월']+1
monthCrime2


# In[34]:


# 잘못 들어간 행 삭제
for i in range(0, 71) :
    if monthCrime2.loc[i]['연도'] == '월' :
        monthCrime2 = monthCrime2.drop(i, axis = 0)
monthCrime2


# In[35]:


# 인덱스 재배열
monthCrime2 = monthCrime2.reset_index()
monthCrime2 = monthCrime2.iloc[:, 1:4]
monthCrime2


# ## 일별 범죄 발생 건수

# In[36]:


dayCrime = pd.read_csv('./요일별 범죄 발생 건수.csv', encoding='euc_kr')

# 원본 훼손 방지를 위해 copy
dayCrime2 = dayCrime.copy()
dayCrime2.columns = ['요일', '2017', '2018', '2019', '2020', '2021']
dayCrime2 = dayCrime2.set_index(["요일"])


# In[37]:


# 칼럼값을 프레임 내에 넣기 위해 stack
dayCrime2 = dayCrime2.stack().reset_index()
dayCrime2 = dayCrime2.rename(columns={'level_1' : '연도', 0 : '총 범죄수'})
dayCrime2


# In[38]:


dayCrime2.info()


# ## 시간별 범죄 발생 건수

# In[39]:


timeCrime = pd.read_csv('./시간별 범죄 발생 건수.csv', encoding='euc_kr')

# 원본 훼손 방지를 위해 copy
timeCrime2 = timeCrime.copy()
timeCrime2.columns = ['시간', '2017', '2018', '2019', '2020', '2021']
timeCrime2 = timeCrime2.set_index(["시간"])
timeCrime2

# timeCrime2 = timeCrime.copy()
# timeCrime2['year'] = timeCrime2['year'].astype(str)


# In[40]:


# 칼럼값을 프레임 내에 넣기 위해 stack
timeCrime2 = timeCrime2.stack().reset_index()
timeCrime2


# In[41]:


# 컬럼명 변경
timeCrime2 = timeCrime2.rename(columns={'level_1' : '연도', 0 : '총 범죄수'})
timeCrime2


# In[42]:


timeCrime2.info()


# ## 장소별 범죄 발생 건수

# In[43]:


placeCrime = pd.read_csv('./장소별 범죄 건수.csv', encoding='euc_kr')

# 원본 훼손 방지를 위해 copy
placeCrime2 = placeCrime.copy()
placeCrime2.columns = ['장소', '2017', '2018', '2019', '2020', '2021']
placeCrime3 = placeCrime2.copy()
placeCrime2 = placeCrime2.set_index(['장소'])

# 컬럼값(장소)을 데이터에 넣음
placeCrime2 = pd.DataFrame(placeCrime2.stack()).reset_index()

# 장소의 실외 여부 리스트
in_or_out = [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0,
             0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 
             1, 1, 0, 0, 0]

placeCrime3.insert(6, '실외 여부',in_or_out)
placeCrime3 = placeCrime3.drop(columns='장소')
placeCrime3 = placeCrime3.set_index(['실외 여부'])
# 컬럼값(실외 여부)을 데이터에 넣음
placeCrime3 = pd.DataFrame(placeCrime3.stack()).reset_index()
# 실외 여부 데이터만 추출
placeCrime3 = placeCrime3.iloc[:, :1]
placeCrime2.insert(3, '실외 여부', placeCrime3)
placeCrime2 = placeCrime2.rename(columns={'level_1' : '연도', 0 : '총 범죄수'})
placeCrime2['실외 여부'] = placeCrime2['실외 여부'].astype(str)

# 불필요한 '기타' 행 제거
placeCrime2 = placeCrime2.iloc[:-5]
placeCrime2


# In[44]:


# # 불필요한 '기타' 행 제거
# placeCrime2 = placeCrime2.drop(['기타'],axis=0)
# placeCrime2
placeCrime2 = placeCrime2.rename(columns={'level_1' : '연도', 0 : '총 범죄수'})
# 불필요한 '기타' 행 제거
placeCrime2 = placeCrime2.iloc[:-5]
placeCrime2


# In[45]:


# # 합계 열 추가
# placeCrime2.loc[:, '합계'] = placeCrime2.loc[:,'2017':'2021'].sum(axis=1)
# placeCrime2


# In[46]:


placeCrime2.info()


# ## 경찰서,파출소,지구대 현황

# In[47]:


police = pd.read_csv('./1720전국 경찰서 현황.csv', encoding='euc_kr')

# 원본 훼손 방지를 위해 copy
police2 = police.copy()
police2


# In[48]:


# 결측치 갯수 세기
police2.isnull().sum(axis=1) # 행으로 계산


# In[49]:


# '세종'의 결측치를 2019년도 정보로 대체
police2['17년도 지구대'] = police['17년도 지구대'].fillna(0)
police2['17년도 파출소'] = police['17년도 파출소'].fillna(0)
police2['18년도 지구대'] = police['18년도 지구대'].fillna(0)
police2['18년도 파출소'] = police['18년도 파출소'].fillna(0)

police2


# In[50]:


# 결측치 갯수 재확인
police2.isnull().sum(axis=1) # 행으로 계산


# In[51]:


# 년도별로 열 합치기
for i in range(17,22):
    i = str(i)
    police2.loc[:, i+'년도 경찰서,지구대,파출소'] = police2.loc[:,i+'년도 경찰서':i+'년도 파출소'].sum(axis=1)

# 불필요한 열 제거
for i in range(17,22):
    i = str(i)
    police2 = police2.drop([i+'년도 경찰서',i+'년도 지구대',i+'년도 파출소'],axis=1)

police2.columns = ['지역', '17년도 경찰서,지구대,파출소', '18년도 경찰서,지구대,파출소', '19년도 경찰서,지구대,파출소',
                  '20년도 경찰서,지구대,파출소','21년도 경찰서,지구대,파출소']
police2 = police2.set_index(["지역"])
police2


# In[52]:


police2.loc['경기'] = police2.loc['경기남부':'경기북부'].sum()

# 행 순서 변경
police2 = police2.reindex(index=['서울','부산','대구','인천','광주','대전','울산','세종','경기','강원',
                        '충북','충남','전북','전남','경북','경남','제주'])
police2


# In[53]:


# 수의 차이
# 각 항목의 최소값을 0, 최대값을 1로 설정하고 범위 안에서 비교

col =  ['17년도 경찰서,지구대,파출소', '18년도 경찰서,지구대,파출소', '19년도 경찰서,지구대,파출소',
        '20년도 경찰서,지구대,파출소','21년도 경찰서,지구대,파출소']
x = police2[col].values
scaler = preprocessing.MinMaxScaler()             # 정규화 시켜준다.
x_scale =scaler.fit_transform(x.astype(float))
police_minmax = pd.DataFrame(x_scale, columns=col, index = police2.index)
police_minmax


# In[54]:


# 지역별 범죄 발생 건수와 합치기 (일반 데이터)
crime_df = crime2.merge(police2[['17년도 경찰서,지구대,파출소', '18년도 경찰서,지구대,파출소', '19년도 경찰서,지구대,파출소',
                                 '20년도 경찰서,지구대,파출소','21년도 경찰서,지구대,파출소']], on='지역')
crime_df


# In[55]:


# 지역별 범죄 발생 건수와 합치기 (정규화 데이터)
crime_df_minmax = crime_minmax.merge(police_minmax[['17년도 경찰서,지구대,파출소', '18년도 경찰서,지구대,파출소', '19년도 경찰서,지구대,파출소',
                                 '20년도 경찰서,지구대,파출소','21년도 경찰서,지구대,파출소']], on='지역')
crime_df_minmax


# ## CCTV 설치 운영 현황

# In[56]:


cctv = pd.read_csv('./CCTV_설치_운영_현황_20230913163452.csv', encoding='euc_kr')

# 원본 훼손 방지를 위해 copy
cctv2 = cctv.copy()
cctv2


# In[57]:


# 불필요한 columns 제거
cctv2 = cctv2.drop(['구분(1)','전체 사업체 (개)','CCTV 미설치/미운영 사업체 수 (개)', 'CCTV 미설치/미운영 사업체 비율 (%)'], axis=1)
# 불필요한 rows 제거
cctv2 = cctv2.drop([0, 18, 19, 20, 21, 22], axis=0)
cctv2


# In[58]:


cctv2.columns = ['지역', 'CCTV 설치/운영 사업체 수 (개)', 'CCTV 설치/운영 사업체 비율 (%)', 'CCTV 설치/운영 대수 (대)']
cctv2 = cctv2.set_index(["지역"])
cctv2


# In[59]:


# 결측치 확인
pd.isna(cctv2)


# In[60]:


# 수의 차이
# 각 항목의 최소값을 0, 최대값을 1로 설정하고 범위 안에서 비교

col =  ['CCTV 설치/운영 사업체 수 (개)', 'CCTV 설치/운영 사업체 비율 (%)', 'CCTV 설치/운영 대수 (대)']
x = cctv2[col].values
scaler = preprocessing.MinMaxScaler()             # 정규화 시켜준다.
x_scale =scaler.fit_transform(x.astype(float))
cctv_minmax = pd.DataFrame(x_scale, columns=col, index = cctv2.index)
cctv_minmax


# In[61]:


# 지역별 범죄 발생 건수와 합치기 (일반 데이터)
# CCTV 운영대수 열만 가져와서 합치기

crime_df = crime_df.merge(cctv2[['CCTV 설치/운영 대수 (대)']], on='지역')
crime_df


# In[62]:


# 지역별 범죄 발생 건수와 합치기 (정규화 데이터)
# CCTV 운영대수 열만 가져와서 합치기

crime_df_minmax = crime_df_minmax.merge(cctv_minmax[['CCTV 설치/운영 대수 (대)']], on='지역')
crime_df_minmax


# ## 외국인 비율

# In[63]:


foreigner = pd.read_csv('./외국인__시군구_20230913163658.csv', encoding='euc_kr')

# 원본 훼손 방지를 위해 copy
foreigner2 = foreigner.copy()
foreigner2


# In[64]:


foreigner2 = foreigner2.drop([0, 1, 2, 3, 4], axis=0)
foreigner2 = foreigner2.drop('행정구역별(시군구)',axis=1)
foreigner2


# In[65]:


# 열 이름 변경
foreigner2 = foreigner2.rename(columns={'2017':'2017_외국인','2018':'2018_외국인','2019':'2019_외국인','2020':'2020_외국인','2021':'2021_외국인'})

# 열 추가
foreigner2['지역'] = ['서울','부산','대구','인천','광주','대전','울산','세종','경기','강원',
                        '충북','충남','전북','전남','경북','경남','제주']

# 열 순서 변경
foreigner2 = foreigner2.reindex(columns=['지역','2017_외국인','2018_외국인', '2019_외국인', '2020_외국인', '2021_외국인'])

# index 지정
foreigner2 = foreigner2.set_index(['지역'])
foreigner2


# In[66]:


foreigner2.info()


# In[67]:


# 결측치 확인
pd.isna(foreigner2)


# In[68]:


# 수의 차이
# 각 항목의 최소값을 0, 최대값을 1로 설정하고 범위 안에서 비교

col =  ['2017_외국인','2018_외국인', '2019_외국인', '2020_외국인', '2021_외국인']
x = foreigner2[col].values
scaler = preprocessing.MinMaxScaler()             # 정규화 시켜준다.
x_scale =scaler.fit_transform(x.astype(float))
foreigner_minmax = pd.DataFrame(x_scale, columns=col, index = foreigner2.index)
foreigner_minmax


# In[69]:


# 지역별 범죄 발생 건수와 합치기 (일반 데이터)
crime_df = crime_df.merge(foreigner2[['2017_외국인','2018_외국인', '2019_외국인', '2020_외국인', '2021_외국인']], on='지역')
crime_df


# In[70]:


# 지역별 범죄 발생 건수와 합치기 (정규화 데이터)
crime_df_minmax = crime_df_minmax.merge(foreigner_minmax[['2017_외국인','2018_외국인', '2019_외국인', '2020_외국인', '2021_외국인']], on='지역')
crime_df_minmax


# ## 평균 연령

# In[71]:


age = pd.read_csv('./201701_202112_주민등록인구기타현황(평균연령)_avgAge.csv', encoding='euc_kr')

# 원본 훼손 방지를 위해 copy
age2 = age.copy()
age2


# In[72]:


# 불필요한 열 삭제(성별 평균 연령)

for i in range(2017,2022):
    i = str(i)
    for j in range(1,10):
        j=str(j)
        age2 = age2.drop([i+'년0'+j+'월_남자 평균연령', i+'년0'+j+'월_여자 평균연령'],axis=1)

    for k in range(10,13):
        k=str(k)
        age2 = age2.drop([i+'년'+k+'월_남자 평균연령', i+'년'+k+'월_여자 평균연령'],axis=1)
age2


# In[73]:


# 결측치 갯수 세기
age.isnull().sum(axis=1) # 행으로 계산


# In[74]:


# 월별로 나누어져 있는 데이터를 연도별로 합치기
    
for i in range(2017,2022):
    i = str(i)
    age2.loc[:, i+'년_평균연령'] = round(age2.loc[:,(i+'년01월_평균연령'):(i+'년12월_평균연령')].sum(axis=1)/12,2)
age2


# In[75]:


# 불필요한 열 삭제
for i in range(2017,2022):
    i = str(i)
    m = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for j in m:
        age2 = age2.drop([i+'년'+j+'월_평균연령'],axis=1)

# 불필요한 행 삭제
age2 = age2.drop(0, axis=0)

age2


# In[76]:


age2.columns = ['지역', '2017년_평균연령', '2018년_평균연령', '2019년_평균연령', '2020년_평균연령', '2021년_평균연령']
age2 = age2.set_index(["지역"])
age2


# In[77]:


# 행 이름 변경
age2 = age2.rename(index={'서울특별시  (1100000000)':'서울','부산광역시  (2600000000)':'부산','대구광역시  (2700000000)':'대구',
                          '인천광역시  (2800000000)':'인천','광주광역시  (2900000000)':'광주','대전광역시  (3000000000)':'대전',
                         '울산광역시  (3100000000)':'울산','세종특별자치시  (3600000000)':'세종','경기도  (4100000000)':'경기',
                         '강원도  (4200000000)':'강원','충청북도  (4300000000)':'충북','충청남도  (4400000000)':'충남',
                         '전라북도  (4500000000)':'전북', '전라남도  (4600000000)':'전남','경상북도  (4700000000)':'경북',
                         '경상남도  (4800000000)':'경남','제주특별자치도  (5000000000)':'제주'})
age2


# In[78]:


# 수의 차이
# 각 항목의 최소값을 0, 최대값을 1로 설정하고 범위 안에서 비교

col =  ['2017년_평균연령', '2018년_평균연령', '2019년_평균연령', '2020년_평균연령', '2021년_평균연령']
x = age2[col].values
scaler = preprocessing.MinMaxScaler()             # 정규화 시켜준다.
x_scale =scaler.fit_transform(x.astype(float))
age_minmax = pd.DataFrame(x_scale, columns=col, index = age2.index)
age_minmax


# In[79]:


# 지역별 범죄 발생 건수와 합치기 (일반 데이터)
crime_df = crime_df.merge(age2[['2017년_평균연령', '2018년_평균연령', '2019년_평균연령', '2020년_평균연령', '2021년_평균연령']], on='지역')
crime_df


# In[80]:


# 지역별 범죄 발생 건수와 합치기 (정규화 데이터)
crime_df_minmax = crime_df_minmax.merge(age_minmax[['2017년_평균연령', '2018년_평균연령', '2019년_평균연령', '2020년_평균연령', '2021년_평균연령']], on='지역')
crime_df_minmax


# ## 인구수

# In[81]:


num = pd.read_csv('./201712_202112_주민등록인구및세대현황_연간.csv', encoding='euc_kr')

# 원본 훼손 방지를 위해 copy
num2 = num.copy()
num2


# In[82]:


# 불필요한 열 제거

num2 = num2.drop(['2017년_세대수','2017년_세대당 인구', '2017년_남자 인구수', '2017년_여자 인구수','2017년_남여 비율', 
                  '2018년_세대수','2018년_세대당 인구', '2018년_남자 인구수', '2018년_여자 인구수','2018년_남여 비율', 
                  '2019년_세대수','2019년_세대당 인구', '2019년_남자 인구수', '2019년_여자 인구수','2019년_남여 비율', 
                  '2020년_세대수','2020년_세대당 인구', '2020년_남자 인구수', '2020년_여자 인구수','2020년_남여 비율', 
                  '2021년_세대수','2021년_세대당 인구', '2021년_남자 인구수', '2021년_여자 인구수','2021년_남여 비율'],axis=1)

# 불필요한 행 제거
num2 = num2.drop([0])
num2


# In[83]:


# 열 이름 변경
# num2 = num2.rename(columns={'행정구역':'지역','2023년08월_총인구수':'총인구수'})
num2['2017년_총인구수'] = num2['2017년_총인구수'].str.replace(",","").astype(int)
num2['2018년_총인구수'] = num2['2018년_총인구수'].str.replace(",","").astype(int)
num2['2019년_총인구수'] = num2['2019년_총인구수'].str.replace(",","").astype(int)
num2['2020년_총인구수'] = num2['2020년_총인구수'].str.replace(",","").astype(int)
num2['2021년_총인구수'] = num2['2021년_총인구수'].str.replace(",","").astype(int)
num2['총인구수'] = num2.loc[:, '2017년_총인구수' : '2021년_총인구수'].mean(axis=1)

# 불필요한 행 제거
num2 = num2.drop(columns=['2017년_총인구수', '2018년_총인구수', '2019년_총인구수', '2020년_총인구수', '2021년_총인구수'])
num2

# index 지정
num2.columns = ['지역', '총인구수']
num2 = num2.set_index(["지역"])
num2


# In[84]:


# 행 이름 변경
num2 = num2.rename(index={'서울특별시  (1100000000)':'서울','부산광역시  (2600000000)':'부산','대구광역시  (2700000000)':'대구',
                          '인천광역시  (2800000000)':'인천','광주광역시  (2900000000)':'광주','대전광역시  (3000000000)':'대전',
                         '울산광역시  (3100000000)':'울산','세종특별자치시  (3600000000)':'세종','경기도  (4100000000)':'경기',
                         '강원도  (4200000000)':'강원','충청북도  (4300000000)':'충북','충청남도  (4400000000)':'충남',
                         '전라북도  (4500000000)':'전북', '전라남도  (4600000000)':'전남','경상북도  (4700000000)':'경북',
                         '경상남도  (4800000000)':'경남','제주특별자치도  (5000000000)':'제주'})
num2


# In[85]:


# 지역별 범죄 발생 건수와 합치기 (일반 데이터)
crime_df = crime_df.merge(num2[['총인구수']], on='지역')
crime_df


# In[86]:


# 지역별 범죄 발생 건수와 합치기 (정규화 데이터)
crime_df_minmax = crime_df_minmax.merge(num2[['총인구수']], on='지역')
crime_df_minmax


# In[87]:


# 열 순서 변경 (일반 데이터)
crime_df = crime_df.reindex(columns=['총인구수','중앙값','2017','2018','2019','2020','2021','17년도 경찰서,지구대,파출소','18년도 경찰서,지구대,파출소','19년도 경찰서,지구대,파출소','20년도 경찰서,지구대,파출소','21년도 경찰서,지구대,파출소','CCTV 설치/운영 대수 (대)','2017_외국인','2018_외국인', '2019_외국인', '2020_외국인', '2021_외국인','2017년_평균연령', '2018년_평균연령', '2019년_평균연령', '2020년_평균연령', '2021년_평균연령'])
crime_df


# In[88]:


# 결측치 갯수 확인
crime_df.isnull().sum(axis=1) # 행으로 계산


# In[89]:


# 열 순서 변경 (정규화 데이터)
crime_df_minmax = crime_df_minmax.reindex(columns=['총인구수','2017','2018','2019','2020','2021','17년도 경찰서,지구대,파출소','18년도 경찰서,지구대,파출소','19년도 경찰서,지구대,파출소','20년도 경찰서,지구대,파출소','21년도 경찰서,지구대,파출소','CCTV 설치/운영 대수 (대)','2017_외국인','2018_외국인', '2019_외국인', '2020_외국인', '2021_외국인','2017년_평균연령', '2018년_평균연령', '2019년_평균연령', '2020년_평균연령', '2021년_평균연령'])
crime_df_minmax


# In[90]:


# 결측치 갯수 확인
crime_df_minmax.isnull().sum(axis=1) # 행으로 계산


# In[91]:


# 지도 시각화를 위한 도시의 영어이름 칼럼 추가
name_eng = ['Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', 'Daejeon', 'Ulsan', 
            'Sejongsi', 'Gyeonggi-do', 'Gangwon-do', 'Chungcheongbuk-do', 'Chungcheongnam-do', 
            'Jeollabuk-do', 'Jeollanam-do', 'Gyeongsangbuk-do', 'Gyeongsangnam-do', 'Jeju-do']
crime_df.insert(0, '지역(영어)', name_eng)
crime_df


# ## 공원 개수

# In[92]:


park_df = pd.read_csv('./전국도시공원정보표준데이터.csv', encoding='euc-kr')

park_df2 = park_df.copy()
park_total = park_df2['제공기관명']
# 결측값 확인
park_total.isna().sum()

# 문자열로 형변환
park_loc = list(park_total)

# 앞에 3글자만 가져옴
for i in range(len(park_loc) - 1)  :
    park_loc[i] = str(park_loc[i])[:3]
len(park_loc)


# In[93]:


# 전체 변수 초기화
gyeonggi_park = 0
gangwon_park = 0
seoul_park = 0
busan_park = 0
daegu_park = 0
incheon_park = 0
dajeon_park = 0
ulsan_park = 0
sejong_park = 0
Chungcheongbuk_park = 0
Chungcheongnam_park = 0
Jeollabuk_park = 0
Jeollanam_park = 0
Gyeongsangbuk_park = 0
Gyeongsangnam_park = 0
jeju_park = 0
gwangju_park = 0
# count 되지 않는 값 확인
error_park = []

# 공원 변수에 count
for i in range(len(park_loc) - 1) :
    if park_loc[i] == '경기도' :
        gyeonggi_park += 1
    elif park_loc[i] == '강원도' or park_loc[i] == '강원특' :
        gangwon_park += 1
    elif park_loc[i] == '서울특' :
        seoul_park += 1
    elif park_loc[i] == '부산광' or park_loc[i] == '기장군' or park_loc[i] == '부산관' :
        busan_park += 1
    elif park_loc[i] == '대구광' :
        daegu_park += 1
    elif park_loc[i] == '인천광' or park_loc[i] == '인천시' :
        incheon_park += 1
    elif park_loc[i] == '대전광' :
        dajeon_park += 1
    elif park_loc[i] == '울산광' or park_loc[i] == '울산시' :
        ulsan_park += 1
    elif park_loc[i] == '세종특' :
        sejong_park += 1
    elif park_loc[i] == '충청북' :
        Chungcheongbuk_park += 1
    elif park_loc[i] == '충청남' :
        Chungcheongnam_park += 1
    elif park_loc[i] == '전라북' :
        Jeollabuk_park += 1
    elif park_loc[i] == '전라남' :
        Jeollanam_park += 1
    elif park_loc[i] == '경상북' :
        Gyeongsangbuk_park += 1
    elif park_loc[i] == '경상남' :
        Gyeongsangnam_park += 1
    elif park_loc[i] == '제주특' :
        jeju_park += 1
    elif park_loc[i] == '광주광' :
        gwangju_park += 1
    else :
        error_park.append(park_loc[i])
error_park


# In[94]:


# 가져온 지역 별 공원 수를 리스트에 저장
total_park = [seoul_park, busan_park, daegu_park, incheon_park, gwangju_park, dajeon_park, ulsan_park, 
              sejong_park, gyeonggi_park, gangwon_park, Chungcheongbuk_park, Chungcheongnam_park,
              Jeollabuk_park, Jeollanam_park, Gyeongsangbuk_park, Gyeongsangnam_park, jeju_park]
total_park


# In[95]:


crime_df.insert(24, '공원 수', total_park)


# In[96]:


crime_df


# In[97]:


crime_df.insert(24, '가로등 수', total_lamp)


# In[98]:


crime_df


# ### 전국 편의점 개수

# In[99]:


# 시간상 전체 주석 처리(코드 시연할때만 사용)
# 5분 가량 소요
# xml url을 불러와서 주소값만 추출
address = []
serviceKey = 'DEXLBUE5-DEXL-DEXL-DEXL-DEXLBUE508'
for page_no in tqdm(range(1, 892)) :
    url = f'https://www.safemap.go.kr/openApiService/data/getConvenienceStoreData.do?serviceKey={serviceKey}&pageNo={page_no}&numOfRows=50&dataType=XML&Fclty_Cd=509010'
    request = requests.get(url).text
    source = BeautifulSoup(request, features="xml")
    txt = source.find_all('ADRES')
    for i in txt :
        address.append(i.get_text)
len(address)


# In[100]:


# # 만약의 상황을 대비해 xlsx 파일로 저장
# pd.DataFrame(address).to_excel('전국 편의점 주소.xlsx')


# In[101]:


# address = pd.read_excel('./전국 편의점 주소.xlsx')

# address = list(address[0])


# In[102]:


# 주소 데이터 중 앞 3글자만 가져옴
for i in range(len(address)) :
    address[i] = str(address[i])[45:48]
address


# In[103]:


# 전체 변수 초기화
gyeonggi_store = 0
gangwon_store = 0
seoul_store = 0
busan_store = 0
daegu_store = 0
incheon_store = 0
dajeon_store = 0
ulsan_store = 0
sejong_store = 0
Chungcheongbuk_store = 0
Chungcheongnam_store = 0
Jeollabuk_store = 0
Jeollanam_store = 0
Gyeongsangbuk_store = 0
Gyeongsangnam_store = 0
jeju_store = 0
gwangju_store = 0
# count 되지 않는 값 확인
error_store = []

for i in address :
    if i == '경기도' :
        gyeonggi_store += 1
    elif i == '강원도' :
        gangwon_store += 1
    elif i == '서울특' :
        seoul_store += 1
    elif i == '부산광' :
        busan_store += 1
    elif i == '대구광' :
        daegu_store += 1
    elif i == '인천광' :
        incheon_store += 1
    elif i == '대전광' :
        dajeon_store += 1
    elif i == '울산광' :
        ulsan_store += 1
    elif i == '세종특' :
        sejong_store += 1
    elif i == '충청북' :
        Chungcheongbuk_store += 1
    elif i == '충청남' :
        Chungcheongnam_store += 1
    elif i == '전라북' :
        Jeollabuk_store += 1
    elif i == '전라남' :
        Jeollanam_store += 1
    elif i == '경상북' :
        Gyeongsangbuk_store += 1
    elif i == '경상남' :
        Gyeongsangnam_store += 1
    elif i == '제주특' :
        jeju_store += 1
    elif i == '광주광' :
        gwangju_store += 1
    else :
        error_store.append(i)
error_store


# In[104]:


total_store = [seoul_store, busan_store, daegu_store, incheon_store, gwangju_store, dajeon_store, ulsan_store, 
              sejong_store, gyeonggi_store, gangwon_store, Chungcheongbuk_store, Chungcheongnam_store,
              Jeollabuk_store, Jeollanam_store, Gyeongsangbuk_store, Gyeongsangnam_store, jeju_store]
total_store


# In[105]:


crime_df.insert(25, '편의점 수', total_store)


# In[106]:


crime_df


# ## 전국 코인노래방 개수

# In[107]:


karaoke_df = pd.read_excel('./코인,동전노래방_시도별.xlsx')

# 원본 손상 방지를 위해 copy
karaoke_df2 = karaoke_df.copy()
karaoke_df2


# In[108]:


karaoke_df2 = karaoke_df2.set_index(['지역'])
# 행 순서 변경
karaoke_df2 = karaoke_df2.reindex(['서울', '부산', '대구', '인천', '광주', '대전', 
                                   '울산', '세종', '경기', '강원', '충북', '충남', '전북', 
                                   '전남', '경북', '경남', '제주'])
karaoke_df2


# In[109]:


crime_df.insert(26, '코인노래방 수', karaoke_df2['개수'])
crime_df


# In[110]:


crime_df['2017_외국인']=crime_df['2017_외국인'].astype('float64')
crime_df['2018_외국인']=crime_df['2017_외국인'].astype('float64')
crime_df['2019_외국인']=crime_df['2017_외국인'].astype('float64')
crime_df['2020_외국인']=crime_df['2017_외국인'].astype('float64')
crime_df['2021_외국인']=crime_df['2017_외국인'].astype('float64')

crime_df.info()


# In[111]:


# 상관분석을 위해 데이터프레임 복사
crime_df1 = crime_df.copy()
# 2017~2021 까지의 총 범죄수 및 여러 요인의 평균 값 계산
crime_df1['총 범죄 수'] = crime_df1.loc[:,'2017':'2021'].sum(axis=1)
crime_df1['평균 치안센터 수'] = crime_df1.loc[:,'17년도 경찰서,지구대,파출소':'21년도 경찰서,지구대,파출소'].mean(axis=1)
crime_df1['평균 외국인 수'] = crime_df1.loc[:,'2017_외국인':'2021_외국인'].mean(axis=1)
crime_df1['평균연령'] = crime_df1.loc[:,'2017년_평균연령':'2021년_평균연령'].mean(axis=1)
crime_df1.info()


# In[112]:


# 인구 수 비례 여러 요인들의 상대적 크기 비교
crime_df1.insert(0, '인구 100명당 cctv 설치/운영 대수(대)',(crime_df1['CCTV 설치/운영 대수 (대)'] / crime_df1['총인구수'] * 100))
crime_df1.insert(0, '인구 100명당 총 범죄 수',(crime_df1['총 범죄 수'] / crime_df1['총인구수'] * 100))
crime_df1.insert(0, '인구 100명당 평균 치안센터 수',(crime_df1['평균 치안센터 수'] / crime_df1['총인구수'] * 100))
crime_df1.insert(0, '인구 100명당 평균 외국인 수',(crime_df1['평균 외국인 수'] / crime_df1['총인구수'] * 100))
crime_df1.insert(0, '인구 100명당 가로등 수',(crime_df1['가로등 수'] / crime_df1['총인구수'] * 100))
crime_df1.insert(0, '인구 100명당 공원 수',(crime_df1['공원 수'] / crime_df1['총인구수'] * 100))
crime_df1.insert(0, '인구 100명당 편의점 수',(crime_df1['편의점 수'] / crime_df1['총인구수'] * 100))
crime_df1.insert(0, '인구 100명당 코인노래방 수',(crime_df1['코인노래방 수'] / crime_df1['총인구수'] * 100))
crime_df1 = crime_df1.drop('총인구수', axis=1)
crime_df1


# In[113]:


crime_df1 = crime_df1.drop(columns= crime_df1.iloc[:, 9:-1])
crime_df1


# In[114]:


crime_df1 = crime_df1.drop(columns={'지역(영어)'})
crime_df1


# In[115]:


# 칼럼 순서 변경
crime_df1 = crime_df1[['인구 100명당 총 범죄 수', '인구 100명당 cctv 설치/운영 대수(대)', '인구 100명당 공원 수',
                       '인구 100명당 가로등 수', '인구 100명당 평균 외국인 수', '인구 100명당 평균 치안센터 수',
                       '인구 100명당 편의점 수', '인구 100명당 코인노래방 수', '평균연령']]
crime_df1

