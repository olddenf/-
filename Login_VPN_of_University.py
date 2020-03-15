#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user_name='自己的用户名'
user_password='自己的密码'
url='校内网的URL'

def Login_VPN_of_University(url,user_name,user_password):
    browser=webdriver.Chrome()#打开谷歌
    browser.maximize_window()#窗口最大化
    browser.get(url)#输入网址
    input_login=browser.find_element_by_xpath('//*[@name="user[login]"]')#用户名
    input_login.send_keys(user_name)#输入用户名
    time.sleep(3)#停滞3s
    input_password=browser.find_element_by_xpath('//*[@name="user[password]"]')#密码框
    input_password.send_keys(user_password)
    time.sleep(3)#停滞3s
    input_password.send_keys(Keys.ENTER)#回车
    time.sleep(4)
    return browser.page_source#返回成功登录的网页
