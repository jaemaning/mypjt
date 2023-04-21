import requests
from pprint import pprint


def recommendation(title):

    search_url = f"https://api.themoviedb.org/3/search/movie?api_key=fe0cd3ae385a968eaa140d8955cf4804&language=ko-KR&page=1&include_adult=false&query={title}"

    search_response = requests.get(search_url).json()

    
    if search_response['results']: # 영화 서치후 첫번째 영화가 있을때
        # 영화 서치후 첫번째 영화
        movie_id = search_response['results'][0]['id'] 

        # 결과 저장할 리스트
        result = []

        # recom_url 에 search한 영화 id 값을 넣어주어 해당 영화의 recommend 정보를 받아옴
        recom_url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=fe0cd3ae385a968eaa140d8955cf4804&language=ko-KR&page=1"
        recom_response = requests.get(recom_url).json()

        # recom_response 목록을 돌며 영화 하나하나의 제목을 result 리스트에 append
        for recom_movie in recom_response['results']:
            result.append(recom_movie['title'])
        
        # 결과 출력
        return result
    
    # 만약 영화 서치했는데 영화가 없다면?
    else:
        return None  # None 값 리턴



    ### 영화 이름이 완전히 일치하는 코드.. 문제 잘못 읽어서 잘못짬
    # for movie in search_response['results']:
    #     if movie['title'] == title:
    #         result = []
    #         movie_id = movie['id']
    #         recom_url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=fe0cd3ae385a968eaa140d8955cf4804&language=ko-KR&page=1"
    #         recom_response = requests.get(recom_url).json()

    #         for recom_movie in recom_response['results']:
    #             result.append(recom_movie['title'])
            
    #         return result

    # else:
    #     return None


    
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
