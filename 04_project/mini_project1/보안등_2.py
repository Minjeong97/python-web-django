#!/usr/bin/env python
# coding: utf-8

# ## 보안등

# In[1]:


# 라이브러리 호출
import pandas as pd
import numpy as np


# ## 개별 데이터 전처리 (서울 ~ 충청북도)

# ### 서울

# In[2]:


# 파일 리스트 확인 (주의: 파일명 반복문으로 돌릴 수 있게 규칙성 있는 파일명으로 통일)
import os
os.listdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/서울')


# In[3]:


# 파일 여러개 한 번에 불러오기
## 1. 파일 리스트 저장
seouls = os.listdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/서울')

## 2. 현재 작업 위치로 이동
os.chdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/서울')

## 3. 데이터 프레임 생성하고 모든 파일 합치기
# 새로운 데이터프레임 생성
df_all_seoul = pd.DataFrame()

for seoul in seouls:
    df = pd.read_csv(seoul, encoding='cp949')
    df_all_seoul = pd.concat([df_all_seoul, df])

df_all_seoul = df_all_seoul.reset_index(drop=True)
df_all_seoul


# In[4]:


# 필요한 칼럼만 남기기
df_seoul = df_all_seoul[['설치개수','소재지도로명주소', '소재지지번주소', '위도', '경도', '데이터기준일자']]
df_seoul


# In[5]:


# 결측값 확인
df_seoul.isnull().sum()


# In[6]:


# 도로명주소 + 지번주소 합치기 -> '주소'
df_seoul['주소'] = np.where(pd.notnull(df_seoul['소재지도로명주소']) == True, df_seoul['소재지도로명주소'], df_seoul['소재지지번주소'])
df_seoul['주소'].isna().sum()


# In[7]:


# 도로명주소 + 지번주소 drop
## 도로명주소 + 지번주소 제외한 나머지 
df_seoul_2 = df_seoul[df_seoul.columns.difference(['소재지도로명주소', '소재지지번주소'])]
# 칼럼 순서 바꾸기
df_seoul_2 = df_seoul_2[['주소', '위도', '경도', '설치개수', '데이터기준일자']]
# 칼럼명 변경
df_seoul_2 = df_seoul_2.rename(columns={"주소": "address", 
                                        "위도": "lat", 
                                        "경도": "long",
                                       "설치개수": "install_cnt",
                                       "데이터기준일자": "date"})
df_seoul_2


# In[8]:


# 주소 분리 -> 시/도
## 공백 기준으로 분리
df_seoul_2['state'] = df_seoul_2['address'].str.split().str[0]
df_seoul_2['city'] = df_seoul_2['address'].str.split().str[1]
# 칼럼 순서 바꾸기
df_seoul_2 = df_seoul_2[['address', 'state', 'city', 'lat', 'long', 'install_cnt', 'date']]
df_seoul_2


# In[9]:


df_seoul_2.state.unique()


# In[10]:


df_seoul_2.loc[~df_seoul_2.state.str.contains('서울특별시'), 'state'].unique()


# In[11]:


df_seoul_unique = df_seoul_2.loc[~df_seoul_2.state.str.contains('서울특별시'), 'state'].unique()
for i in df_seoul_unique:
    print(i)


# In[12]:


# 주소에 '서울'이 포함된 주소만 남기고, '서울인조별서유기비서울인조별서유기비' 행의 state와 city 값은 null 처리
df_seoul_2[~df_seoul_2.state.str.contains('서울특별시')]
# df_seoul_2[df_seoul_2.state.str.contains('서울')]


# In[13]:


# 바꿔야 할 데이터들의 행 인덱스 저장해서 바꾸기
seoul_error_list = df_seoul_2[~df_seoul_2.state.str.contains('서울특별시')].index
seoul_error_list


# In[14]:


df_seoul_2.loc[67106]


# In[15]:


for i in seoul_error_list:
    if i not in [67106]:
        df_seoul_2.at[i, 'state'] = np.nan
        df_seoul_2.at[i, 'city'] = np.nan
    else:
         df_seoul_2.at[i, 'state'] = '서울특별시'

df_seoul_2.loc[seoul_error_list]


# In[16]:


# df_seoul_3 = df_seoul_2[df_seoul_2['state'].str.contains('서울')]
# # df_seoul_3 = df_seoul_2[df_seoul_2['state'].str.contains('서울')].state.unique()  # ['서울특별시', '서울틀별시', '서울시', '서울인조별서유기비서울인조별서유기비']
# df_seoul_3 = df_seoul_3[~df_seoul_3['state'].str.contains('서울인조별서유기비서울인조별서유기비')]
df_seoul_2.state.unique()


# In[17]:


# state 오류난 것 수정
# df_seoul_3.loc[~df_seoul_3.state.str.contains('서울특별시'), 'state'] = '서울특별시'
# df_seoul_3.state.unique()


# In[18]:


# df_seoul_3.info()


# ### 세종

# In[19]:


# 파일 리스트 확인 (주의: 파일명 반복문으로 돌릴 수 있게 규칙성 있는 파일명으로 통일)
import os
os.listdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/세종')


# In[20]:


# 파일 여러개 한 번에 불러오기
## 1. 파일 리스트 저장
sejongs = os.listdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/세종')

## 2. 현재 작업 위치로 이동
os.chdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/세종')

## 3. 데이터 프레임 생성하고 모든 파일 합치기
# 새로운 데이터프레임 생성
df_all_sejong = pd.DataFrame()

for sejong in sejongs:
    df = pd.read_csv(sejong, encoding='cp949')
    df_all_sejong = pd.concat([df_all_sejong, df])

df_all_sejong = df_all_sejong.reset_index(drop=True)
df_all_sejong


# In[21]:


# 필요한 칼럼만 남기기
df_sejong = df_all_sejong[['설치개수','소재지도로명주소', '소재지지번주소', '위도', '경도', '데이터기준일자']]
df_sejong


# In[22]:


# 결측값 확인
df_sejong.isnull().sum()


# In[23]:


# 도로명주소 + 지번주소 합치기 -> '주소'
df_sejong['주소'] = np.where(pd.notnull(df_sejong['소재지도로명주소']) == True, df_sejong['소재지도로명주소'], df_sejong['소재지지번주소'])
df_sejong['주소'].isna().sum()


# In[24]:


# 도로명주소 + 지번주소 drop
## 도로명주소 + 지번주소 제외한 나머지 
df_sejong_2 = df_sejong[df_sejong.columns.difference(['소재지도로명주소', '소재지지번주소'])]
# 칼럼 순서 바꾸기
df_sejong_2 = df_sejong_2[['주소', '위도', '경도', '설치개수', '데이터기준일자']]
# 칼럼명 변경
df_sejong_2 = df_sejong_2.rename(columns={"주소": "address", 
                                        "위도": "lat", 
                                        "경도": "long",
                                       "설치개수": "install_cnt",
                                       "데이터기준일자": "date"})
df_sejong_2


# In[25]:


# 주소 분리 -> 시/도
## 공백 기준으로 분리
df_sejong_2['state'] = df_sejong_2['address'].str.split().str[0]
df_sejong_2['city'] = df_sejong_2['address'].str.split().str[1]
# 칼럼 순서 바꾸기
df_sejong_2 = df_sejong_2[['address', 'state', 'city', 'lat', 'long', 'install_cnt', 'date']]
df_sejong_2


# In[26]:


df_sejong_2.state.unique()
# # df_incheon_2.loc[~df_incheon_2.state.str.contains('전라남도'), 'state'] = '전라남도'
# df_ulsan_2[df_ulsan_2['address'].str.startswith('울산광역시')]
# # df_incheon_2.drop(2583, axis=0, inplace=True)
# df_ulsan_2.state.unique()


# ### 울산

# In[27]:


# 파일 여러개 한 번에 불러오기
## 1. 파일 리스트 저장
ulsans = os.listdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/울산')

## 2. 현재 작업 위치로 이동
os.chdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/울산')

## 3. 데이터 프레임 생성하고 모든 파일 합치기
# 새로운 데이터프레임 생성
df_all_ulsan = pd.DataFrame()

for ulsan in ulsans:
    df = pd.read_csv(ulsan, encoding='cp949')
    df_all_ulsan = pd.concat([df_all_ulsan, df])

df_all_ulsan = df_all_ulsan.reset_index(drop=True)
df_all_ulsan


# In[28]:


# 필요한 칼럼만 남기기
df_ulsan = df_all_ulsan[['설치개수','소재지도로명주소', '소재지지번주소', '위도', '경도', '데이터기준일자']]

# 결측값 확인
df_ulsan.isnull().sum()


# In[29]:


# 도로명주소 + 지번주소 합치기 -> '주소'
df_ulsan['주소'] = np.where(pd.notnull(df_ulsan['소재지도로명주소']) == True, df_ulsan['소재지도로명주소'], df_ulsan['소재지지번주소'])
df_ulsan['주소'].isna().sum()


# In[30]:


# 도로명주소 + 지번주소 drop
## 도로명주소 + 지번주소 제외한 나머지 
df_ulsan_2 = df_ulsan[df_ulsan.columns.difference(['소재지도로명주소', '소재지지번주소'])]
# 칼럼 순서 바꾸기
df_ulsan_2 = df_ulsan_2[['주소', '위도', '경도', '설치개수', '데이터기준일자']]
# 칼럼명 변경
df_ulsan_2 = df_ulsan_2.rename(columns={"주소": "address", 
                                        "위도": "lat", 
                                        "경도": "long",
                                       "설치개수": "install_cnt",
                                       "데이터기준일자": "date"})
# 주소 분리 -> 시/도
## 공백 기준으로 분리
df_ulsan_2['state'] = df_ulsan_2['address'].str.split().str[0]
df_ulsan_2['city'] = df_ulsan_2['address'].str.split().str[1]
# 칼럼 순서 바꾸기
df_ulsan_2 = df_ulsan_2[['address', 'state', 'city', 'lat', 'long', 'install_cnt', 'date']]

df_ulsan_2


# In[31]:


df_ulsan_2.state.unique()
# # df_incheon_2.loc[~df_incheon_2.state.str.contains('전라남도'), 'state'] = '전라남도'
# df_ulsan_2[df_ulsan_2['address'].str.startswith('울산광역시')]
# # df_incheon_2.drop(2583, axis=0, inplace=True)
# df_ulsan_2.state.unique()


# ### 인천

# In[32]:


# 파일 여러개 한 번에 불러오기
## 1. 파일 리스트 저장
incheons = os.listdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/인천')

## 2. 현재 작업 위치로 이동
os.chdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/인천')

## 3. 데이터 프레임 생성하고 모든 파일 합치기
# 새로운 데이터프레임 생성
df_all_incheon = pd.DataFrame()

for incheon in incheons:
    df = pd.read_csv(incheon, encoding='cp949')
    df_all_incheon = pd.concat([df_all_incheon, df])

df_all_incheon = df_all_incheon.reset_index(drop=True)
df_all_incheon


# In[33]:


# 필요한 칼럼만 남기기
df_incheon = df_all_incheon[['설치개수','소재지도로명주소', '소재지지번주소', '위도', '경도', '데이터기준일자']]

# 결측값 확인
df_incheon.isnull().sum()

# 도로명주소 + 지번주소 합치기 -> '주소'
df_incheon['주소'] = np.where(pd.notnull(df_incheon['소재지도로명주소']) == True, df_incheon['소재지도로명주소'], df_incheon['소재지지번주소'])
df_incheon['주소'].isna().sum()


# In[34]:


# 도로명주소 + 지번주소 drop
## 도로명주소 + 지번주소 제외한 나머지 
df_incheon_2 = df_incheon[df_incheon.columns.difference(['소재지도로명주소', '소재지지번주소'])]
# 칼럼 순서 바꾸기
df_incheon_2 = df_incheon_2[['주소', '위도', '경도', '설치개수', '데이터기준일자']]
# 칼럼명 변경
df_incheon_2 = df_incheon_2.rename(columns={"주소": "address", 
                                        "위도": "lat", 
                                        "경도": "long",
                                       "설치개수": "install_cnt",
                                       "데이터기준일자": "date"})
# 주소 분리 -> 시/도
## 공백 기준으로 분리
df_incheon_2['state'] = df_incheon_2['address'].str.split().str[0]
df_incheon_2['city'] = df_incheon_2['address'].str.split().str[1]
# 칼럼 순서 바꾸기
df_incheon_2 = df_incheon_2[['address', 'state', 'city', 'lat', 'long', 'install_cnt', 'date']]

df_incheon_2


# In[35]:


# 주소에 '인천'이 포함된 주소만 남기고, '경기도' 행은 삭제
df_incheon_2.loc[~df_incheon_2.state.str.contains('인천'), 'state'].unique()


# In[36]:


df_incheon_2.state.unique()  # 경기도 데이터 1개 들어가 있음. -> 삭제

df_incheon_2[df_incheon_2['address'].str.startswith('경기도')]
df_incheon_2.drop(12502, axis=0, inplace=True)
df_incheon_2.state.unique()


# ### 전라남도

# In[37]:


# 파일 여러개 한 번에 불러오기
## 1. 파일 리스트 저장
jns = os.listdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/전라남도')

## 2. 현재 작업 위치로 이동
os.chdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/전라남도')

## 3. 데이터 프레임 생성하고 모든 파일 합치기
# 새로운 데이터프레임 생성
df_all_jn = pd.DataFrame()

for jn in jns:
    df = pd.read_csv(jn, encoding='cp949')
    df_all_jn = pd.concat([df_all_jn, df])

df_all_jn = df_all_jn.reset_index(drop=True)
df_all_jn


# In[38]:


# 필요한 칼럼만 남기기
df_jn = df_all_jn[['설치개수','소재지도로명주소', '소재지지번주소', '위도', '경도', '데이터기준일자']]

# 결측값 확인
df_jn.isnull().sum()

# 도로명주소 + 지번주소 합치기 -> '주소'
df_jn['주소'] = np.where(pd.notnull(df_jn['소재지도로명주소']) == True, df_jn['소재지도로명주소'], df_jn['소재지지번주소'])
df_jn['주소'].isna().sum()


# In[39]:


# 도로명주소 + 지번주소 drop
## 도로명주소 + 지번주소 제외한 나머지 
df_jn_2 = df_jn[df_jn.columns.difference(['소재지도로명주소', '소재지지번주소'])]
# 칼럼 순서 바꾸기
df_jn_2 = df_jn_2[['주소', '위도', '경도', '설치개수', '데이터기준일자']]
# 칼럼명 변경
df_jn_2 = df_jn_2.rename(columns={"주소": "address", 
                                        "위도": "lat", 
                                        "경도": "long",
                                       "설치개수": "install_cnt",
                                       "데이터기준일자": "date"})
# 주소 분리 -> 시/도
## 공백 기준으로 분리
df_jn_2['state'] = df_jn_2['address'].str.split().str[0]
df_jn_2['city'] = df_jn_2['address'].str.split().str[1]
# 칼럼 순서 바꾸기
df_jn_2 = df_jn_2[['address', 'state', 'city', 'lat', 'long', 'install_cnt', 'date']]

df_jn_2


# In[40]:


# 주소에 '전라남도'이 포함된 주소만 남기고, '경기도' 행은 삭제
df_jn_2.loc[~df_jn_2.state.str.contains('전라남도'), 'state'].unique()


# In[41]:


# df_jn_2[df_jn_2.state != '전라남도']
# df_jn_2[df_jn_2.state != '전라남도'].state.unique()


# In[42]:


# 경기도 삭제
df_jn_3 = df_jn_2[~df_jn_2['state'].str.contains('경기도')].reset_index(inplace=False)
df_jn_3 = df_jn_3.drop(['index'], axis=1)
df_jn_3[df_jn_3.state != '전라남도'].state.unique()


# In[43]:


df_jn_3[df_jn_3.state != '전라남도']
# df_jn_3[df_jn_3.state == '역리사거리~터미널']


# In[44]:


'''
['영암읍교회', '영암읍', '엉암읍', '덕진', '금정면', '시종면', '덕진면', '도포면', '미암면',
       '서호면', '군서면', '신북면', '학산면', '영암초등학교', '잠곡동길', '삼호읍', ('역리사거리~터미널'),
       ('공용주차장', '80W설치'), '하정웅미술관', '영암읍송평로334', ('대봉간336L4R17L18'),
       '영암성당(영암읍)', '영암로', '남', '함평군']
'''
# 수정
jn_error_list = df_jn_3[df_jn_3.state != '전라남도'].index
# jn_error_list
for i in jn_error_list:
    if i not in [114726, 139008]:
        df_jn_3.at[i, 'state'] = '전라남도'
        df_jn_3.at[i, 'city'] = '영암군'    
    else:
        df_jn_3.at[i, 'state'] = '전라남도'
# ()표시한 부분은 nan 처리 (정확한 위치 파악 어렵기 때문)
for j in [109195, 109216, 109529, 109123]:
    df_jn_3.at[j, 'state'] = np.nan
    df_jn_3.at[j, 'city'] = np.nan
    
df_jn_3.loc[jn_error_list]
# print(df_jn_3.loc[[jn_error_list]])
df_jn_3[df_jn_3.state.isnull()]


# In[45]:


df_jn_3.state.unique()
# df_jn_2.loc[~df_jn_2.state.str.contains('전라남도'), 'state'] = '전라남도'
# # df_jn_2[~df_jb_2['address'].str.startswith('전라북도')]
# df_jn_2.state.unique()


# ### 전라북도

# In[46]:


# 파일 여러개 한 번에 불러오기
## 1. 파일 리스트 저장
jbs = os.listdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/전라북도')

## 2. 현재 작업 위치로 이동
os.chdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/전라북도')

## 3. 데이터 프레임 생성하고 모든 파일 합치기
# 새로운 데이터프레임 생성
df_all_jb = pd.DataFrame()

for jb in jbs:
    df = pd.read_csv(jb, encoding='cp949')
    df_all_jb = pd.concat([df_all_jb, df])

df_all_jb = df_all_jb.reset_index(drop=True)
df_all_jb


# In[47]:


# 필요한 칼럼만 남기기
df_jb = df_all_jb[['설치개수','소재지도로명주소', '소재지지번주소', '위도', '경도', '데이터기준일자']]

# 결측값 확인
df_jb.isnull().sum()

# 도로명주소 + 지번주소 합치기 -> '주소'
df_jb['주소'] = np.where(pd.notnull(df_jb['소재지도로명주소']) == True, df_jb['소재지도로명주소'], df_jb['소재지지번주소'])
df_jb['주소'].isna().sum()


# In[48]:


# 도로명주소 + 지번주소 drop
## 도로명주소 + 지번주소 제외한 나머지 
df_jb_2 = df_jb[df_jb.columns.difference(['소재지도로명주소', '소재지지번주소'])]
# 칼럼 순서 바꾸기
df_jb_2 = df_jb_2[['주소', '위도', '경도', '설치개수', '데이터기준일자']]
# 칼럼명 변경
df_jb_2 = df_jb_2.rename(columns={"주소": "address", 
                                        "위도": "lat", 
                                        "경도": "long",
                                       "설치개수": "install_cnt",
                                       "데이터기준일자": "date"})
# 주소 분리 -> 시/도
## 공백 기준으로 분리
df_jb_2['state'] = df_jb_2['address'].str.split().str[0]
df_jb_2['city'] = df_jb_2['address'].str.split().str[1]
# 칼럼 순서 바꾸기
df_jb_2 = df_jb_2[['address', 'state', 'city', 'lat', 'long', 'install_cnt', 'date']]

df_jb_2


# In[49]:


# 주소에 '전라북도'이 포함된 주소만 남기고, '전주시' 행 확인 후 필요없으면 삭제
df_jb_2.loc[~df_jb_2.state.str.contains('전라북도'), 'state'].unique()


# In[50]:


df_jb_2[df_jb_2.state.str.contains('전주시')]


# In[51]:


df_jb_2.loc[df_jb_2.state == '전주시', 'city'] = "전주시"
df_jb_2.loc[df_jb_2.city == '전주시', 'state'] = '전라북도'
df_jb_2.loc[df_jb_2.city == '전주시']
df_jb_2.state.unique()


# In[52]:


# state == '전북전라북도' 확인 --> state명 변경 (전북전라북도 -> 전라북도)
df_jb_2[df_jb_2.state == '전북전라북도']


# In[53]:


# --> state명 변경 (전북전라북도 -> 전라북도)
df_jb_2.loc[df_jb_2.state == '전북전라북도', 'state'] = "전라북도"
df_jb_2.state.unique()


# In[54]:


# df_jb_2.state.unique()

# df_jb_2.loc[df_jb_2.state.str.contains('전라북도'), 'state'] = '전라북도'
# df_jb_2[~df_jb_2['address'].str.startswith('전라북도')]
# df_jb_2.state.unique()


# ### 제주도

# In[55]:


# 파일 여러개 한 번에 불러오기
## 1. 파일 리스트 저장
jejus = os.listdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/제주도')

## 2. 현재 작업 위치로 이동
os.chdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/제주도')

## 3. 데이터 프레임 생성하고 모든 파일 합치기
# 새로운 데이터프레임 생성
df_all_jeju = pd.DataFrame()

for jeju in jejus:
    df = pd.read_csv(jeju, encoding='cp949')
    df_all_jeju = pd.concat([df_all_jeju, df])

df_all_jeju = df_all_jeju.reset_index(drop=True)
df_all_jeju


# In[56]:


# 필요한 칼럼만 남기기
df_jeju = df_all_jeju[['설치개수','소재지도로명주소', '소재지지번주소', '위도', '경도', '데이터기준일자']]

# 결측값 확인
df_jeju.isnull().sum()

# 도로명주소 + 지번주소 합치기 -> '주소'
df_jeju['주소'] = np.where(pd.notnull(df_jeju['소재지도로명주소']) == True, df_jeju['소재지도로명주소'], df_jeju['소재지지번주소'])
df_jeju['주소'].isna().sum()


# In[57]:


# 도로명주소 + 지번주소 drop
## 도로명주소 + 지번주소 제외한 나머지 
df_jeju_2 = df_jeju[df_jeju.columns.difference(['소재지도로명주소', '소재지지번주소'])]
# 칼럼 순서 바꾸기
df_jeju_2 = df_jeju_2[['주소', '위도', '경도', '설치개수', '데이터기준일자']]
# 칼럼명 변경
df_jeju_2 = df_jeju_2.rename(columns={"주소": "address", 
                                        "위도": "lat", 
                                        "경도": "long",
                                       "설치개수": "install_cnt",
                                       "데이터기준일자": "date"})
# 주소 분리 -> 시/도
## 공백 기준으로 분리
df_jeju_2['state'] = df_jeju_2['address'].str.split().str[0]
df_jeju_2['city'] = df_jeju_2['address'].str.split().str[1]
# 칼럼 순서 바꾸기
df_jeju_2 = df_jeju_2[['address', 'state', 'city', 'lat', 'long', 'install_cnt', 'date']]

df_jeju_2


# In[58]:


df_jeju_2.state.unique()
# df_jeju_2.loc[~df_jeju_2.state.str.contains('제주특별자치도'), 'state'] = '제주특별자치도'
# df_jeju_2[~df_jeju_2['address'].str.startswith('제주특별자치도')]


# ### 충청남도

# In[59]:


# 파일 여러개 한 번에 불러오기
## 1. 파일 리스트 저장
chungns = os.listdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/충청남도')

## 2. 현재 작업 위치로 이동
os.chdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/충청남도')

## 3. 데이터 프레임 생성하고 모든 파일 합치기
# 새로운 데이터프레임 생성
df_all_chungn = pd.DataFrame()

for chungn in chungns:
    df = pd.read_csv(chungn, encoding='cp949')
    df_all_chungn = pd.concat([df_all_chungn, df])

df_all_chungn = df_all_chungn.reset_index(drop=True)
df_all_chungn


# In[60]:


# 필요한 칼럼만 남기기
df_chungn = df_all_chungn[['설치개수','소재지도로명주소', '소재지지번주소', '위도', '경도', '데이터기준일자']]

# 결측값 확인
df_chungn.isnull().sum()

# df_chungn
# 도로명주소 + 지번주소 합치기 -> '주소'
df_chungn['주소'] = np.where(pd.notnull(df_chungn['소재지도로명주소']) == True, df_chungn['소재지도로명주소'], df_chungn['소재지지번주소'])
df_chungn['주소'].isna().sum()

# df_chungn


# In[61]:


# 도로명주소 + 지번주소 drop
## 도로명주소 + 지번주소 제외한 나머지 
df_chungn_2 = df_chungn[df_chungn.columns.difference(['소재지도로명주소', '소재지지번주소'])]
# 칼럼 순서 바꾸기
df_chungn_2 = df_chungn_2[['주소', '위도', '경도', '설치개수', '데이터기준일자']]
# 칼럼명 변경
df_chungn_2 = df_chungn_2.rename(columns={"주소": "address", 
                                        "위도": "lat", 
                                        "경도": "long",
                                       "설치개수": "install_cnt",
                                       "데이터기준일자": "date"})
# 주소 분리 -> 시/도
# 공백 기준으로 분리
df_chungn_2['state'] = df_chungn_2['address'].str.split().str[0]
df_chungn_2['city'] = df_chungn_2['address'].str.split().str[1]


# 칼럼 순서 바꾸기
df_chungn_2 = df_chungn_2[['address', 'state', 'city', 'lat', 'long', 'install_cnt', 'date']]

df_chungn_2


# In[62]:


# state 값 제대로 들어가 있는지 확인
df_chungn_2.state.unique()


# In[63]:


df_chungn_2[~df_chungn_2.state.str.contains('충청남도')]
# 확인 결과, 아래 모든 행들은 '충청남도 서산시'에 해당됨. -> state & city 값 바꿔주기


# In[64]:


chn_error_list = df_chungn_2[~df_chungn_2.state.str.contains('충청남도')].index
# chn_error_list
for l in chn_error_list:
    df_chungn_2.at[l, 'state'] = '충청남도'
    df_chungn_2.at[l, 'city'] = '서산시'
    
df_chungn_2.state.unique()

df_chungn_2[~df_chungn_2.address.str.contains('충청남도')]


# In[65]:


df_chungn_2[df_chungn_2.address == '부춘동 충청남도 서산시 갈산동 407-2']


# ### 충청북도

# In[66]:


# 파일 여러개 한 번에 불러오기
## 1. 파일 리스트 저장
chungbs = os.listdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/충청북도')

## 2. 현재 작업 위치로 이동
os.chdir('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/data/rawdata/rawdata_보안등/rawdata/충청북도')

## 3. 데이터 프레임 생성하고 모든 파일 합치기
# 새로운 데이터프레임 생성
df_all_chungb = pd.DataFrame()

for chungb in chungbs:
    df = pd.read_csv(chungb, encoding='cp949')
    df_all_chungb = pd.concat([df_all_chungb, df])

df_all_chungb = df_all_chungb.reset_index(drop=True)
df_all_chungb


# In[67]:


# 필요한 칼럼만 남기기
df_chungb = df_all_chungb[['설치개수','소재지도로명주소', '소재지지번주소', '위도', '경도', '데이터기준일자']]

# 결측값 확인
df_chungn.isnull().sum()

# df_chungn
# 도로명주소 + 지번주소 합치기 -> '주소'
df_chungb['주소'] = np.where(pd.notnull(df_chungb['소재지도로명주소']) == True, df_chungb['소재지도로명주소'], df_chungb['소재지지번주소'])
df_chungb['주소'].isna().sum()

df_chungb


# In[68]:


# 도로명주소 + 지번주소 drop
## 도로명주소 + 지번주소 제외한 나머지 
df_chungb_2 = df_chungb[df_chungb.columns.difference(['소재지도로명주소', '소재지지번주소'])]
# 칼럼 순서 바꾸기
df_chungb_2 = df_chungb_2[['주소', '위도', '경도', '설치개수', '데이터기준일자']]
# 칼럼명 변경
df_chungb_2 = df_chungb_2.rename(columns={"주소": "address", 
                                        "위도": "lat", 
                                        "경도": "long",
                                       "설치개수": "install_cnt",
                                       "데이터기준일자": "date"})
# 주소 분리 -> 시/도
## 공백 기준으로 분리
df_chungb_2['state'] = df_chungb_2['address'].str.split().str[0]
df_chungb_2['city'] = df_chungb_2['address'].str.split().str[1]
# 칼럼 순서 바꾸기
df_chungb_2 = df_chungb_2[['address', 'state', 'city', 'lat', 'long', 'install_cnt', 'date']]

df_chungb_2


# In[69]:


df_chungb_2.state.unique()  # ['충청북도', '경상북도', '서울특별시']

# df_chungb_2.loc[~df_chungb_2.state.str.contains('서울특별시'), 'state'] = '서울특별시'
df_chungb_2[df_chungb_2['address'].str.startswith('경상북도')]  # 1개
df_chungb_2[df_chungb_2['address'].str.startswith('서울특별시')]  # 1개
df_chungb_2.drop([5252, 5253], axis=0, inplace=True)
df_chungb_2.state.unique()


# ## 데이터 합치기 (서울 ~ 충청북도)

# In[70]:


# [df_seoul_2, df_sejong_2, df_ulsan_2, df_incheon_2, df_jn_3, df_jb_2, df_jeju_2, df_chungn_2, df_chungb_2]
df_incheon_2.state.unique()


# In[71]:


df_sclight_2 = pd.concat([df_seoul_2, df_sejong_2, df_ulsan_2, df_incheon_2, df_jn_3, df_jb_2, df_jeju_2, df_chungn_2, df_chungb_2], ignore_index=True)
df_sclight_2


# In[72]:


df_sclight_2.state.unique()


# In[73]:


df_sclight_2.info()


# ## 전체 데이터 오류 확인

# In[74]:


df_sclight_2.isnull().sum()


# #### state 명 확인 및 지역 고윳값으로만 통일

# In[75]:


# # city 결측값 인덱스 추출 (리스트로 저장)
# sclight2_city_null = df_sclight2.loc[df_sclight2['city'].isnull()].index.tolist()

# # lat 결측값 인덱스 추출 (리스트로 저장)
# sclight2_lat_null = df_sclight2.loc[df_sclight2['lat'].isnull()].index.tolist()

# # long 결측값 인덱스 추출 (리스트로 저장)
# sclight2_long_null = df_sclight2.loc[df_sclight2['long'].isnull()].index.tolist()

# # 위 3개의 결측값 인덱스 리스트를 딕셔너리로 만들기
# dict_sclight2_null = {'city': sclight2_city_null, 'lat': sclight2_lat_null, 'long': sclight2_long_null}
# dict_sclight2_null

# # 보기 좋게 출력
# import pprint
# pprint.pprint(dict_sclight2_null)


# In[76]:


## 주소명 이상하게 들어가 있는 부분 찾기
df_sclight_2.state.value_counts()
df_sclight_2.state.unique().tolist()


# In[77]:


df_sclight_2.city.unique().tolist()


# #### 위도 경도 관련 drop할 행 확인

# In[78]:


df_sclight_2.columns


# In[79]:


df_sclight_2


# ####  'city, state, lat, long' 경우의 수 제거

# In[80]:


# 모두 없음
df_sclight_2[df_sclight_2['state'].isna() & df_sclight_2['city'].isna() & df_sclight_2['lat'].isna() & df_sclight_2['long'].isna()].info()
# 위도만 있음
df_sclight_2[df_sclight_2['state'].isna() & df_sclight_2['city'].isna() & df_sclight_2['lat'].notnull() & df_sclight_2['long'].isna()].info()
# 경도만 있음
df_sclight_2[df_sclight_2['state'].isna() & df_sclight_2['city'].isna() & df_sclight_2['lat'].isna() & df_sclight_2['long'].notnull()].info()
    


# In[81]:


# ['city', 'state', 'lat', 'long']
# 경우의 수: [X X X X] [X X O X] [X X X O]
# --> 제거할 행의 인덱스를 저장해서 전체 데이터에서 제거해보자.

# 모두 없음
null_all = df_sclight_2[df_sclight_2['state'].isna() & df_sclight_2['city'].isna() & df_sclight_2['lat'].isna() & df_sclight_2['long'].isna()].index.tolist()
# 위도만 있음
notnull_lat = df_sclight_2[df_sclight_2['state'].isna() & df_sclight_2['city'].isna() & df_sclight_2['lat'].notnull() & df_sclight_2['long'].isna()].index.tolist()
# 경도만 있음
notnull_long = df_sclight_2[df_sclight_2['state'].isna() & df_sclight_2['city'].isna() & df_sclight_2['lat'].isna() & df_sclight_2['long'].notnull()].index.tolist()

# 정보 확인
len(null_all), len(notnull_lat), len(notnull_long)


# In[82]:


# 삭제할 행 인덱스 저장할 빈 리스트 생성
null_rows = null_all + notnull_lat + notnull_long

# 중복값 삭제
null_rows = list(set(null_rows))

# 정렬
null_rows.sort()

len(null_rows)
null_rows


# In[83]:


# 원래 데이터셋에서 삭제할 행 인데스로 제거하기
df_sclight2 = df_sclight_2.drop(null_rows, axis=0, inplace=False)
# index 초기화
df_sclight2 = df_sclight2.reset_index(drop=True)


# In[84]:


# 최종본
df_sclight2


# In[85]:


df_sclight2.info()
# df_sclight2[df_sclight2.state.isna()]


# ## 시도별 Group_by

# In[86]:


# 보안등 개수 sum 필요
df_sclight2.install_cnt.unique()


# In[87]:


# 데이터프레임 크기 조절
# pd.set_option('display.max.colwidth', 100)

df_sclight2.head()


# In[88]:


# 시도/군구별 평균값 
df_sclight2.groupby(['state', 'city']).mean()


# In[89]:


# 시도/군구별 
# ['lat', 'long']: 평균값
# ['install_cnt']: 합계

df_sclight2_StCi = df_sclight2.groupby(['state', 'city']).agg({
    'lat': 'mean',
    'long': 'mean',
    'install_cnt': 'sum'}).reset_index()

# df_sclight2_StCi.info()
df_sclight2_StCi


# ## EDA: 시도별 보안등 개수

# ### Bar Graph

# In[147]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib
# 한글 꺠짐 방지 
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False


# In[148]:


df_sclight2_StCi.columns


# - 참고: https://hleecaster.com/python-seaborn-color/

# In[149]:


g_state = df_sclight2_StCi.groupby(['state'])['install_cnt'].sum().reset_index()
g_state


# In[150]:


# import warnings
# # 경고 메시지를 무시하고 숨기기
# warnings.filterwarnings(action='ignore')
# 숨기기했던 경고 메시지를 다시 보이게
# warnings.filterwarnings(action='default')
colors = ['black','dimgray','dimgrey', 'grey','darkgray','silver','lightgray', 'lightgrey', 'gainsboro'] # 색상 지정

title_font = {
    'fontsize': 25,
    'fontweight': 'bold',
}

lable_font = {
    'fontsize': 15,
    'fontweight': 'bold',
    
}

plt.figure(figsize=(16,8))
plt.bar(g_state['state'], g_state['install_cnt'], color=colors)
plt.xlabel('시도명', fontdict=lable_font, labelpad=10)
plt.ylabel('보안등 개수', fontdict=lable_font, labelpad=10)
plt.title('시도별 보안등 개수 현황', fontdict=title_font, pad=30)
plt.grid(True,color='gray', alpha=0.3, linestyle='--')
# plt.rc('font', family="Malgun Gothic") #그래프 내부의 한글 깨짐 처리
plt.show()


# In[155]:


sns.set(font='Malgun Gothic', rc={'axes.unicode_minus':False}, style='darkgrid')
# sns.set_theme(style='whitegrid')

# qualitative_colors = sns.color_palette("Set3", 10)
# sns.palplot(qualitative_colors)

sns.barplot(data=g_state,
            x='install_cnt', 
            y='state',
           orient='h',
           palette='BuGn',
           )


# In[ ]:





# In[ ]:





# In[ ]:





# ### Folium 지도 시각화

# # 위경도 있는 데이터만 저장
# # df_sclight_g = df_sclight2.dropna(subset=['lat', 'long'], inplace=False)
# df_sclight_g = df_sclight2.dropna(inplace=False)
# df_sclight_g = df_sclight_g.reset_index(drop=True)
# df_sclight_g.info()

# # 라이브러리 설치
# # !pip install folium

# # 라이브러리 호출
# import folium as g

# # city, 위도, 경도 데이터만 따로 저장
# sclight_city = df_sclight_g['city']
# sclight_x = df_sclight_g['lat']
# sclight_y = df_sclight_g['long']

# #지도의 중심을 지정하기 위해 위도와 경도의 평균 구하기
# mean_lat = df_sclight_g['lat'].mean()
# mean_long = df_sclight_g['long'].mean()
# 
# print(mean_lat, mean_long)

# ## 지도 띄우기
# 
# # Map 함수에서 location으로 처음 화면이 나오는 부분 설정
# # zoom_start: 처음 지도를 봤을 때 확대 정도
# m = g.Map([mean_lat, mean_long], zoom_start = 9)

# coords = []
# 
# for i in range(len(df_sclight_g)):
#     x = sclight_x[i]
#     y = sclight_y[i]
#     coords.append([x, y])
#     
# for i in range(len(coords)):
#     g.Circle(
#         location = coords[i],
#         radius = 50,
#         color = '#000000',
#         fill = 'crimson',
#     ).add_to(m)
# 
# m.save('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/results/map.html')

# # Case 2
# 
# '''
# - x, y 좌표와 city를 받아서 dict 형태로 만들고 
# - x, y 좌표를 QGIS 지도 좌표계에 맞게 변환 (to EPSG:3857)
# - 후에 point들을 .shp로 내보내기 
# '''
# 
# TRAN_4326_TO_3857 = Transformer.from_crs("EPSG:4326", "EPSG:3857") 
#     # EPSG:3857좌표계로 변환
#     # "ESPG:3857"을 다른 좌표계로 바꾸면 무한하게 응용 가능
#     
# points = []
# ttareung = []
# 
# for i in range(len(df_sclight_g)): # 마지막 인덱스에 NaN이 존재해서 -1
#     
#     idx = sclight_city[i]
#     x_coord = sclight_x[i]
#     y_coord = sclight_y[i]
#     
#     xx, yy = TRAN_4326_TO_3857.transform(x_coord, y_coord) # 변환하는 과정
#     sclight_dict = {'ID': idx, 'x_coord': xx, 'y_coord': yy}
#     
#     if i % 20 == 0: 
#         print(f'{i}th station is working...')
#     
#     points.append(point(xx, yy))
#     ttareung.append(sclight_dict)
# 
# points = gpd.GeoDataFrame(geometry = points)
# points.to_file('C:/Users/samsung/TIL/DS/project/miniPJ/01_pj/results/tta_points.shp', driver="Shapefile")
