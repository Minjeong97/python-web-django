# 라이브러리 호출
import os
import pandas as pd


# 파일 불러오기
seoul_GN = pd.read_csv('./data/rawdata/rawdata_보안등/rawdata/서울/서울특별시_강남구_보안등정보_20230103.csv')
seoul_GN.head()