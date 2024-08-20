import json

import requests
import re
import html
import pandas as pd
from bs4 import BeautifulSoup

url = "https://mp.weixin.qq.com/cgi-bin/appmsgpublish?sub=list&begin=0&count=10&token=364105463&lang=zh_CN"
payload = {}
headers = {
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
		"accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
		"cookie": "appmsglist_action_3943274291=card; ua_id=VuIAcdOtBqHnndxyAAAAAPRm13eyIz8IlH4r9QDewpk=; wxuin=21035274672260; mm_lang=zh_CN; personAgree_3943274291=true; poc_sid=HD44mmajmz9IpVJ-uYp95xpFeE-nxndiHFRsykMT; eas_sid=m1B7h2l105H566S4G8A6W0x3o7; pgv_pvid=1641041718; ts_uid=7159249510; pgv_pvi=8892408832; __root_domain_v=.weixin.qq.com; _qddaz=QD.854921634790799; qq_domain_video_guid_verify=91e73a0d41df614c; _qimei_uuid42=18716111f2b100f33d7d0a7d7bb374e937516615c1; _qimei_fingerprint=1568d6407fe894a1b033d02c920f1a3e; _qimei_q36=; _qimei_h38=e1476bec3d7d0a7d7bb374e902000006d18716; _clck=3943274291|1|fof|0; uuid=4f68e142ad3d7cf6a8ca346f0ff45ccc; rand_info=CAESIOdWH84utat+5soDlO2tocnfCPB7zIrvb1pWQ36fmrJQ; slave_bizuin=3943274291; data_bizuin=3943274291; bizuin=3943274291; data_ticket=YAJAWCDnOxRWPU6KCFsE+m+JyvRbBi9/sfYgFoYhC9O8+Gf4SgykWTRRcyCZnFCV; slave_sid=T1ZVczU3SlNuYWh0TWZKZ25RdERYYjFLQ21OMGdIRnJNeEZVM0dPX18wbkdKR2s1QjVGdjluMEFKRXkybk95RlRmdVR2dnN0TXVYVnhtTm5WYXBpRXBLQTBVVm51cnVRNEFLRzkxeUM0T1VEeG1tS2JWaHp2cG1VMDdydGFzdFJLU3dxd1ZxeGYySGRYdGc2; slave_user=gh_2ddf0452d62c; xid=82bddad41ba26bb9303639b5ee8af30d; mm_lang=zh_CN; rewardsn=; wxtokenkey=777; _clsk=zrwu6w|1723969728819|2|1|mp.weixin.qq.com/weheat-agent/payload/record",
		"priority": "u=0, i",
		"referer": "https://mp.weixin.qq.com/cgi-bin/appmsgpublish?sub=list&begin=10&count=10&token=364105463&lang=zh_CN",
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

content = requests.request("GET", url, headers=headers, data=payload).text
list1=re.findall('"publish_info":"(.*?)"',content)
#list2=html.unescape(str(list1))
list3={}
artcle_info=[]
for list2 in list1:
	list3=html.unescape(str(list2))
	print(list3)
	data = json.loads(list3)

	# 提取appmsg_info
	appmsg_info = data['appmsg_info']
	first_appmsg_info = appmsg_info[0]
	items=[]
	items.append(first_appmsg_info['title'])
	items.append(first_appmsg_info['read_num'])
	items.append(first_appmsg_info['like_num'])
	items.append(first_appmsg_info['comment_num'])
	artcle_info.append(items)
name=['title','read_num','like_num','comment_num']
result=pd.DataFrame(columns=name,data=artcle_info)
result.to_csv('wxgzpt.csv',index=False,encoding='UTF-8')

	# 现在你可以访问first_appmsg_info中的任何字段了
	#print(first_appmsg_info['title'],end='\t')  # 输出文章标题
	#print(first_appmsg_info['read_num'],end='\n')

	# 现在appmsg_info包含了appmsg_info列表中的所有元素
	#print(appmsg_info)
	#appmsg_info=list3['type']
	#print(list3[5])
	#print(list3)
	#print(appmsg_info)
#print
	#title=re.findall('"appmsg_info"',list3)
#title=re.findall('"appmsg_info":[{"(.*?)"}]',list2)
#print(title)

#print(title)
#print(list2)
#titles=[]
#print(list1)

	#try:
		#list3=json.loads(list2)
		#title=list3.get('title')
		#if title:
			#titles.append(title)
	#except json.JSONDecodeError:
		#print(f'无法解析的JSON字符串:{list2}')

#print(titles)
	#list3=re.findall(',&quot;title&quot;:&quot;"(.*?)"&quot;,',str(list2))
	#print(list3)
#list2=re.findall(',&quot;title&quot;:&quot;"(.*?)"&quot;,',str(list1))
#print(list2)


#soup=BeautifulSoup(content,'html.parser')
#cup1=soup.find_all('script',{'type':'text/javascript'})
#for cup2 in cup1:
	#print(cup2.find_all('title'))

#cup2=cup1.find('div',{'class':'weui-desktop-block'})
#print(cup2)
#with open('wxgzpt1.html','w',encoding='utf-8') as f:

#    f.write(content)

#<div class="weui-desktop-mass-appmsg__bd"><div><div><a href="https://mp.weixin.qq.com/s?__biz=Mzk0MzI3NDI5MQ==&amp;mid=2247484558&amp;idx=1&amp;sn=ff66c226aa3d23e8345f6daf7f9646be&amp;chksm=c33724d2f440adc4ab705f38c3e38c2b20cca8962d057a91ce40e76ca55bed22a99b34951d32#rd" target="_blank" class="weui-desktop-mass-appmsg__title" style="overflow: visible;"><span>机器学习之Logistic&nbsp;Regression</span> <b class="weui-desktop-key-tag">原创</b> <!----> <!----> <!----> <!----></a></div> <!----> <!----> <!----> <!----> <div class="weui-desktop-mass-media__data-list"><div class="weui-desktop-tooltip__wrp"><div class="weui-desktop-mass-media__data appmsg-view"><span class="weui-desktop-mass-media__data__inner">10</span></div> <span class="weui-desktop-tooltip weui-desktop-tooltip__down-center" style="display: none;">阅读数</span></div> <div class="weui-desktop-tooltip__wrp"><div class="weui-desktop-mass-media__data appmsg-like"><span class="weui-desktop-mass-media__data__inner">2</span></div> <span class="weui-desktop-tooltip weui-desktop-tooltip__down-center" style="display: none;"><span>点赞数</span></span></div> <div class="weui-desktop-tooltip__wrp"><div class="weui-desktop-mass-media__data appmsg-haokan"><span class="weui-desktop-mass-media__data__inner">0</span></div> <span class="weui-desktop-tooltip weui-desktop-tooltip__down-center" style="display: none;">在看数</span></div> <div class="weui-desktop-tooltip__wrp"><a href="file:///D:/misc/appmsgcomment?action=list_latest_comment&amp;begin=0&amp;count=10&amp;mp_version=7&amp;sendtype=MASSSEND&amp;comment_id=3589869002949820422&amp;token=364105463&amp;lang=zh_CN" target="_blank" class="weui-desktop-icon__response-mouse weui-desktop-mass-media__data appmsg-comment"><span class="js_comment_info weui-desktop-mass-media__data__inner"><span class="weui-desktop-link">1</span></span></a> <span class="weui-desktop-tooltip weui-desktop-tooltip__down-center" style="display: none;">留言数</span></div> <div class="weui-desktop-tooltip__wrp"><a href="/cgi-bin/appmsgcopyright?action=reprint&amp;begin=0&amp;count=10&amp;id=2247484558&amp;idx=1&amp;need_quote=1" target="_blank" class="weui-desktop-icon__response-mouse weui-desktop-mass-media__data appmsg-forward"><span class="weui-desktop-mass-media__data__inner"><span class="weui-desktop-link">0</span></span></a> <span class="weui-desktop-tooltip weui-desktop-tooltip__down-center" style="display: none;">被转载/引用/分享</span></div> <!----> <!----> <div class="weui-desktop-tooltip__wrp"> <span class="weui-desktop-tooltip weui-desktop-tooltip__down-center" style="display: none;">投票</span></div> <div class="weui-desktop-tooltip__wrp"><div class="weui-desktop-mass-media__data appmsg-underline__disable"><span class="weui-desktop-mass-media__data__inner">0</span></div> <span class="weui-desktop-tooltip weui-desktop-tooltip__down-center" style="display: none;">划线人数</span></div></div></div></div>