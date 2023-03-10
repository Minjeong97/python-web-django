from pprint import pprint

import requests

key = '95b3753b13ee4da85b01fd219aed52e5'
url = 'https://api.themoviedb.org/3/movie/popular?api_key=95b3753b13ee4da85b01fd219aed52e5&language=ko-KR'

data = requests.get(url).json()
# print(data)

recm_data = ''
title_lists = []

def recommendation(title):
    search = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=95b3753b13ee4da85b01fd219aed52e5&query={title}').json()
    
    
    if search['results'] == list():
        return None
    
    elif search['results'][0]['original_title'] == title:
        movie_id = search['results'][0]['id']
    
        recm_url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=95b3753b13ee4da85b01fd219aed52e5&language=ko-KR'
        recm_data = requests.get(recm_url).json()
        
        for n in range(len(recm_data)):
            title_lists.append(recm_data['results'][n]['title'])
            # map() 함수로 이름만 추출 가능
        
        return title_lists
    else:
        return list()
            

    
    # 여기에 코드를 작성합니다.  


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 ls영화'))
    # => None
