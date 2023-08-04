from unicodedata import name
import requests
from bs4 import BeautifulSoup 

#---------------------------------------------------------------------------------------------------------------------#
def altseason():
    url1 = 'https://www.blockchaincenter.net/altcoin-season-index/'
    response = requests.get(url1)
    soup = BeautifulSoup(response.text, 'lxml')
    Altseason = soup.find('div', style='margin-top:-74px').find('div').text
    
    return Altseason
#---------------------------------------------------------------------------------------------------------------------#    
def dominance():
    url = 'https://coinmarketcap.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    item = soup.find('div', class_='cmc-global-stats__inner-content').find(href="/charts/#dominance-percentage").text
    return item
#---------------------------------------------------------------------------------------------------------------------#     
def feargreed():
    url = 'https://bitstat.top/fear_greed.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    item = soup.find('div', class_='glbl-stat grey_font small-font10 upper').find(href='https://bitstat.top/fear_greed.php').text
    return(item)
#---------------------------------------------------------------------------------------------------------------------# 
def cap():
    url = 'https://coinmarketcap.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    item = soup.find('div', class_='cmc-global-stats__inner-content').find(href = '/charts/').text
    return(item)
#---------------------------------------------------------------------------------------------------------------------# 