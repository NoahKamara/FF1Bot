from selenium import webdriver
from Configuration import loadConfig
from TeamSaver import load
import time
from Dictionaries import Driver, Constructor, Team



def site_login(login, password, webDriver):
    webDriver.get(
        "https://account.formula1.com/#/en/login?redirect=https%3A%2F%2Ffantasy.formula1.com%2F&lead_source"
        "=web_fantasy")
    webDriver.find_element_by_name("Login").send_keys(login)
    webDriver.find_element_by_name("Password").send_keys(password + "\n")
    time.sleep(3)

def createNewTeam(team):
    webDriver = webdriver.Chrome()
    config = loadConfig()
    auth = config.auth
    site_login(auth.login, auth.password, webDriver)
    webDriver.get("https://fantasy.formula1.com/pick-a-team")
    time.sleep(3)
    for driver in team.drivers:
        webDriver.find_element_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[3]/div[1]/div/input").clear()
        webDriver.find_element_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[3]/div[1]/div/input").send_keys(driver.name)
        webDriver.find_element_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[4]/div/span[4]/button").click()

    webDriver.find_element_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[3]/div[1]/div/input").clear()
    webDriver.find_element_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[3]/div[1]/div/input").send_keys(team.constructor.name)
    webDriver.find_element_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[4]/div/span[4]/button").click()
    time.sleep(1)
    webDriver.find_element_by_xpath("/html/body/div[2]/div[6]/div[1]/div[2]/div[2]/div/div[1]/div/div/div[3]").click()
    turboDrivers = webDriver.find_elements_by_xpath("/html/body/div[2]/div[6]/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div")
    time.sleep(1)

    for driver in turboDrivers:
        driverName = driver.find_element_by_class_name("name").text.replace("DR ", "").split(" ")[1]
        if (driverName == team.turboedDriver().name):
            driver.find_element_by_class_name("button__inner").click()
            break
    teamName = input("Enter a name for your team: ")
    time.sleep(1)
    webDriver.find_element_by_xpath("/html/body/div[2]/div[8]/div/div/div/div[2]/form/div[2]/div/div/div[1]/div/input").send_keys(teamName)
    webDriver.find_element_by_xpath("/html/body/div[2]/div[8]/div/div/div/div[2]/form/div[3]/div/button").click()
    #webDriver.close()


def changeTeamMember(old, new):
    webDriver = webdriver.Chrome()
    config = loadConfig()
    auth = config.auth
    site_login(auth.login, auth.password, webDriver)
    webDriver.get("https://fantasy.formula1.com/edit-team/slot/2")
    time.sleep(1)
    driverSlots = webDriver.find_elements_by_xpath("/html/body/div[2]/div[6]/div[1]/div[2]/div[3]/div[6]/div[1]/div")
    for slot in driverSlots:
        slotDriver = slot.find_element_by_class_name("player-name").text
        if (' ' in slotDriver):
            slotDriver = slotDriver.split(" ")[1]
        if (slotDriver.lower() == old.name.lower()):
            slot.find_element_by_class_name("remove-btn").click() #
            break
    webDriver.find_element_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[3]/div[1]/div/input").clear()
    webDriver.find_element_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[3]/div[1]/div/input").send_keys(new.name)
    webDriver.find_element_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[4]/div/span[4]/button").click()
    #webDriver.close()
