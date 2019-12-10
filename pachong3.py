from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# 地址是以p后面的数字为页码，同时发现最大是13页，因此用一个循环将所有地址放到list里面
urls = ['http://dl.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,14)]

# 测试代码
# url = 'http://dl.xiaozhu.com/search-duanzufang-p1-0/'
# url = 'http://dl.xiaozhu.com/fangzi/112174266701.html'

# 定义方法，通过循环主页面地址，找到每个房型的地址并返回
def getSubLink(url):
    detail_url = []
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    sublinks = soup.select('#page_list > ul > li > a')
    for i in sublinks:
        # print(i.get('href'))
        detail_url.append(i.get('href'))
    # print(detail_url)
    return detail_url

# print(getSubLink(url))

def get_Attr(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    # print(soup)
    title = soup.select('div.pho_info>h4>em')[0].get_text()
    address = soup.select('div.pho_info > p')[0].get('title')
    price_dayl = soup.select('div.day_l > span')[0].get_text()
    img_address = soup.select('#curBigImage')[0].get('src')
    owner_pic_address = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')[0].get('src')
    owner_gender_temp = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic>div')[0].get('class')
    if len(owner_gender_temp) == 0:
        owner_gender = 'NA'
    else:
        if owner_gender_temp[0] == 'member_ico1':
            owner_gender = 'Female'
        else:
            owner_gender = 'Male'
    # print(owner_gender)

    owner_name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')[0].get_text()
    # time.sleep(1)
    room_details = {
        'url':url,
        'title' :  title,
        'address' :  address,
        'price_dayl' :  price_dayl,
        'img_address' :  img_address,
        'owner_pic_address' :  owner_pic_address,
        'owner_gender' :  owner_gender,
        'owner_name' :  owner_name
    }
    # print(room_details)
    return room_details
# get_Attr(url)
# print(get_Attr(url))



room_info = []
for url in urls:
    sub_url_list = getSubLink(url)
    for sub_url in sub_url_list:
        # print(sub_url)
        room_info.append(get_Attr(sub_url))
        print(sub_url+'---done')
    print(url+'------DONE')


# 通过Pandas的data frame方法，把整个room信息以及对应列名弄成一个df对象
df = pd.DataFrame(room_info,
                  columns=['url', 'title', 'address', 'price_dayl', 'img_address', 'owner_pic_address', 'owner_gender', 'owner_name']
                  )
# 通过to_csv方法生成csv文件
df.to_csv('./short_rent.csv', index=True, encoding='utf-8')

