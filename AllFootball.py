import requests
from lxml import etree
import os
import re
import time

headers = {

        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.3',
        'Host':'www.dongqiudi.com',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1'

           }

def main():

    while True:

        html = requests.get('http://www.dongqiudi.com',headers=headers)

        html.encoding='utf-8'

#print(html.text)

        selector=etree.HTML(html.text)
#file=open('log.txt','w+')

#news=re.findall('target="_blank" class="pc_count">(.*?)</a>',html.text)

#for each in news:
#    file.write(each+'\n')

        now=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        os.mkdir(now,0o777)

        football_news=selector.xpath('//div[@id="news_list"]/ol/li/h2/a/@href ')

        news_title=selector.xpath('//div[@id="news_list"]/ol/li/h2/a/text()')

#print(news_title)
#print(football_news)

        BASE_DIR=os.path.dirname(__file__)
#print(BASE_DIR)

        file_path=os.path.join(BASE_DIR,now)
#print(file_path)


        for i in range(0,len(news_title)):
            new_file=open(file_path+'/'+news_title[i]+'.txt','w')

            news_html=requests.get(url=football_news[i],headers=headers)
            news_html.encoding='utf-8'

            selector=etree.HTML(news_html.text)
            news_content=selector.xpath('//div[@id="main"]/div[@id="con"]/div/div/div/p/text()')
            print(type(news_content))

            new_file.writelines(news_content.encode('utf-8'))
            new_file.close()

        time.sleep(3600)
#file.close()


if __name__=="__main__":
    main()
