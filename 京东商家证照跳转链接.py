# -*- encoding: utf-8 -*-
"""
@Author  : cy1
@File    : 京东商家证照跳转链接.py
@Time    : 2023/6/28 21:38 
@Software: PyCharm
"""
import requests


headers = {
    "authority": "badjs.m.jd.com",
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://diansong.jkcsjd.com/",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
}
cookies = {
    "shshshfpb": "aC-OH-0mvjlr65NqM6edmWQ",
    "TrackID": "1MGdmXENSI0C4DaROq7XrqNrZO_M2J3Ah4JaTryjRQ7v1Q-7Wfue-rCMZZ78gF-woAt04Le62o4FtzhJhFQsZoy0zCJEpEdqZlJ6i0QNsV5I",
    "thor": "00AEF2CE68665E4707CB4A99A25ED030011D41070E71C558631E1CCB1C3DB6381C596F4971C13366A18283F5C0D0D1CCEE8962DD720EAEB6A2D336F318F9B77718713CAE3E528ABB846723E3B85800131ABCD69BCDC0B8A7565610C1B8EAC40DABC4235AF40A377BED56B8EFAE07C008A7EB0B1EEBEFCFF78B74A44A8C224C7C",
    "flash": "2_KPmjmDz7Yd1pg23X3kNYx6m-U08ls_IcuHP_5C6ZdcnLlhtDXXnJxmzLsR3krZnpIXw107DXGxscEGrAfhizlB-4VUw-nr5MUspWPEPtCaK*",
    "pinId": "vzAdi7yQqZdvlpsNiYg67A",
    "pin": "%E7%BE%BD%E6%9C%AB2016",
    "unick": "%E7%BE%BD%E6%9C%AB2016",
    "ceshi3.com": "000",
    "_tp": "OuOlH9cuHD9gFTUOlLwQ0flOhtNIIpRilc%2BZTFZLFtU%3D",
    "_pst": "%E7%BE%BD%E6%9C%AB2016"
}
url = "https://badjs.m.jd.com/report"
params = {
    "id": "912",
    "msg\\[0\\]": "setPicTitlehide",
    "from\\[0\\]": "https://diansong.jkcsjd.com/store/1006970573?venderid=12990930",
    "key\\[0\\]": "dsyf.m.jd.com;diansong.jkcsjd.com_1647512031",
    "domain\\[0\\]": "dsyf.m.jd.com;diansong.jkcsjd.com",
    "level\\[0\\]": "2",
    "count": "1",
    "_t": "Wed Jun 28 2023 21:16:15 GMT 0800 (中国标准时间)"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)