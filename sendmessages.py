# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests


# 云片
# 单条短信发送
# apikey:成功注册后登录云片官网,进入后台可查看
# text:需要使用已审核通过的模板或者默认模板
# mobile:接收的手机号,仅支持单号码发送
# text = u'【猎头宝】您的验证码是{}。如非本人操作，请忽略本短信'.format('123321')
# mobile = ''
apikey = ''
text1 = '【JLB验证】您的验证口令是#code#。有效期为#hour#，请尽快验证'
text2 = '【JLB验证】正在进行登录操作，您的验证口令是#code#'


def send_sms(text, mobile):
    sms_host = "https://sms.yunpian.com/v2/sms/single_send.json"
    params = {'apikey': apikey, 'text': text, 'mobile': mobile}
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    res = requests.post(sms_host, headers=headers, params=params)
    return res.json()

# res = send_sms(apikey, text1, mobile)
# print res
