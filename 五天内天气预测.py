# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 17:33:36 2018

@author: lenovo
"""
import urllib.request as r
import json
import time
#city_pinyin=input("请输入城市拼音：")
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
print("欢迎使用全球天气APP")
time.sleep(1)
print("当前城市为北京")
print("1.查看当前城市天气，2.查看其它城市天气，3.保存当前城市，")
menno=input("请输入菜单：")
if menno=='1':
    print("当前城市的天气")
    url1='http://api.openweathermap.org/data/2.5/forecast?q=beijing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    
    info=r.urlopen(url1).read().decode('utf-8','ignore')
   
    data=json.loads(info)
    
    
    print('星期天天气：{}\t星期天温度是:{}\t星期天压强是:{}\t星期天最高气温是:{}'.format(data["list"][0]["weather"][0]["description"],data["list"][0]["main"]["temp"],data["list"][0]["main"]["pressure"],data["list"][0]["main"]["temp_max"]))
    print('星期一天气：{}\t星期二温度是:{}\t星期一压强是:{}\t星期一最高气温是:{}'.format(data["list"][9]["weather"][0]["description"],data["list"][9]["main"]["temp"],data["list"][9]["main"]["pressure"],data["list"][9]["main"]["temp_max"]))
    print('星期二天气：{}\t星期天温度是:{}\t星期天压强是:{}\t星期天最高气温是:{}'.format(data["list"][18]["weather"][0]["description"],data["list"][18]["main"]["temp"],data["list"][18]["main"]["pressure"],data["list"][18]["main"]["temp_max"]))
    print('星期三天气：{}\t星期天温度是:{}\t星期天压强是:{}\t星期天最高气温是:{}'.format(data["list"][23]["weather"][0]["description"],data["list"][23]["main"]["temp"],data["list"][23]["main"]["pressure"],data["list"][23]["main"]["temp_max"]))
    print('星期四天气：{}\t星期天温度是:{}\t星期天压强是:{}\t星期天最高气温是:{}'.format(data["list"][34]["weather"][0]["description"],data["list"][34]["main"]["temp"],data["list"][34]["main"]["pressure"],data["list"][34]["main"]["temp_max"]))
if menno=='2':
    print("2.查看其它城市天气")
    time.sleep(1)
    city_pinyin=input("请输入城市拼音：")
    info=r.urlopen(url.format(city_pinyin)).read().decode('utf-8','ignore')
    data=json.loads(info)
    print('星期天天气：{};星期天温度是{};星期天压强是{};星期天最高气温是{}'.format(data["list"][0]["weather"][0]["description"],data["list"][0]["main"]["temp"],data["list"][0]["main"]["pressure"],data["list"][0]["main"]["temp_max"]))
    print('星期一天气：{};星期天温度是{};星期天压强是{};星期天最高气温是{}'.format(data["list"][9]["weather"][0]["description"],data["list"][9]["main"]["temp"],data["list"][9]["main"]["pressure"],data["list"][9]["main"]["temp_max"]))
    print('星期二天气：{};星期天温度是{};星期天压强是{};星期天最高气温是{}'.format(data["list"][18]["weather"][0]["description"],data["list"][18]["main"]["temp"],data["list"][18]["main"]["pressure"],data["list"][18]["main"]["temp_max"]))
    print('星期三天气：{};星期天温度是{};星期天压强是{};星期天最高气温是{}'.format(data["list"][23]["weather"][0]["description"],data["list"][23]["main"]["temp"],data["list"][23]["main"]["pressure"],data["list"][23]["main"]["temp_max"]))
    print('星期四天气：{};星期天温度是{};星期天压强是{};星期天最高气温是{}'.format(data["list"][34]["weather"][0]["description"],data["list"][34]["main"]["temp"],data["list"][34]["main"]["pressure"],data["list"][34]["main"]["temp_max"]))
if menno=='3':

    print("3.保存当前城市")