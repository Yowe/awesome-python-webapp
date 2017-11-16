#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import os
from DownLoad import request
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class mzitu():
    def load_all_url(self, url):
        html = request.get(url, 3)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print "开始保存:",title
            path = str(title).strip().decode('utf-8')
            self.mkdir(path)
            href = a['href']
            self.html(href)  #套图的地址

    def html(self, href):
        html = request.get(href, 3)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span)+1):
            page_url = href + '/' + str(page)
            self.img(page_url)

    def img(self, page_url):
        img_html = request.get(page_url, 3)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save_file(img_url)

    #保存图片
    def save_file(self, img_url):
        name = img_url[-9:-4]
        img = request.get(img_url, 3)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()


    #创建文件夹
    def mkdir(self, path):
        dirPath = os.path.join("D:\mzitu", path)
        isExists = os.path.exists(dirPath)
        if not isExists:
            os.mkdir(dirPath)
            os.chdir(dirPath)
            return True
        else:
            return False





mzspider = mzitu()
mzspider.load_all_url('http://www.mzitu.com/all')