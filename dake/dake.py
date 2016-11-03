# -*- coding: utf-8 -*-
# script for dake
# requirements: instal splinter and webdriver

from splinter import Browser

#personal info for input
userName = 'Sxxx'
psw = '123456'

def dakeIn():
    with Browser('chrome') as browser:
        url = "https://ckip.worksap.co.jp/cws/cws/srwtimerec"
        browser.visit(url)
        browser.fill('user_id', userName)
        browser.fill('password', psw)
        button = browser.find_by_value(' 出 社 / Work start ')
        button.click()

def dakeOut():
    with Browser('chrome') as browser:
        url = "https://ckip.worksap.co.jp/cws/cws/srwtimerec"
        browser.visit(url)
        browser.fill('user_id', userName)
        browser.fill('password', psw)
        button = browser.find_by_value(' 退 社 / Work end ')
        button.click()

dakeIn()
