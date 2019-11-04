import requests
import urllib
from time import sleep
from bs4 import BeautifulSoup
user_agent = {'User-agent': 'Mozilla/5.0'}
mgal = input('검색하실 갤러리가 마이너갤러리인가요? 그렇다면 ㅇ을 입력해주시고 아니라면 아무 키나 입력해주세요: ')
if mgal == 'ㅇ':
    mgal = 'mgallery/'
else:
    mgal = ''
gall = input('검색하실 갤러리의 id를 입력하세요. 해당 갤러리 url에 있습니다: ')
#갤러리 id 목록 만들 수 있는데 귀찮음 ㅈㅅ
enter = input('검색어를 입력하세요: ')
print('검색은 최신글(큰 번호)부터 시작해 옛날글(작은 번호)로 역순으로 시행됩니다.')
print('검색되어 나오는 글 번호에는 디시인사이드 링크 생성 방식에 따른 오차가 있습니다. 아주 낮은 글 번호에서는 불규칙적이나 수가 높아지면 대략 100~200개 정도로 좁혀집니다.')
start = int(input('검색을 시작할 글 번호를 입력하세요: '))-5000
finish = int(input('검색을 마칠 글 번호를 입력하세요: '))-5000
#입력한 숫자에서 ±5000 내외로 검색하는 시스템이더라고요. 상술했듯 오차가 들쑥날쑥이고.
for i in range(start, finish, -10000):
    for page in range(1, 511):
        url = 'https://gall.dcinside.com/'+mgal+'board/lists/?id='+gall+'&page='+str(page)+'&search_pos=-'+str(i)+'&s_type=search_all&s_keyword='+enter
        rp = requests.get(url,headers=user_agent)
        soup = BeautifulSoup(rp.text,'lxml')
        check = soup.find(property="og:url").get('content')
        wow = soup.find_all(class_="ub-content us-post")
        if not wow:
            break
        if not 'page='+str(page) in check:
            break
        for j in wow:
            no = j.find('td', class_="gall_num")
            title = j.find('a')
            print('https://gall.dcinside.com/'+mgal+'board/view/?id='+gall+'&no='+no.get_text())
            print(title.get_text())
        sleep(1)
        #너무 빨리 검색하면 접속 차단당해서 1초에 1 검색 페이지


