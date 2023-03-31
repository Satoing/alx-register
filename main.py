from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from imgCode import get_code
import csv

name = '你的名字'
idCard = '你的身份证号'
pwd = '你账号的密码'

if __name__ == "__main__":
    service = Service(executable_path='./driver/msedgedriver.exe')

    driver = webdriver.Edge(service=service)

    while True:
        driver.get("http://account.100bt.com/register/register.action?mustIdCard=true")
        driver.find_element(By.ID, "codeImg").screenshot("./img/tmp.jpg")

        code = get_code()
        print(f"验证码----------------{code}")

        driver.find_element(By.ID, 'trueName').send_keys(name)
        driver.find_element(By.ID, 'perCard').send_keys(idCard)
        driver.find_element(By.ID, 'ddNumP').send_keys(pwd)
        driver.find_element(By.ID, 'rddNumP').send_keys(pwd)
        driver.find_element(By.ID, 'captchas').send_keys(code)
        
        driver.find_element(By.ID, 'checkbox1').click()
        driver.find_element(By.ID, 'checkbox2').click()
        driver.find_element(By.ID, 'submit5').click()
        
        time.sleep(5)

        try: uname = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/blockquote[1]/span[2]').text
        except: continue
        
        try: pword = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/blockquote[2]/span[2]').text
        except: continue
        
        print(f'{uname}, {pword}')
        with open("./account.csv", "a", encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([uname, pword, 0, 0, 0, 0])
        
        driver.save_screenshot('./img/account.jpg') # 备份