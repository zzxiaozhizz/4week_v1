from bs4 import BeautifulSoup

target_file_location = 'C:\\Users\\zhigang.zhang\\PycharmProjects\\test\\课程源码及作业参考答案\\Plan-for-combating-master\\week1\\1_2\\1_2answer_of_homework\\1_2_homework_required\\index.html'

with open(target_file_location, 'r') as web:
    Soup = BeautifulSoup(web, 'lxml')

    imgs = Soup.select('body > div > div > div > div > div > div > img')
    prices = Soup.select('body > div > div > div > div > div > div > div.caption > h4.pull-right')
    titles = Soup.select('body > div > div > div > div > div > div > div.caption > h4 > a')
    reviews =    Soup.select('body > div > div > div > div > div > div > div.ratings > p.pull-right')
    rates_full = Soup.select('body > div > div > div > div > div > div > div.ratings > p:nth-of-type(2)')
    # print(rates_full)

# for i in rates_full:
#     print(i)



info = []#
for img, price, title, review, rate_full in zip(imgs, prices, titles, reviews, rates_full):
    product = {
        'img': img.get('src'),
        'price': price.get_text(),
        'title': title.get_text(),
        'review': review.get_text(),
        'rate_full':len(rate_full.find_all('span',class_= 'glyphicon glyphicon-star')),
    }
    info.append(product)

print(*info, sep='\n')

'''
body > div > div > div.col-md-9 > div > div > div > div.ratings > p > span.glyphicon.glyphicon-star-empty
body > div > div > div.col-md-9 > div > div > div > div.ratings > p > span:nth-child(3)
body > div > div > div.col-md-9 > div > div > div > div.ratings > p > span:nth-child(5)
body > div> div > div.col-md-9 > div> div> div > div.ratings > p
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p:nth-child(2)   
'''


