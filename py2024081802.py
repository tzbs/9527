import requests
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
with open('wxgzpt1.html','w',encoding='utf-8') as f:
    f.write(content)
