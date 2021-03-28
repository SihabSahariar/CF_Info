from bs4 import BeautifulSoup as bs
import requests 
try:
    userName = input('Enter codeforces username: ')
    url = f'http://codeforces.com/profile/{userName}' 
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    info = soup.find_all('span', style="font-weight:bold;")
    Data = {}
    Data['Current position '] = info[1].string[0:-2]
    Data['Contest rating'] = info[0].string
    Data['Max rating '] = info[2].string
    print('================Codeforces Profile Information================')
    print(f'Username: {userName}')
    for i, j in Data.items():
        print(i,':',j)
except:
    print('Something went wrong!\nTry again.')
