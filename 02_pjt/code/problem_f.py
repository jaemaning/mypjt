import os
import sys
import urllib.request
import json
import webbrowser
import time
from datetime import date

def naver_movie(title):

    # naver 이용시 client_id 와 client_secret 값이 필요 , 발급 후 url request header 에 추가.
    # title 파라미터를 받고 urllib.parse.quote에 넣어 encText 생성 후 url 쿼리 값에 넣어줌.
    client_id = "8cfEkyaU2wzcDan5rIQi"
    client_secret = "ljBslaxTqo"
    encText = urllib.parse.quote(title)
    url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # JSON 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode==200):
        # 받아온 정보를 json으로 변환하는 과정
        response_body = response.read()
        encoding = response.info().get_content_charset('utf8')  # JSON default
        data = json.loads(response_body.decode(encoding))
        naver_moive_link_list = []

        for movie in data['items']:
            # 영화 목록을 for 문 돌며 이름에 받아온 parameter 값이 들어있는 것을 찾아 리스트에 저장
            if title in movie['title'] :
                naver_movie_url = movie['link']
                naver_moive_link_list.append(naver_movie_url)
                # webbrowser default 값은 chrome으로 열리고, 2초 후 다음 영화 오픈.
                webbrowser.open_new_tab(naver_movie_url) 
                time.sleep(2)

    # 에러시 처리 코드
    else:
        print("Error Code:" + rescode)

    return naver_moive_link_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    '''
    영화 제목을 입력하면, 해당 영화의 네이버 영화 상세페이지 링크가 나오며
    이후 바로 크롬으로 웹페이지를 열어 보는 코드 작성.
    
    영화 링크 주소 list 를 만들어서 return 도 해줌.
    '''

    print(naver_movie('해리'))
    # ['https://movie.naver.com/movie/bi/mi/basic.nhn?code=218946', 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=222299', 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=223676', 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=203098', 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=193568', 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=205194', 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=199111', 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=172796', 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=192771', 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=180098']
    print(naver_movie('검색할 수 없는 영화'))
    # []
    print(naver_movie('살인의 추억'))
    # ['https://movie.naver.com/movie/bi/mi/basic.nhn?code=149038', 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=35901']
