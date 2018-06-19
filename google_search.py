import re, sys
from selenium import webdriver
from googlesearch import search
from pyvirtualdisplay import Display


def main():

    display = Display(visible=0, size=(1920, 1080)).start()
    driver = webdriver.Chrome()

    query = sys.argv[1]
    name = sys.argv[-1]

    for sitelist in search(
            query, tld="com", lang="en", num=5, start=0, stop=5, pause=2):
        print(sitelist)
        list = [sitelist]
        for sitelist in list:
            final = re.search(name, sitelist)
            if final:
                print("Found")
            else:
                print("Not Found")

    driver.quit()


if __name__ == '__main__':
    main()