# -*- coding: utf-8 -*-
# script for dake
# requirements: instal splinter and webdriver
from splinter import Browser

userName = 'Sxxx'
psw = '123456'

def dakeIn():
    with Browser('chrome') as browser:
        browser.visit("https://ckip.worksap.co.jp/cws/cws/srwtimerec")
        browser.fill('user_id', userName)
        browser.fill('password', psw)
        browser.find_by_value(' 出 社 / Work start ').click()

def dakeOut():
    with Browser('chrome') as browser:
        browser.visit("https://ckip.worksap.co.jp/cws/cws/srwtimerec")
        browser.fill('user_id', userName)
        browser.fill('password', psw)
        browser.find_by_value(' 退 社 / Work end ').click()

dakeIn()
