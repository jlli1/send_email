from seleniumDemo.day04.zhuce_demo.zhs_d import zhuc
from selenium import webdriver
import csv
import unittest
# 注册登录化
class zhce(unittest.TestCase):
    a = zhuc()
    def setUp(self):
        self.d = webdriver.Firefox()
        self.d.get("http://192.168.2.143/ecshop/")
        self.file = open("D:\\FTP\\10selenium\\zhuce.csv",encoding="utf-8")
        self.data = csv.reader(self.file)
        self.d.maximize_window()
    def test_zhuce(self):
        for i in self.data:
            self.a.zc(self.d,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9])
    def tearDown(self):
        self.file.close()
        self.d.close()

if __name__ == "__main__":
    unittest.main()
