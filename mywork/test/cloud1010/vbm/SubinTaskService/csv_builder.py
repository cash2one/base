# ! /usr/bin/python
# -*- coding:utf-8 -*-
# Filename: csv_helper.py
# Author: jack
# E-mail: jack_chen@subin.cn
# Date: 2016-06-22
# Description: csv文件构建类

import csv
import codecs
import time
from pymongo import MongoClient
import pymongo
from config import *
from logger import *

ISO_TIMEFORMAT = '%Y-%m-%d %H:%M'
SUBING_TIMEFORMAT = '%Y.%m.%d %H:%M'

def _get_dict_value(dict_name, key):
    value = ''
    try:
        if(dict_name == None):
            return value
        if key in dict_name:
            value = dict_name[key]
            value = str(value)
            if value.isdigit():
                if len(value) > 15:
                    value = ',' + value
    except Exception as e:
        logging.exception(e)
    return value

def build_csv(before_day=1):
    conn = MongoClient(mongodb_host, mongodb_port)
    db = conn.park
    collection = db.user_order
    orders = collection.find({"park_id": export_park_id}).sort('quit_time', pymongo.DESCENDING)
    coupons = db.coupon_management.find({"park_id": export_park_id}).sort('quit_time', pymongo.DESCENDING) # coupon
    rows = []
    rows_coupon = [] # coupon 
    days = datetime.timedelta(days=before_day)
    yesterday = datetime.date.today() - days
    for order in orders:
        if order['pay_time'].date() == yesterday:
            wechatorder = db.wechat_order.find_one({'seq': order['seq']})
            rows.append({'订单号': _get_dict_value(order, 'seq'), '票据':  _format_ticket(order['ticket']),
                         '微信号': _get_dict_value(order, 'wechat_id'), '支付宝号': _get_dict_value(order, 'alipay_id'),
                         '支付类型': _get_pay_type(order['pay_type']), '车牌号': _get_dict_value(order, 'license_plate'),
                         '停留时间': _format_seconds_to_hhmmss(order['time']),
                         '进库时间': _formate_subin_time(_get_dict_value(order, 'entry')),
                         '订单时间': _formate_subin_time(_get_dict_value(order, 'quit_time')),
                         '付费时间': order['pay_time'].strftime(ISO_TIMEFORMAT),
                         '折扣': _get_dict_value(order, 'discount'), '应收金额': _get_dict_value(order, 'price'),
                         '优惠金额': _get_dict_value(order, 'coupon_price'),
                         '实收金额': _get_dict_value(order, 'ActualPrice') if order['isPaid'] else 0,
                         '是否支付': '是' if order['isPaid'] else '否', '发票状态':'已发放'if order['isInvoice'] else '未发放',
                         '优惠券编号': _get_dict_value(order, 'chooseCouponId'), '停车场编号': _get_dict_value(order, 'park_id'),
                         '停车场名称': _get_dict_value(order, 'park_name'), '物业公司': _get_dict_value(order, 'company_name'),
                         '平台订单': _get_dict_value(wechatorder, 'out_trade_no'), '微信OPEN_ID': _get_dict_value(order, 'wechat_openId'),
                         '第三方微信OPEN_ID': _get_dict_value(order, 'third_wechat_openId')})
            del order['_id']

    # 卡券
    for coupon in coupons:
        rows_coupon.append({'卡券名称': _get_dict_value(coupon, 'coupon_name'), '卡券ID': _get_dict_value(coupon, 'coupon_id'), 
                            '卡券金额': _get_dict_value(coupon, 'price'), '卡券有效起始时间': _get_dict_value(coupon, 'receive_date'),
                            '卡券有效截止时间': _get_dict_value(coupon, 'receive_close_date'), '卡券类型': _get_dict_value(coupon, 'coupon_type'),
                            '总量': _get_dict_value(coupon, 'amount'), '已领取数量': _get_dict_value(coupon, 'receive_amount'), 
                            '已使用数量': _get_dict_value(coupon, 'used_amount'), '指定停车场': _get_dict_value(coupon, 'parks'), 
                            '卡券状态': _get_dict_value(coupon, 'coupon_status'), '停车场商家': _get_dict_value(coupon, 'company_name'), 
                            '消费金额': float(_get_dict_value(coupon, 'used_amount')) * float(_get_dict_value(coupon, 'price'))})


    conn.close()

    fieldnames = ['订单号', '票据', '微信号', '支付宝号', '支付类型', '车牌号', '停留时间', '进库时间', '订单时间'
        , '付费时间', '折扣', '应收金额', '优惠金额', '实收金额', '是否支付', '发票状态', '优惠券编号', '停车场编号'
        , '停车场名称', '物业公司', '平台订单', '微信OPEN_ID', '第三方微信OPEN_ID']

    fieldnames_coupon = ['卡券名称', '卡券ID', '卡券金额', '卡券有效起始时间', '卡券有效截止时间', '卡券类型', '总量', '已领取数量', '已使用数量', '指定停车场', '卡券状态', '停车场商家', '消费金额']  # 卡券

    csv_file = export_park_id + '-wxpay-' + yesterday.__format__('%Y%m%d') + '.csv'

    csv_file_coupon = export_park_id + '-coupon-' + yesterday.__format__('%Y%m%d') + '.csv' # 卡券

    if not os.path.exists('file'):
        os.makedirs('file')
    with open('file/' + csv_file, 'w', encoding='utf-8_sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
   
    # 卡券
    with open('file/' + csv_file_coupon, 'w', encoding='utf-8_sig', newline='') as f_coupon:
        writer = csv.DictWriter(f_coupon, fieldnames=fieldnames_coupon)
        writer.writeheader()
        writer.writerows(rows_coupon)

        #  不需要统计信息
        # (totalActualPrice, totalpreferentialPrice, totalPrice) = _calc_price(rows)
        # writer.writerow({ '票据': '应收金额', '微信号': totalPrice})
        # writer.writerow({'票据': '优惠总金额', '微信号': totalpreferentialPrice})
        # writer.writerow({'票据': '实际金额', '微信号': totalActualPrice})
    return csv_file, csv_file_coupon

def _formate_subin_time(strtime):
    d = datetime.datetime.strptime(strtime, SUBING_TIMEFORMAT)
    time_sec_float = time.mktime(d.timetuple())
    timeFormate = time.strftime(ISO_TIMEFORMAT, time.localtime(time_sec_float))
    return str(timeFormate)

def _calc_price(rows):
    totalActualPrice = 0.0
    totalpreferentialPrice = 0.0
    totalPrice = 0.0
    for row in rows:
        totalActualPrice += float('%0.2f' % float(row['实收金额']))
        totalpreferentialPrice += float('%0.2f' % float(row['优惠金额']))
        totalPrice += float('%0.2f' % float(row['应收金额']))
    return (totalActualPrice, totalpreferentialPrice, totalPrice)

def _get_pay_type(pay_type):
    if pay_type == 1:
        return '1.微信'
    elif pay_type == 2:
        return '2.支付宝'
    else:
        return '未知'


def _format_ticket(ticket):
    if ticket:
        parkid = ticket[0:4]
        ticket = ticket[5:-3] + '.' + parkid
        return ticket

# 将秒转换成时分秒格式
def _format_seconds_to_hhmmss(seconds):
    if seconds != None:
        hours = seconds // (60 * 60)
        seconds %= (60 * 60)
        minutes = seconds // 60
        seconds %= 60
        return "%i:%02i:%02i" % (hours, minutes, seconds)
    return "%i:%02i:%02i" % (0, 0, 0)
