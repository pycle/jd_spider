# -*- encoding: utf-8 -*-
"""
@Author  : cy1
@File    : get_verify.py
@Time    : 2023/6/28 21:36 
@Software: PyCharm
"""
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
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "x-referer-page": "https://diansong.jkcsjd.com/store/1006970573",
    "x-rp-client": "h5_1.0.0"
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
#     "flash": "2_YLgCyPZaQ9aDRAPNd5eozj_Pcs_niCqXojSkL8lhWpEs64C9N0mJwwTLznOANDiYZtt-WVplzTMTzYEW7KgcDAzitzF1Ii-mjYEPti7J0EL*",
#     "thor": "00AEF2CE68665E4707CB4A99A25ED03005B0DB5E07C281631FCC382DC4B569804E64F330C4F200E384C3020B179B47BF2D4AADA830836D769AC136CB0A7222DF4E5D1A50DC608A3ED1EA26F17677B77C50F9FAF0B77E129FE8887C6B0D63E337C23180BE8A9AC8FA4CA6F68BA9DE2C72B5D6CEB57D7391301FB65EA78C49135F",
#     "pin": "%E7%BE%BD%E6%9C%AB2016",
#     "unick": "%E7%BE%BD%E6%9C%AB2016",
#     "3AB9D23F7A4B3CSS": "jdd03MSVUODKZ52JYZHTAIKFVP532TCX3ZAP5WHUOWRNVPFFBGTYKXW4L3CAZQRRVIINQKPMOML4MGJTGXZDL6HFP5ADDEMAAAAMJAH4UXRQAAAAAC2H43LVZBZUXCUX",
#     "mba_sid": "16879502830096424950457509520.16",
#     "__jd_ref_cls": "MMedicineHome_ShopHomeQualification"
# }
url = "https://color.jkcsjd.com/api/ds_getExtendInfo"
data = {
    "functionId": "ds_getExtendInfo",
    "body": "{\"storeId\":\"1006970573\"}",
    "appid": "dian_song",
    "t": "1687958174543",
    "x-api-eid-token": "jdd03MSVUODKZ52JYZHTAIKFVP532TCX3ZAP5WHUOWRNVPFFBGTYKXW4L3CAZQRRVIINQKPMOML4MGJTGXZDL6HFP5ADDEMAAAAMJAH4UXRQAAAAAC2H43LVZBZUXCUX"
}
response = requests.post(url, headers=headers,  data=data)

# print(response.text)
res=response.json()
response.close()
img_list=[i['imgUrl'] for i in res['data']['qualification']]
# print(response  )