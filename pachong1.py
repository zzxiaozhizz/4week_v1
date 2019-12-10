from bs4 import BeautifulSoup
web_path = 'C://Users//zhigang.zhang//PycharmProjects//test//课程源码及作业参考答案//Plan-for-combating-master//week1//1_2//1_2code_of_video//web//new_index.html'

with open(web_path, 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    # print(Soup)
    imgs = Soup.select('body > div.main-content > ul > li > img')
    descs = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates = Soup.select('body > div.main-content > ul > li > div.rate > span')
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    # 这么写标签会被打散，没有1对多的结构
    # cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info > span')
    # 直接在上一层就停住取值,可以取到结构信息
    cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')

    # print(*imgs, sep='\n')
    # print(*descs, sep='\n')
    # print(*rates, sep='\n')
    # print(*titles, sep='\n')
    # print(*cates, sep='\n')

# for title in titles:
#     print(title)
#     print(title.get_text())
info = []
for img, desc, rate, title, cate in zip(imgs, descs, rates, titles, cates):
    raw_data = {
        'img': img.get('scr'),# Img信息在scr里面，取元素的属性，直接用get方法，传入属性名
        'desc': desc.get_text(),
        'rate': rate.get_text(),
        'title': title.get_text(),
        'cate': list(cate.stripped_strings)
    }
    info.append(raw_data)
for i in info:
    if float(i['rate'])>3:
        print(i['title'], i['rate'])


'''
body > div.main-content > ul > li:nth-child(1) > div.rate > span
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(2)
body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a
body > div.main-content > ul > li:nth-child(1) > img

'''