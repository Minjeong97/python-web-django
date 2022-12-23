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
        if pop_results[idx]['vote_average'] >= 8:
            vote_eight.append(pop_results[idx])
            
    return vote_eight
        


'''강사님 피드백
def vote_average_movies():
    for movie in pop_results:
        if movie['vote_average'] > 8:
            vote_eight.append(movie)
            
    # 'filter()' 로도 한 번 해보기!
    
    return vote_eight
'''    


'''
def vote_average_movies():
    pop_results = data['results']
    vote_eight = []
    for pop in pop_results:
        if pop['vote_average'] >= 8:
            vote_eight.append(pop['vote_average'])
    
    return vote_average_movies
'''

    # 여기에 코드를 작성합니다.  

if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
