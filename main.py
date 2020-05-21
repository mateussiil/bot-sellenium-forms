from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(15)

def getUrl(url):
    driver.get(url)

def getName():
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[20]/div/div[2]/div/span/div/div[2]').click()
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[21]/div/div[2]/div/span/div/div[3]').click()
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[22]/div/div[2]/div/span/div/div[5]').click()
    submit()

def submit():
    #submit
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div/div[1]').click()

    #proxima
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]').click()

def stop():
    driver.close()

def init(cont):
    for i in range(cont):
        getUrl('https://docs.google.com/forms/d/e/1FAIpQLSc9PGyD0hqCTMHRVulsOQLvavX5V4dGvonHjXyI_9Izcl0vVg/viewform')
        getName()
    




'''
mekudash
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[4]').click()
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[7]/div/div[2]/div/span/div/div[4]').click()
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/span/div/div[5]').click()
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[12]/div/div[2]/div/span/div/div[1]').click()
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[14]/div/div[2]/div/span/div/div[4]').click()
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[25]/div/div[2]/div/span/div/div[7]').click()
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[26]/div/div[2]/div/span/div/div[7]').click()
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[27]/div/div[2]/div/span/div/div[7]').click()
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[28]/div/div[2]/div/span/div/div[7]').click()
'''