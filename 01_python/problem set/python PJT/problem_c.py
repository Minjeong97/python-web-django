from pprint import pprint

import requests

key = '95b3753b13ee4da85b01fd219aed52e5'
url = 'https://api.themoviedb.org/3/movie/popular?api_key=95b3753b13ee4da85b01fd219aed52e5&language=ko-KR'
data = requests.get(url).json()
# print(data)

def popular_count():
    count = len(data['results'])
    return count  # 20

pop_results = data['results']
vote_eight = []

def vote_average_movies():
    for idx in range(popular_count()):
        if pop_results[idx]['vote_average'] > 8:
            vote_eight.append(pop_results[idx])
    
    return vote_eight


def ranking():
    key_values = []
    values = []
    for idx in range(popular_count()):
        for k, v in pop_results[idx].items():
            if k == 'vote_average' or k == 'title':
                key_values.append(v)
    for v in range(0, len(key_values), 2):
        values.append(key_values[v:v+2])
        
    values.sort(key=lambda values: -values[1])
    # values.sort(key=lambda values: values[1], reverse=True)
    
    return values[:5]
        


'''
def ranking():
    for idx in range(popular_count()):
        key_lists = pop_results[idx]
        for item in key_lists:
            rank_results = sorted(pop_results[idx][item], reverse=True)[:5]
    return rank_results
'''

#        rank_lists = sorted(pop_results[idx]['vote_average'].items(), key = lambda item: item[1], reverse = True)[:5]
    
    #return rank_lists
    # 여기에 코드를 작성합니다.  


if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 상위 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
