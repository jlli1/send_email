from time import sleep
# from selenium import webdriver
from selenium.webdriver.support.ui import Select
class zhuc:
    def zc(slef,d,q,w,e,r,t,y,u,i,o,p):
        # d = webdriver.Firefox()
        d.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[1]/font/a[2]/img").click()
        sleep(3)
        d.find_element_by_id("username").send_keys(q)
        # sleep(3)
        d.find_element_by_id("email").send_keys(w)
        d.find_element_by_id("password1").send_keys(e)
        d.find_element_by_id("conform_password").send_keys(r)
        # sleep(3)
        d.find_element_by_name("extend_field1").send_keys(t)
        d.find_element_by_name("extend_field2").send_keys(y)
        d.find_element_by_name("extend_field3").send_keys(u)
        d.find_element_by_name("extend_field4").send_keys(i)
        d.find_element_by_name("extend_field5").send_keys(o)
        s = d.find_element_by_name("sel_question")
        aa = Select(s)
        aa.select_by_value("interest")
        d.find_element_by_name("passwd_answer").send_keys(p)
        sleep(3)
        #点击提交
        d.find_element_by_name("Submit").click()
        sleep(5)
        #点击退出
        d.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[1]/font/font/a[2]").click()
        sleep(5)