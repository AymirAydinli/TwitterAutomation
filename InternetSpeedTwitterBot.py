from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self, up, down):
        self.driver = webdriver.Chrome(chrome_options)
        self.up = up
        self.down = down
        self.twitter_email = TWITTER_EMAIL
        self.twitter_username = TWITTER_USERNAME
        self.twitter_password = TWITTER_PASSWORD

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(30)
        pass_trust = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        pass_trust.click()
        go_button = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(50)
        down_res = self.driver.find_element(By.CSS_SELECTOR, value='div .download-speed')
        up_res = self.driver.find_element(By.CSS_SELECTOR, value='div .upload-speed')
        return down_res.text, up_res.text



    def close_window(self):
        self.driver.quit()

    def tweet_at_provider(self, down_speed, up_speed):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(15)
        input_email = self.driver.find_element(By.TAG_NAME, value="input")
        print(self.twitter_email)
        input_email.send_keys(self.twitter_email)
        input_email.send_keys(Keys.ENTER)
        time.sleep(15)
        input_username = self.driver.find_element(By.TAG_NAME, value="input")
        input_username.send_keys(self.twitter_username)
        input_username.send_keys(Keys.ENTER)
        time.sleep(15)
        pwd = self.driver.find_element(By.NAME, value="password")
        pwd.send_keys(self.twitter_password)
        pwd.send_keys(Keys.ENTER)
        time.sleep(50)
        internet_provider = "Internet Provider"
        if float(self.down) > float(down_speed) or float(self.up) > float(up_speed):
            tweet = f"Hey {internet_provider}, why is my internet speed {down_speed}down/{up_speed}up when I pay for {self.down}down/{self.up}up?"
        else:
            tweet = f"Hey {internet_provider} thank you for providing a good service."

        post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                        '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                        '1]/div/div/div/div[2]/div['
                                                        '1]/div/div/div/div/div/div/div/div/div/div/label/div['
                                                        '1]/div/div/div/div/div/div[2]/div/div/div/div')

        post.send_keys(tweet)
        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                               '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                               '1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div['
                                                               '3]/div/span/span')
        post_button.click()
        print("success")
