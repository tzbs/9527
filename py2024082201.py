import requests
from bs4 import BeautifulSoup
import re
import csv

url = "https://movie.douban.com/subject/1292722/reviews?"

params = [['start','0']]
headers = {
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
		"accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
		"cookie": "ll=\"118379\"; bid=n6XSMjOsBv0; dbcl2=\"250324254:rTEyrbZ/sZE\"; ck=AVgn; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; frodotk_db=\"65184610fe6795d12f48d232fb36c173\"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1724310953%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%E6%B3%B0%E5%9D%A6%E5%B0%BC%E5%85%8B%E5%8F%B7%22%5D; _pk_id.100001.4cf6=d05a7fe2f9af226a.1724310953.; _pk_ses.100001.4cf6=1; __yadk_uid=LpQJnr9noWLBgeUm1atN2Va4T1mKWakY",
		"priority": "u=0, i",
		"referer": "https://movie.douban.com/subject/1292722/reviews?start=20",
		"sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "\"Windows\"",
		"sec-fetch-dest": "document",
		"sec-fetch-mode": "navigate",
		"sec-fetch-site": "same-origin",
		"sec-fetch-user": "?1",
		"upgrade-insecure-requests": "1",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
}
payload = {}
headers1 = {
		"accept": "application/json, text/javascript, */*; q=0.01",
		"accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
		"cookie": "ll=\"118379\"; bid=n6XSMjOsBv0; dbcl2=\"250324254:rTEyrbZ/sZE\"; ck=AVgn; push_noty_num=0; push_doumail_num=0; frodotk_db=\"65184610fe6795d12f48d232fb36c173\"; _pk_id.100001.4cf6=d05a7fe2f9af226a.1724310953.; __yadk_uid=LpQJnr9noWLBgeUm1atN2Va4T1mKWakY; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1724332265%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%E6%B3%B0%E5%9D%A6%E5%B0%BC%E5%85%8B%E5%8F%B7%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; RT=nu=&cl=1724334652946",
		"priority": "u=1, i",
		"referer": "https://movie.douban.com/subject/1292722/reviews?start=0",
		"sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "\"Windows\"",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
		"x-requested-with": "XMLHttpRequest",
}
person_info=[]
temp=[]
j=0
for i in range(0,21):
	if i%20==0:
		params[0][1]=str(i)
		content=requests.get(url,headers=headers,params=params).text
		soup=BeautifulSoup(content,'html.parser')
		for cup1 in soup.findAll('header',attrs={'class':'main-hd'}):
			cup2 = cup1.findAll('a', attrs={'class': 'name'})
			cup3 = cup1.findAll('span', attrs={'class': 'main-meta'})
			temp.append(cup2[0].get_text(strip=True))
			temp.append(cup3[0].get_text(strip=True))
			person_info.append(temp)
			temp=[]
		for cup1 in soup.findAll('div',attrs={'class':'main-bd'}):
			cup4 = cup1.findAll('div', attrs={'class': 'short-content'})
			cup5=cup4[0].find('a',title='展开')
			str1=cup5['id']
			number_key=re.findall(r'\d+', str1)
			key_number=int(number_key[0])
			url1=f'https://movie.douban.com/j/review/{key_number}/full'
			review = requests.request("GET", url1, headers=headers1, data=payload).json()
			soup1=BeautifulSoup(review['html'],'html.parser')
			text_content=soup1.get_text(strip=True)
			person_info[j].append(text_content)
			j+=1
# 指定文件名
filename = 'Titanic.csv'
# 使用'with'语句打开文件，确保文件正确关闭
with open(filename, mode='w', newline='', encoding='utf_8_sig') as file:
	# 创建一个csv.writer对象
	writer = csv.writer(file)
	# 遍历二维列表，并写入CSV文件
	for row in person_info:
		writer.writerow(row)
print(f'CSV文件已保存为：{filename}')








