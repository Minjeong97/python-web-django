from pprint import pprint

import requests

key = '95b3753b13ee4da85b01fd219aed52e5'
url = 'https://api.themoviedb.org/3/movie/popular?api_key=95b3753b13ee4da85b01fd219aed52e5&language=ko-KR'
data = requests.get(url).json()
# print(data)


pop_results = data['results']
vote_eight = []

# solution 1.
def vote_average_movies():
    return list(filter(lambda movie: movie['vote_average'] >= 8, pop_results))
    # for movie in filter(lambda movie: movie['vote_average'] >= 8, pop_results):
    #     vote_eight.append(movie)


# solution 2.
def vote_average_movies():
    print(list(filter(lambda movie: movie['vote_average'] >= 8, pop_results)))
    for movie in filter(lambda movie: movie['vote_average'] >= 8, pop_results):
        vote_eight.append(movie)
        
    return vote_eight

if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())