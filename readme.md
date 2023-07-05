爬取的是京东快送（同城的）附近的药店和店铺营业执照

https://diansong.jkcsjd.com/channel?source=fujin_yjs_icon&un_area=15_1158_46343_59390&sid=bae8e037cfc0635d249a08035a06685w

完整爬虫在spider.py下
jd_spider类的init中proxy是代理配置请自行更换或删除
latitude，longitude是经纬度需要打点获得或者百度地图接口获取

jd_=jd_spider(*[lon,lat])   #传入经纬度实例化

jd_.run()   #执行

datas=jd_.get_data()   #获取这个点执行完的店铺和证照数据

save_ddd(datas)   #保存数据


"https://color.jkcsjd.com/api/ds_getDistributableStore" 
这个接口接受经纬度返回附近药店
请求的时候h5st参数需要通过get_h5st.js获得



"https://color.jkcsjd.com/api/ds_getExtendInfo"
这个接口接受storeId返回店铺证照


数据库：

CREATE TABLE `fj2p1x_jd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `store_name` varchar(255) DEFAULT NULL,
  `store_url` varchar(255) DEFAULT NULL,
  `hash_index` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `lat` varchar(255) DEFAULT NULL,
  `lon` varchar(255) DEFAULT NULL,
  `store_id` varchar(50) DEFAULT NULL,
  `img_list` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;