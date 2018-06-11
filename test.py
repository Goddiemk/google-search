import unittest,re
from selenium import webdriver
from googlesearch import search
from pyvirtualdisplay import Display

class test1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def testing(self):
        query="foods"
        for je in search(query,tld="com",num=5,stop=1,pause=2):
            print(je)
            list=[je]
            testa = "http://www.mdpi.com/"
            for je in list:
                m = re.match(testa,je)
                if m:
                    print("Found")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
