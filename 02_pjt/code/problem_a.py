import requests


def popular_count():

    # tmdb 인기영화 정보 api url 를 받아 정보를 받아옴
    url = "https://api.themoviedb.org/3/movie/popular?api_key=fe0cd3ae385a968eaa140d8955cf4804&language=en-US&page=1"
    response = requests.get(url).json()

    # 몇개의 영화 정보가 있는 cnt 라는 변수를 만들어 직접 for문 돌며 카운트
    cnt = 0
    for movie in response['results']:
        cnt += 1

    return cnt
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
