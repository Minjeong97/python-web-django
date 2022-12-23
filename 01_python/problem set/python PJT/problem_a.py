# 1. 브라우저 주소창에
## 1. 뭐가됐든 client(request 보낼 수 있는 프로그램이면 뭐든) 프로그램을 준비해서
## cf) https://requests.readthedocs.io/en/latest/
## git bash 창에 'pip install requests' 설치

import requests

key = '95b3753b13ee4da85b01fd219aed52e5'
url = 'https://api.themoviedb.org/3/movie/popular?api_key=95b3753b13ee4da85b01fd219aed52e5&language=ko-KR'
data = requests.get(url).json()
# print(data)



def popular_count():
    count = len(data['results'])
    return count
    # 여기에 코드를 작성합니다.  


if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
