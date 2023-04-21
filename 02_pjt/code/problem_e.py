import requests
from pprint import pprint


def credits(title):

    # 영화 제목을 parameter로 받아와 search_url 쿼리 안에 넣어주고 해당 json 파일을 받아옴
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key=fe0cd3ae385a968eaa140d8955cf4804&language=ko-KR&page=1&include_adult=false&query={title}"

    search_response = requests.get(search_url).json()

    if search_response['results']: # 영화 서치후 첫번째 영화가 있을때
        # 영화 서치후 첫번째 영화
        movie_id = search_response['results'][0]['id']

        # cedits_url 에 search한 영화 id 값을 넣어주어 해당 영화의 credits 정보를 받아옴
        credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=fe0cd3ae385a968eaa140d8955cf4804&language=ko-KR"
        credits_response = requests.get(credits_url).json()

        # 결과 담을 리스트
        actor_list = []
        director_list = []

        # casting_actor list 와 crew list 에 credits json 정보를 하나씩 돌며 원하는 조건에 부합하면 append
        for casting_actor in credits_response['cast']:
            if casting_actor["cast_id"] < 10:
                actor_list.append(casting_actor['name'])
        
        for crew in credits_response['crew']:
            if crew['department'] == "Directing":
                director_list.append(crew['name'])

        # 최종적으로 dictionary 로 반환
        return {'cast' : actor_list, 'directing' : director_list}

    # 만약 영화 서치했는데 영화가 없다면?
    else:
        return None  # None 값 리턴

    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
