# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 17:33:36 2018

@author: lenovo
"""
while True:
    import urllib.request as r
    import json
    import time
    days=[0,8,16,24,32]
    url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    a=open('state.txt','r').readline(1)
    if a=='1':
        print("欢迎使用全球天气APP")
    else:
        print("欢迎第一次使用我的全球天气app")
        url1='http://api.openweathermap.org/data/2.5/forecast?q=beijing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
        open('state.txt','w').write('1')
        print("当前城市为北京")
    time.sleep(1)
    print("1.查看当前城市天气；2.查看其它城市天气;3.其它任意键退出")
    menno=input("请输入菜单：")
    if menno=='2':
        print("2.查看其它城市天气")
        time.sleep(1)
        city_pinyin=input("请输入城市拼音：")
        info=r.urlopen(url.format(city_pinyin)).read().decode('utf-8','ignore')
        data=json.loads(info)
        def tianqi1(day):
            print('{}天气：{}\t温度是：{}\t压强是：{}\t最高气温是：{}'.format(data["list"][day]["dt_txt"][0:10],data["list"][day]["weather"][0]["description"],data["list"][day]["main"]["temp"],data["list"][day]["main"]["pressure"],data["list"][day]["main"]["temp_max"]))   
        for day in days:
            tianqi1(day) 
        print("您是否要保存当前城市为默认城市")
        print("1、是；2、否")
        s=input("请选择")
        if s=='1':
            url1=url.format(city_pinyin)
            time.sleep(2)
            print("保存成功")
        else:
            break
    elif menno=='1':
        print("当前城市的天气")
        #url1='http://api.openweathermap.org/data/2.5/forecast?q=beijing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
        info=r.urlopen(url1).read().decode('utf-8','ignore')
        data=json.loads(info)
        def tianqi(day):
            print('{}天气：{}\t温度是：{}\t压强是：{}\t最高气温是：{}'.format(data["list"][day]["dt_txt"][0:10],data["list"][day]["weather"][0]["description"],data["list"][day]["main"]["temp"],data["list"][day]["main"]["pressure"],data["list"][day]["main"]["temp_max"]))
        for day in days:
            tianqi(day)   
    else:
        break
    time.sleep(2)