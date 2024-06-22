import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class Mygpt:
    def __init__(self, *path):
        self.responseThemePathLight = "//*[@class='markdown prose w-full break-words dark:prose-invert light'][last()]"
        self.responseThemePathDark = "//*[@class='markdown prose w-full break-words dark:prose-invert dark'][last()]"
        self.currentTheme = self.responseThemePathDark
        if len(path) != 0:
            self.driver = webdriver.Chrome(path[0])

        else:
            self.driver = uc.Chrome()
    def loadGpt(self):
        self.driver.get("https://chatgpt.com/")
    def getResponse(self, text):
        textarea = self.driver.find_element(By.ID , "prompt-textarea")
        textarea.send_keys(text)
        textarea.send_keys(Keys.RETURN)
        time.sleep(10)
        try:
            response = self.driver.find_element(By.XPATH , self.responseThemePathDark)
            return response.text
        except Exception as e:
            self.currentTheme = self.responseThemePathLight
            response = self.driver.find_element(By.XPATH, self.responseThemePathLight)
            return response.text
    def closeGpt(self):
        self.driver.close()






