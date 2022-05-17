from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
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
RandNum = lambda x, y: random.randint(x, y)
def NormNum3to5() -> int:
    p = random.random()
    return 3 if p < 0.5 else (4 if p < 0.8 else 5)
def NormNum1to3() -> int:
    p = random.random()
    return 3 if p < 0.5 else (2 if p < 0.8 else 1)
second_part_personality = random.random() < 0.25
personality = not second_part_personality and random.random() < 0.8 

print(personality)
for i in range(1, 67):
    if i == 38:
        continue
    try:
        # age
        if i == 6:
            continue
        if i == 1:
            prob = random.random()
            if prob < 0.1:
                # <=20
                driver.find_element(By.XPATH, "//*[@id=\"div1\"]/div[2]/div[1]/div").click()
                driver.find_element(By.XPATH, "//*[@id=\"div6\"]/div[2]/div[1]/div").click()
            elif prob < 0.3:
                # 21-30
                driver.find_element(By.XPATH, "//*[@id=\"div1\"]/div[2]/div[2]/div").click()
                driver.find_element(By.XPATH, "//*[@id=\"div6\"]/div[2]/div[" + str(NormNum1to3()) + "]/div").click()
            elif prob < 0.8:
                # 31-40
                driver.find_element(By.XPATH, "//*[@id=\"div1\"]/div[2]/div[3]/div").click()
                driver.find_element(By.XPATH, "//*[@id=\"div6\"]/div[2]/div[" + str(RandNum(1, 4)) + "]/div").click()
            elif prob < 0.9:
                # 41-50
                driver.find_element(By.XPATH, "//*[@id=\"div1\"]/div[2]/div[4]/div").click()
                driver.find_element(By.XPATH, "//*[@id=\"div6\"]/div[2]/div[" + str(RandNum(1, 5)) + "]/div").click()
            else:
                # >= 50
                driver.find_element(By.XPATH, "//*[@id=\"div1\"]/div[2]/div[5]/div").click()
                driver.find_element(By.XPATH, "//*[@id=\"div6\"]/div[2]/div[" + str(RandNum(1, 6)) + "]/div").click()
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
            driver.find_element(By.XPATH, "//*[@id=\"div4\"]/div[2]/div[" + str(NormNum1to3()) + "]/div").click()
        elif i == 5:
            prob = random.random()
            if prob < 0.3:
                driver.find_element(By.XPATH, "//*[@id=\"div5\"]/div[2]/div[1]/div").click()
            elif prob < 0.5:
                driver.find_element(By.XPATH, "//*[@id=\"div5\"]/div[2]/div[2]/div").click()
            elif prob < 0.65:
                driver.find_element(By.XPATH, "//*[@id=\"div5\"]/div[2]/div[3]/div").click()
            else:
                driver.find_element(By.XPATH, "//*[@id=\"div5\"]/div[2]/div[4]/div").click()
        # second part
        elif i >= 7 and i <= 50:
            num = str(NormNum1to3()) if (second_part_personality and random.random() < 0.9) else str(NormNum3to5())
            driver.find_element(By.XPATH, "//*[@id=\"div" + str(i) + "\"]/div[2]/div[" + num + "]/div").click()
        # third part
        elif i >= 51 and i <= 59:
            num = str(NormNum3to5()) if (personality and random.random() < 0.9) else str(NormNum1to3())
            driver.find_element(By.XPATH, "//*[@id=\"div" + str(i) + "\"]/div[2]/div[" + num + "]/div").click()
        elif i >= 60 and i <= 66:
            num = str(NormNum1to3()) if (personality and random.random() < 0.9) else str(NormNum3to5())
            driver.find_element(By.XPATH, "//*[@id=\"div" + str(i) + "\"]/div[2]/div[" + num + "]/div").click()
    except Exception as e: print(e)
driver.find_element(By.XPATH, "//*[@id=\"ctlNext\"]").click()
check = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id=\"rectMask\"]")))
check.click()
check = WebDriverWait(driver, 5).until(ec.invisibility_of_element_located((By.XPATH, "//*[@id=\"rectMask\"]")))
driver.close()