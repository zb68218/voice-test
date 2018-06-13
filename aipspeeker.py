# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 11:24
# @Author  : zb
from aip import AipSpeech
import mp3play,time,os

path = os.path.abspath('..//vioce-control//wav//audio.mp3') #获取MP3绝对路径
path1=os.path.realpath('..//vioce-control//dic//test.txt') #获取dic 相对路径
print path
print  path1
############百度ID#######
APP_ID = '10462370'
API_KEY = 'xGFG6Bz1WRXf40CGLjh4Ns6PCa6Bgt8M'
SECRET_KEY = '45X0mnZzIVqugr4XOtfspm6ywjAGj26h'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

#####打开txt文档######
with open(path1) as f:
    a=f.read()
    s=a.decode('gbk').encode('utf-8')
    print s

####返回结果######
result  = client.synthesis(s, 'zh', 1, {'vol': 5,})

#######生成MP3文件#########
if not isinstance(result, dict):
    with open(path, 'wb') as f:
        f.write(result)

p=mp3play.load(path)
p.play()
time.sleep(10)
p.stop()