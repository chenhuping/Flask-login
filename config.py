#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : config.py
# @Author : Chenhuping
# @Date   : 2019/7/4 15:03
# @Explain:


import datetime
import os


class AboutConfig(object):
    # 调试模式
    FLASK_DEBUG = 1
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://hpcheng:123456@192.168.10.154/hotel_server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = 'xxxxxx'
    # 选择语言
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    # 设置flask-login的cookie的过期时间
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=5)
    FLASKY_POSTS_PER_PAGE = 20
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
    # 省份代码
    PROVINCE_CODE = {"北京市": 11, "天津市": 12, "上海市": 31, "重庆市": 50,
                     '河北省': 13, "河南省": 41, "云南省": 53, "辽宁省": 21, "黑龙江省": 23,
                     "湖南省": 43, "安徽省": 34, "山东省": 37, "新疆维吾尔自治区": 65, "江苏省": 32, "浙江省": 33,
                     "江西省": 36, "湖北省": 42, "广西壮族自治区": 45, "甘肃省": 62, "山西省": 14,
                     "内蒙古自治区": 15, "陕西省": 61, "吉林省": 22, "福建省": 35, "贵州省": 52, "广东省": 44,
                     "青海省": 63, "西藏自治区": 54, "四川省": 51, "宁夏回族自治区": 64, "海南省": 46}
