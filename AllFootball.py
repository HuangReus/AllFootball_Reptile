import requests
import re

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.3','Host':'www.dongqiudi.com','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.8','Cache-Control':'max-age=0','Connection':'keep-alive'}
html = requests.get('http://www.dongqiudi.com',headers=headers)
html.encoding='utf-8'

#print(html.text)

file=open('log.txt','w')

news=re.findall('target="_blank" class="pc_count">(.*?)</a>',html.text)

file.writelines(news)

#for each in news:
#    print(each)

file.close()

