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

    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:jmgo123456@127.0.0.1:3306/test20190704'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://hpcheng:123456@192.168.10.154/hotel_server'

    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 打印sql
    # SQLALCHEMY_ECHO = True

    DEBUG = True
    # flask-admin语言设置
    # ---------------------------------------------------
    SECRET_KEY = 'chenhuping'
    # 选择语言
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    # 设置flask-login的cookie的过期时间
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=5)
    # 分页相关
    # POSTS_PER_PAGE = 2
    #
    FLASKY_POSTS_PER_PAGE = 20

    # 上传文件
    # 设置上传文件的地址
    # UPLOADED_PHOTOS_DEST = os.path.join(os.getcwd(), 'upload/image')
    # 配置上传文件大小，默认64M，设置None则会采用MAX_CONTENT_LENGTH配置选项
    # app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024

    # UPLOAD_FOLDER = 'C:\Users\chenhuping\Desktop\\newsoul\marshmallowjmgo\upload'

    # 省份代码
    PROVINCE_CODE = {"北京市": 11, "天津市": 12, "上海市": 31, "重庆市": 50,
                     '河北省': 13, "河南省": 41, "云南省": 53, "辽宁省": 21, "黑龙江省": 23,
                     "湖南省": 43, "安徽省": 34, "山东省": 37, "新疆维吾尔自治区": 65, "江苏省": 32, "浙江省": 33,
                     "江西省": 36, "湖北省": 42, "广西壮族自治区": 45, "甘肃省": 62, "山西省": 14,
                     "内蒙古自治区": 15, "陕西省": 61, "吉林省": 22, "福建省": 35, "贵州省": 52, "广东省": 44,
                     "青海省": 63, "西藏自治区": 54, "四川省": 51, "宁夏回族自治区": 64, "海南省": 46}

    KEY = 'HJSOP0982MKjyqgb'
    IV = 'P091jMGAQLybx82G'
    # 坚果服务器地址
    JMGO_SERVER_ROOT = "http://192.168.10.243:10011"
