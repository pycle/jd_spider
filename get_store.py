# -*- encoding: utf-8 -*-
"""
@Author  : cy1
@File    : get_store.py
@Time    : 2023/6/28 20:16 
@Software: PyCharm
"""
import execjs
import requests


headers = {
    "authority": "color.jkcsjd.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "origin": "https://diansong.jkcsjd.com",
    "referer": "https://diansong.jkcsjd.com/",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
}
# cookies = {
#     "burriedExpLabel": "tsabtest|base64|ZGlhbnNvbmdfMTQ0NzZ8YmFzZQ|tsabtest",
#     "runType": "0",
#     "jkcsjdv": "168795028412288971",
#     "serveType": "Agroup",
#     "shshshfpa": "76fcf0a3-ff01-4918-8139-996a13460e5a-1687950282",
#     "shshshfpx": "76fcf0a3-ff01-4918-8139-996a13460e5a-1687950282",
#     "source": "fujin_yjs_icon",
#     "3AB9D23F7A4B3C9B": "MSVUODKZ52JYZHTAIKFVP532TCX3ZAP5WHUOWRNVPFFBGTYKXW4L3CAZQRRVIINQKPMOML4MGJTGXZDL6HFP5ADDEM",
#     "__jda": "74320393.16879502830088458425.1687950283.1687950283.1687950283.1",
#     "__jdv": "74320393%7Cdirect%7C-%7Cnone%7C-%7C1687950283008",
#     "__jdc": "74320393",
#     "mba_muid": "16879502830088458425",
#     "shshshfpb": "aC-OH-0mvjlr65NqM6edmWQ",
#     "pt_key": "AAJknCE5ADC7933riOtBm_PVD6KhtdsCdulh7RxPKvcz5_3yrvpaarzs2V82EwyVMmCly5JRYsM",
#     "pt_pin": "%E7%BE%BD%E6%9C%AB2016",
#     "pt_token": "ziwwf8i5",
#     "pwdt_id": "%E7%BE%BD%E6%9C%AB2016",
#     "sfstoken": "tk01maf9e1c24a8sM3gyN0w2Sjd1BOj5fxThvhbJv78M2h5qJnWsLZrP9+W2zbaDuwp41FqVBnOws7u2eIcdQFRg0LRK",
#     "shshshsID": "4ab8e6a2d8bce8584ee8dbb6154d6818_6_1687953720811",
#     "3AB9D23F7A4B3CSS": "jdd03MSVUODKZ52JYZHTAIKFVP532TCX3ZAP5WHUOWRNVPFFBGTYKXW4L3CAZQRRVIINQKPMOML4MGJTGXZDL6HFP5ADDEMAAAAMJAHQ44LAAAAAADFKMNJYTGX6PL4X",
#     "__jdb": "74320393.6.16879502830088458425|1.1687950283",
#     "mba_sid": "16879502830096424950457509520.10",
#     "__jd_ref_cls": "MMedicineShop_PublicInquiryExpo"
# }
url = "https://color.jkcsjd.com/api/ds_getDistributableStore"

with open('get_h5st.js','r',encoding='utf-8')as f:
    js_code=f.read()
ctx = execjs.compile(js_code).call("jd_get_h5st","{\"longitude\":120.209618,\"latitude\":30.34082,\"storeMaxSize\":30,\"skuPoolType\":1,\"agingType\":1}")
data = {
    "functionId": "ds_getDistributableStore",
    "body": "{\"longitude\":120.209618,\"latitude\":30.34082,\"storeMaxSize\":50,\"skuPoolType\":1,\"agingType\":1}",
    "appid": "dian_song",
    "t": "1687953963343", # int(time.time()*1000)
    "h5st":ctx,
    # "h5st": "20230628200603348;9839659553910274;f7dfe;tk03wc10e1c6818nMgPMtYuFvz8xxMdT8KihPRdP2QXTiHznm6-6EXQyZlULfiPV5L7PfQBHJXHs1rL1swnTvjEi23zG;716b9b522d5306f8ebf86265c89afbc5ced777e13bab1ae46ac30958c734da64;3.1;1687953963348;62f4d401ae05799f14989d31956d3c5ff69bf9d5a722facd4df405c9452a670e06cef39a50ad1e9b78fa7ec6af1b14462c66909b783cc0ffb13050ced02e4907ce98100c47c9aa97794a353958cb4258c9ba85a9b411b2ebc6249d2f4a6340ab4b415d6a036ef09ee8a14e42dc25b0a056f1b628c4eb1d594c54900a4b48c3eb",
    "x-api-eid-token": "jdd03MSVUODKZ52JYZHTAIKFVP532TCX3ZAP5WHUOWRNVPFFBGTYKXW4L3CAZQRRVIINQKPMOML4MGJTGXZDL6HFP5ADDEMAAAAMJAHQ44LAAAAAADFKMNJYTGX6PL4X"
}
response = requests.post(url, headers=headers, data=data)

# print(response.text)
# print(response)

data_list=response.json()
response.close()
data_info={}
for i in data_list['data']:
    data_info['name']=i['storeName']
    data_info['url']=i['shopPageUrlM']
    data_info['address']=i["address"]
    # print(i['storeName'],i['venderId'],i['storeId'],i["shopPageUrlM"],i["phone"],i["address"],i['latitude'],i['longitude'])