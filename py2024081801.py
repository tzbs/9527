import requests
content=requests.get('https://mp.weixin.qq.com/cgi-bin/appmsgpublish?sub=list&begin=0&count=10&token=364105463&lang=zh_CN').text
with open('wxgzpt.html','w',encoding='utf-8') as f:
    f.write(content)
#print(content)