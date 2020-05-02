from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime
from selenium.webdriver.common.action_chains import ActionChains
username = os.environ.get("YOUR USERNAME FROM THE ENVIRONMENT VARIABLES")
password = os.environ.get("YOUR PASSWORD FROM THE ENVIRONMENT VARIABLES")

# ADD AS MANY FRIENDS AS YOU LIKE
friends = [{'name': 'YOUR FRIENDS USERNAME',
            'bday': 'YOUR FRIENDS BIRTHDAY IN DD/M'}]
tday = datetime.date.today()
dateon = tday.day
datemonth = tday.month
birthday = f"{dateon}-{datemonth}"
people = []
for i in friends:
    if birthday in i['bday']:
        people.append(i['name'])


class InstaBot():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.people = people

    def sendmessage(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(f"{self.username}")
        sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(f"{self.password}")
        sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div").click()
        sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[3]/button[2]").click()
        sleep(5)
        # SEarching
        for i in people:
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div").click()
            sleep(5)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(f"{i}")
            sleep(5)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a/div/div[2]/div/span").click()
            sleep(5)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/button").click()
            sleep(5)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("HAPPY BDAYY!!"+Keys.ENTER)
            sleep(5)
            self.driver.get("https://www.instagram.com/")
            sleep(5)


if len(people) != 0:
    for i in people:
        print(f"The wishes were sent to {i}")
else:
    print("No birthdays todayy!!!")
bot = InstaBot(username, password)
bot.sendmessage()
