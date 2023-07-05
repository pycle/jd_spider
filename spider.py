# -*- encoding: utf-8 -*-
"""
@Author  : cy1
@File    : spider.py
@Time    : 2023/7/3 9:56 
@Software: PyCharm
"""
import hashlib
import time
import execjs
import requests



class jd_spider:

    def __init__(self,lon,lat):
        # 隧道域名:端口号
        tunnel = "m730.kdltps.com:15818"
        # 用户名密码方式
        username = "t18784792562347"
        password = "utd6r5ss"
        self.get_store_url = "https://color.jkcsjd.com/api/ds_getDistributableStore"
        self.get_verify_url = "https://color.jkcsjd.com/api/ds_getExtendInfo"
        self.latitude=str(lat)
        self.longitude=str(lon)
        self.headers = {
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
        self.data_list=[]
        self.proxy={
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username,
                                                            "pwd": password,
                                                            "proxy": tunnel},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username,
                                                             "pwd": password,
                                                             "proxy": tunnel}
        }

    def get_store(self):
        data_body = "{\"longitude\":" + self.longitude + ",\"latitude\":" + self.latitude + ",\"storeMaxSize\":50,\"skuPoolType\":1,\"agingType\":1}"
        with open('get_h5st.js', 'r', encoding='utf-8') as f:
            js_code = f.read()
        ctx = execjs.compile(js_code).call("jd_get_h5st", data_body)
        data = {
            "functionId": "ds_getDistributableStore",
            "body": data_body,
            "appid": "dian_song",
            "t": int(time.time() * 1000),
            "h5st": ctx,
            # "h5st": "20230628200603348;9839659553910274;f7dfe;tk03wc10e1c6818nMgPMtYuFvz8xxMdT8KihPRdP2QXTiHznm6-6EXQyZlULfiPV5L7PfQBHJXHs1rL1swnTvjEi23zG;716b9b522d5306f8ebf86265c89afbc5ced777e13bab1ae46ac30958c734da64;3.1;1687953963348;62f4d401ae05799f14989d31956d3c5ff69bf9d5a722facd4df405c9452a670e06cef39a50ad1e9b78fa7ec6af1b14462c66909b783cc0ffb13050ced02e4907ce98100c47c9aa97794a353958cb4258c9ba85a9b411b2ebc6249d2f4a6340ab4b415d6a036ef09ee8a14e42dc25b0a056f1b628c4eb1d594c54900a4b48c3eb",
            "x-api-eid-token": "jdd03MSVUODKZ52JYZHTAIKFVP532TCX3ZAP5WHUOWRNVPFFBGTYKXW4L3CAZQRRVIINQKPMOML4MGJTGXZDL6HFP5ADDEMAAAAMJAHQ44LAAAAAADFKMNJYTGX6PL4X"
        }
        response = requests.post(self.get_store_url, headers=self.headers, data=data, proxies=self.proxy)
        data_list=response.json()
        response.close()

        for i in data_list['data']:
            data_info = {}
            data_info['store_name'] = i['storeName']
            data_info['store_url'] = i['shopPageUrlM']
            data_info['hash_index']= hashlib.sha256(i['shopPageUrlM'].encode()).hexdigest()
            data_info['address'] = i["address"]
            # print(i['storeName'], i['venderId'], i['storeId'], i["shopPageUrlM"], i["phone"], i["address"],
            #       i['latitude'], i['longitude'])
            data_info['lat']= i['latitude']
            data_info['lon'] =i['longitude']
            data_info['store_id'] =i['storeId']
            data_info['img_list']= self.get_verify(i['storeId'])
            print(data_info)
            self.data_list.append(data_info)
    def get_verify(self,store_id):
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
        data = {
            "functionId": "ds_getExtendInfo",
            "body": "{\"storeId\":\""+str(store_id)+"\"}",
            "appid": "dian_song",
            "t":  int(time.time()*1000),
            "x-api-eid-token": "jdd03MSVUODKZ52JYZHTAIKFVP532TCX3ZAP5WHUOWRNVPFFBGTYKXW4L3CAZQRRVIINQKPMOML4MGJTGXZDL6HFP5ADDEMAAAAMJAH4UXRQAAAAAC2H43LVZBZUXCUX"
        }
        response = requests.post(self.get_verify_url, headers=headers, data=data,proxies=self.proxy)
        # print(response.text)
        res = response.json()
        response.close()
        return str([i['imgUrl'] for i in res['data']['qualification']])

    def get_data(self):
        return self.data_list
    def run(self):
        print("run  >>>   {},{},{}".format('福建',self.latitude,self.longitude))
        self.get_store()

        # print(self.data_list)
def save_ddd(data_l):
    if data_l!=[]:
        import pymysql
        conn = pymysql.connect(host='60.190.6.134', port=29308, user='nltuser', password='tz@&3a1wY^&C', database='nltdb')
        cursor = conn.cursor()
        values = [tuple(i.values()) for i in data_l]
        keys = list(data_l[-1].keys())
        sql_1 = "insert into `{}`(`{}`) values({})".format('fj2p1x_jd', '`,`'.join(data_l[-1].keys()),
                                                           ','.join([''.join('%s') for i in keys]))
        # print(values)
        cursor.executemany(sql_1,values)
        conn.commit()
        cursor.close()
        conn.close()
if __name__=="__main__":
    jd_=jd_spider(*[118.15958,24.726257])
    jd_.run()
    datas=jd_.get_data()
    print("-------------------------")
    print(datas)
    save_ddd(datas)
