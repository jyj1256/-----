# -*- coding: utf-8 -*-
import requests                 
from bs4 import BeautifulSoup   
import re                        
from konlpy.tag import Okt
import pandas as pd
import collections
from matplotlib import pyplot as plt
import seaborn as sns
###########################################
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize 
###########################################
okt = Okt()
resp222htmlstr = ""              
BlogText1 = ""                    
BlogText2 = ""                     
BlogText3 = ""                     
AllBlogText = ""                   
b = 1                             
p = re.compile('"http://blog[.]daum[.]net[a-zA-Z0-9\.\&\/\?\:@\-_=#]*" class="f_url"')    
keyward = input("검색할 키워드 입력->")
print('\n')
date1 = input('언제부터?-->')
print('\n')
date2 = input('언제까지?-->')
print('\n')
x = int(input("몆페이지 까지?--> "))
##############################################################################################################################################################
while b <= x:             
    url77 = 'https://search.daum.net/search?w=blog&f=section&SA=daumsec&lpp=10&nil_src=blog&q='+keyward+'&DA=PGD&period=u&sd='+date1+'000000&ed='+date2+'235959&p='+str(b)
    resp77 = requests.get(url77)
    resp77html =resp77.text
    resp77htmlstr = str(resp77html)
    array = p.findall(resp77htmlstr)            
    i = 0                              
    giri = len(array)  
    while i < giri:         
        url88 = array[i]     
        url99 = url88.replace('class="f_url"',"").strip()     
        url222 = url99.replace('"','').strip()     
        resp222 = requests.get(url222)                                
        soup222 = BeautifulSoup(resp222.text)
        BlogText1 = soup222.find_all('b')
        BlogText2 = soup222.find_all('p')
        BlogText3 = soup222.find_all('strong')
        for q1 in BlogText1:
            print(q1.get_text())
            AllBlogText = AllBlogText + q1.get_text()
        for q2 in BlogText2:
            print(q2.get_text())
            AllBlogText = AllBlogText + q2.get_text()
        for q3 in BlogText3:
            print(q3.get_text())
            AllBlogText = AllBlogText + q3.get_text()
        i = i + 1
    b = b + 1
################################################################################################################################################################ 

print( "lgdlskfjslkvjslvkjkls\n\n\n\n\njflsjflsjfljflsjflsjfls\njflsjflsjflsjflsjfls\n\n\n\n\n\njflsjflsjfl\nsjflsjflsjfslfjslfjlsjflds\n\n\n\n\nkfjslkdkfjslfjslvjnlsdnfhvloskhjfnslfjsldjflsjflsdjflsdjfls\n\n\n")
print( "lgdlskfjslkvjslvkjklsjflsjflsjfljflsjflsjflsjflsjflsjflsjflsjflsjflsjflsjflsjflsjflsjfslfjslfjlsjfldskfjslk\n\n\n\n\n\n\n\n\n\ndkfjslfjslvjnlsdnfhvloskhjfnslfjsldjflsjflsdjflsdjfls\n\n\n\n\n")
#########################################################################################################################################################################################################################
AllBlogText = AllBlogText.replace("아직 블로그를 개설하지 않으셨습니다.친구 신청을 하시려면 먼저 블로그를 개설해 주세요.지금 개설 하시겠습니까?친구가 되시면 친구의 새글 및 활동에 대한 알림을 받아보실 수 있습니다","").strip()
AllBlogText = AllBlogText.replace("친구신청을 하시겠습니까?친구 신청을 했습니다.상대가 수락하면 친구가 됩니다.친구 신청을 실패했습니다. 잠시 후 다시 시도해 주세요.친구 신청 가능 수를 초과했습니다.","").strip()
AllBlogText = AllBlogText.replace("친구신청","").strip()
AllBlogText = AllBlogText.replace("블로그 개설","").strip()
AllBlogText = re.sub(r"\d\d\d\d[.]\d\d[.]\d\d \d\d:\d\d","",AllBlogText)
AllBlogText = re.sub(r"[-=+#/\?:^@*\"※~ㆍ◆◇』‘|\(\)\[\]`\'…》\”\“\’·]","",AllBlogText)
###################################################################################################################################################################
#불용어 지정
k = 0
uselessword = ['그냥','사실','먼저','조금','진짜','지금','워낙','제공','역시','우리','사람','시간','강제','진자','것','물가','코로나','폭염','득템','구매','유행','축제','여름휴가','비트코인','백신','때문','정도','위해','경우','오늘','상황','가장','현재','세상','사회','생각','대한','교회','하나님','그','지역','아침','이상','사업','댓글','산행','예상','시작','사랑','구간','일리','계층','하나','비공개','정말','이','래서','마음','다시','바로','녀석','수','다른','요즘','친구','가지','아주','사용','설치','확인','광연','강조','하루','모습','오후','모두','국','야기','아들','곳','나무','박재홍','버스','여기','기도','의','타고','런데','한번','안철','대해','문제','처음','더','도착','준비','형님','보고','바람','가기','모든','주님','필요','통해','식사','저녁','사진','마을','숙소','호텔','바위']    #  불용어 리스트--> 불용어는 키워드마다 다르기때문에 키워드마다 바꿔줘야함
while k < len(uselessword):
    AllBlogText = AllBlogText.replace(str(uselessword[k]),"")
    k = k + 1
########################################################################################################################################################################
#print(AllBlogText)
#pstaglist = okt.pos(AllBlogText)          #품사 분석
pstaglist = okt.nouns(AllBlogText)       # 명사 추출배
#pstaglist = okt.morphs(AllBlogText)      # 형태소 분석
#print(type(pstaglist))  --> 결과 class : list
#print(type(pstaglist[45]))   --> 결과 class : str

##############################################################################################################################################
u = 0
while u < len(pstaglist):
    if len(pstaglist[u]) == 1:
        pstaglist.remove(pstaglist[u])
    u = u+1
##############################################################################################################################################
#print(pstaglist)
counts = collections.Counter(pstaglist)
#print(counts)   # 결과 : Collections.Counter


frequencydata = counts.most_common(15)
print(type(frequencydata))
df = pd.DataFrame(frequencydata)
df = df.rename(columns={0 : 'keyward', 1 : 'frequency'})
print(df)
plt.rcParams['font.family'] = 'AppleGothic'
visualizationdata = sns.barplot(data=df, x="keyward", y="frequency")
visualizationdata.set_title(keyward)
sns.set(font_scale=0.1)
print(visualizationdata)
plt.savefig('graph.png')