from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import config
import sys

def vote_Mcrate(link):
    print(f"\n  ||| Launching MCRATE {link} autovote |||")
    driver.get(link)
    time.sleep(2.5)
    try:
        driver.find_element_by_xpath('''/html/body/div[1]/div[6]/table[1]/tbody/tr[1]/td[3]/div[1]/a''').click()

    except:
        print('\n  ||| Xpath not found trying another...- :/ |||\n')
        try:
            driver.find_element_by_xpath('''/html/body/div[1]/div[7]/table[1]/tbody/tr[1]/td[3]/div[1]/a''').click()
        except:
            print("  ||| another xpath is not found, close and try edit... |||")
            driver.close()

    try:
        driver.find_element_by_xpath('''/html/body/div/div[6]/div/a''').click()
        print(" ||| Find div[6] xpath |||")
    except:
        print('  ||| Vk login is not needed? control check another xpath |||\n')

        try:
            driver.find_element_by_xpath('''/html/body/div/div[7]/div/a''').click()
            print("  ||| Find div[7] xpath |||")
        except:
            print('  ||| Vk login is not needed? pass |||')
            pass

        else:
            vkAuth()
    else:
        vkAuth()

    try:
        driver.find_element_by_xpath("/html/body/div/div[6]/form/table/tbody/tr/td[2]/input").send_keys(config.minecraft_login)
        print("  ||| Find div[6] xpath |||")
        driver.find_element_by_xpath("/html/body/div/div[6]/form/table/tbody/tr/td[3]/span").click()

    except:
        print('  ||| Trying another xpath... |||')
        try:
            driver.find_element_by_xpath("/html/body/div/div[7]/form/table/tbody/tr/td[2]/input").send_keys(config.minecraft_login)
            print("Find div[7] xpath")
            driver.find_element_by_xpath("/html/body/div/div[7]/form/table/tbody/tr/td[3]/span").click()
        except:
            print("\n  ||| Cant find XPATH... it may be if programm is launhed today... |||")
            pass


    print("\n  ||| MCRATE IS DONE ||| \n")

    time.sleep(1)


def vote_Mctop(link):
    driver.get(link)

    print(f"\n  ||| launching MCTOP {link} autovote |||")
    time.sleep(2)
    try:
        #driver.find_element_by_css_selector('''#container > section > div > header > div.project-card > div > div.col-xs-2.project-btn.project-btn__vote-btn > button''').click()
        driver.find_element_by_xpath('''/html/body/div[2]/section/div/header/div[2]/div/div[4]/button''').click()
    except:
        print('  ||| Error handling xpath |||')
        pass
    else:
        time.sleep(2)
        driver.find_element_by_xpath('''/html/body/div[3]/div/div/div[2]/div/ul/li/a/i''').click()

    try:
        vkAuth()
    except:
        print('\n  ||| vkAuth is not complete. pass |||')
        pass

    time.sleep(2)

    try:
        driver.find_element_by_xpath('''/html/body/div[3]/div/div/div[2]/form/div/input''').send_keys(config.minecraft_login)
        driver.find_element_by_xpath('''/html/body/div[3]/div/div/div[2]/form/button''').click()
    except:
        print('  ||| Something wrong, or u are voted today |||')
    else:
        print('  ||| Vote done |||\n')

    print("\n  ||| MSTOP IS DONE |||")



    time.sleep(1)

def vote_Topcaraft(link):
    driver.get(link)
    print(f"\n  ||| launching Topcraft {link} autovote |||\n")

    try:
        driver.find_element_by_xpath("/html/body/div[2]/section/header/div[1]/div/div[4]/button").click()
    except:
        print('  ||| Error handling current xpath |||')

    time.sleep(2)
    try:
        driver.find_element_by_xpath('''/html/body/div[3]/div[2]/div/div[2]/div/ul/li/a/i''').click()
    except:
        print('  ||| Cant find /li/a/i element from xpath |||')
        pass

    try:
        vkAuth()
    except:
        print('\n  ||| vkAuth is not complete. pass |||')
        pass

    try:
        driver.find_element_by_xpath('''/html/body/div[3]/div[2]/div/div[2]/form/div/input''').send_keys(config.minecraft_login)
        driver.find_element_by_xpath('''/html/body/div[3]/div[2]/div/div[2]/form/div/button''').click()
    except:
        print('  ||| Error handling current xpath |||')
    else:
        print('  ||| Vote done |||')

    print("\n  ||| TOPCRAFT IS DONE |||")




    time.sleep(2)

def vkAuth():
    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div/div/input[6]").send_keys(config.Vk_login)
    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div/div/input[7]").send_keys(config.Vk_pass)
    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div/div/button").click()


if __name__ == ('__main__'):
    print(r'''
     _______  ______    _______  _______  _______   ______    _______  __   __ 
    |       ||    _ |  |       ||   _   ||       | |    _ |  |   _   ||  | |  |
    |    ___||   | ||  |    ___||  |_|  ||_     _| |   | ||  |  |_|  ||  |_|  |
    |   | __ |   |_||_ |   |___ |       |  |   |   |   |_||_ |       ||       |
    |   ||  ||    __  ||    ___||       |  |   |   |    __  ||       ||_     _|
    |   |_| ||   |  | ||   |___ |   _   |  |   |   |   |  | ||   _   |  |   |  
    |_______||___|  |_||_______||__| |__|  |___|   |___|  |_||__| |__|  |___|  
                  __   _  _  ____  __   _  _   __  ____  ____  ____ 
                 / _\ / )( \(_  _)/  \ / )( \ /  \(_  _)(  __)(  _ \
                /    \) \/ (  )( (  O )\ \/ /(  O ) )(   ) _)  )   /
                \_/\_/\____/ (__) \__/  \__/  \__/ (__) (____)(__\_)''')

    print('\n  |||                Exord Greatray || autovoter v0.2.1 ||                 |||\n')
    print('  |||                        Start in 5 sec                              |||\n')

    print('\n')
    time.sleep(5)

    ua = dict(DesiredCapabilities.CHROME)
    options = webdriver.ChromeOptions()
    # options.add_argument("--user-data-dir=selenium")
    options.add_argument("--window-size=1920,1080")
    #options.add_argument('--headless')
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_driver_binary = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_options=options)

    vote_Mcrate("http://mcrate.su/project/5846")
    vote_Mctop("https://mctop.su/servers/4037")
    vote_Topcaraft("https://topcraft.ru/servers/7071")

    print('\n  ||| All jobs done exit on 5 sec |||')
    print(" OK ")

    driver.close()
    driver.__exit__()

    sys.exit()