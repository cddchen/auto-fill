from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

random.seed(time.time())
opt = webdriver.ChromeOptions()
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path=r'/Users/cdd/Downloads/auto/chromedriver', options=opt)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
driver.get("https://www.wjx.cn/vm/mgVIiyd.aspx")
for i in range(1, 67):
    try:
        if i == 1:
            prob = random.random()
            if prob < 0.1:
                driver.find_element(By.XPATH, "//*[@id=\"div1\"]/div[2]/div[1]/div").click()
            elif prob < 0.3:
                driver.find_element(By.XPATH, "//*[@id=\"div1\"]/div[2]/div[2]/div").click()
            elif prob < 0.8:
                driver.find_element(By.XPATH, "//*[@id=\"div1\"]/div[2]/div[3]/div").click()
            elif prob < 0.9:
                driver.find_element(By.XPATH, "//*[@id=\"div1\"]/div[2]/div[4]/div").click()
            else:
                driver.find_element(By.XPATH, "//*[@id=\"div1\"]/div[2]/div[5]/div").click()
        elif i == 2:
            if random.random() < 0.3:
                driver.find_element(By.XPATH, "//*[@id=\"div2\"]/div[2]/div[2]/div").click()
            else:
                driver.find_element(By.XPATH, "//*[@id=\"div2\"]/div[2]/div[1]/div").click()
        elif i == 3:
            prob = random.random()
            if prob < 0.7:
                driver.find_element(By.XPATH, "//*[@id=\"div3\"]/div[2]/div[1]/div").click()
            elif prob < 0.9:
                driver.find_element(By.XPATH, "//*[@id=\"div3\"]/div[2]/div[2]/div").click()
            else:
                driver.find_element(By.XPATH, "//*[@id=\"div3\"]/div[2]/div[3]/div").click()
        elif i == 4:
            prob = random.random()
            if prob < 0.33:
                driver.find_element(By.XPATH, "//*[@id=\"div4\"]/div[2]/div[1]/div").click()
            elif prob < 0.66:
                driver.find_element(By.XPATH, "//*[@id=\"div4\"]/div[2]/div[2]/div").click()
            else:
                driver.find_element(By.XPATH, "//*[@id=\"div4\"]/div[2]/div[3]/div").click()
        elif i == 5:
            prob = random.random()
            if prob < 0.3:
                driver.find_element(By.XPATH, "//*[@id=\"div5\"]/div[2]/div[1]/div").click()
            elif prob < 0.5:
                driver.find_element(By.XPATH, "//*[@id=\"div5\"]/div[2]/div[2]/div").click()
            elif prob < 0.7:
                driver.find_element(By.XPATH, "//*[@id=\"div5\"]/div[2]/div[3]/div").click()
            else:
                driver.find_element(By.XPATH, "//*[@id=\"div5\"]/div[2]/div[4]/div").click()
        elif i == 6:
            prob = random.random()
            if prob < 0.1:
                driver.find_element(By.XPATH, "//*[@id=\"div6\"]/div[2]/div[1]/div").click()
            elif prob < 0.3:
                driver.find_element(By.XPATH, "//*[@id=\"div6\"]/div[2]/div[2]/div").click()
            elif prob < 0.7:
                driver.find_element(By.XPATH, "//*[@id=\"div6\"]/div[2]/div[3]/div").click()
            elif prob < 0.9:
                driver.find_element(By.XPATH, "//*[@id=\"div6\"]/div[2]/div[4]/div").click()
            elif prob < 0.95:
                driver.find_element(By.XPATH, "//*[@id=\"div6\"]/div[2]/div[5]/div").click()
            else:
                driver.find_element(By.XPATH, "//*[@id=\"div6\"]/div[2]/div[6]/div").click()
        else:
            if random.random() < 0.3:
                if random.random() < 0.5:
                    driver.find_element(By.XPATH, "//*[@id=\"div" + str(i) + "\"]/div[2]/div[1]/div").click()
                else:
                    driver.find_element(By.XPATH, "//*[@id=\"div" + str(i) + "\"]/div[2]/div[2]/div").click()
            else:
                prob = random.random()
                if prob < 0.25:
                    driver.find_element(By.XPATH, "//*[@id=\"div" + str(i) + "\"]/div[2]/div[3]/div").click()
                elif prob < 0.75:
                    driver.find_element(By.XPATH, "//*[@id=\"div" + str(i) + "\"]/div[2]/div[4]/div").click()
                else:
                    driver.find_element(By.XPATH, "//*[@id=\"div" + str(i) + "\"]/div[2]/div[5]/div").click()
    except:
        print(i, "occurs wrong.")
driver.find_element(By.XPATH, "//*[@id=\"ctlNext\"]").click()