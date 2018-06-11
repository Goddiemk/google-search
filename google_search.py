import re
from selenium import webdriver
from googlesearch import search
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1920, 1080)).start()
driver = webdriver.Chrome()
query=input("Enter the search word ")
name = input("Enter your website's name ")
for sitelist in search(query,tld="co.in",lang="en",num=5,stop=1,pause=2):
    print(sitelist)
    list=[sitelist]
    for sitelist in list:
        final=re.search(name,sitelist)
        if final:
            print("Found")
        else: print("Not Found")
driver.quit()