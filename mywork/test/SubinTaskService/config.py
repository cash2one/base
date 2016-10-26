#! /usr/bin/python
# -*- coding:utf-8 -*-
# Filename: config.py
# Author: jack
# E-mail: jack_chen@subin.cn
# Date: 2016-06-22
# Description: 配置文件基类

from pymongo import MongoClient
import pymongo
from logger import *
from prettytable import PrettyTable

mongodb_host = 'localhost'
mongodb_port = 27017
conn = MongoClient(mongodb_host, mongodb_port)
db = conn.park
export_csv_interval = 24  # 小时
export_before_days = [1]

def _get_dict_value(dict_name, key):
    value = ''
    try:
        if(dict_name == None):
            return value
        if key in dict_name:
            value = dict_name[key]
            value = str(value)
    except Exception as e:
        logging.exception(e)
    return value

db_config = (db.ftp_config.find_one()) # 配置信息字典
ftp_ip = _get_dict_value(db_config, 'ftp_ip')

answer = input("您需要加载默认配置吗？（ENTER）加载默认/输入其他进行手动配置）> ")
while True:
    if ftp_ip == "" and answer == '':
        print("未发现默认配置，请确认! ")
        answer = input("您需要加载默认配置吗？（ENTER）加载默认/输入其他进行手动配置）> ")
    else:
        break

if answer == "":
    ftp_ip = _get_dict_value(db_config, 'ftp_ip') #
    ftp_name = _get_dict_value(db_config, 'ftp_name')  #
    ftp_psw = _get_dict_value(db_config, 'ftp_psw') #
    export_csv_time = _get_dict_value(db_config, 'export_csv_time') #
    export_park_id = _get_dict_value(db_config, 'export_park_id') #
    ftp_path = input("请输入FTP路径 > ")
    table = PrettyTable(['FTP_IP', 'FTP_NAME', 'FTP_PSW', 'EXPORT_CSV_TIME', 'EXPORT_PARK_ID']) # 将默认配置绘制成表格，输出到屏幕
    table.add_row([ftp_ip, ftp_name, "******", export_csv_time, export_park_id])
    print ("默认配置：")
    print (table)
else:
    ftp_ip = input('请输入FTP服务器地址 > ') # 设置FTP服务器地址
    ftp_name = input('请输入用户名 > ') # FTP用户名
    ftp_psw = input('请输入密码 > ') # FTP 密码
    ftp_path = input("请输入FTP路径 > ")
    export_csv_time = input('请设置导出时间（格式：xx:xx:xx）> ') # 时间


    # 获取所有停车场
    def park_list():
        collection = db.park_management    
        parks = collection.find()
        return parks

    # 选择停车场
    print ("您需要选择停车场，以下为您可选择的停车场，请输入您选择的停车场的ID >")
    parks = park_list()
    parks_id_cache = []
    print ('停车场ID', '\t', '停车场名称')
    print ("-"*50)
    for p in parks:     # 列出可选停车场
        print (p['park_id'], '\t\t', p['park_name'])
        parks_id_cache.append(p['park_id'])

    # 判断停车场ID输入可行性
    export_park_id = input('> ') 
    while True:
        if export_park_id in parks_id_cache:
            break
        else:
            print ('您输入的停车场ID不存在，请重新输入 > ')
            export_park_id = input('> ')

    config_dic = {'ftp_ip': ftp_ip, 'ftp_name': ftp_name, 'ftp_psw': ftp_psw, \
                                          'export_csv_time': export_csv_time, 'export_park_id': export_park_id}

    end_answer = input("您是否要将此配置保存为默认配置？（'ENTER' 保存/其他不保存）> ")
    if end_answer == '':
        print ('Saving...')
        if not db.ftp_config.find_one():
            db.ftp_config.save(config_dic)
        db.ftp_config.update({}, {'$set': config_dic})
        print ('OK Saved!')
    else:
        print ('NO save!')

conn.close()
