import requests
from bs4 import BeautifulSoup
import re

def filter(s):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    
    result = hangul.sub('',s)
    return result

url_page = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=199393&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false"

page=0
list_text=[]
while page<10 :
    page+=1
    if page > 1:
        url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=199393&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false"
        url_page = url + "&page=" + str(page)
    else: pass
    
    res = requests.get(url_page)
    soup = BeautifulSoup(res.text, "lxml")
    div = soup.find_all(class_="score_reple")

    count = 0
    list=[]
    for i in div:
        span_id = "_filtered_ment_" + str(count)
        list.append(i.p.find(id=span_id))
        count+=1
        
    for j in list :
        list_text.append(filter(j.text))

print(list_text)