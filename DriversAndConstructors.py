import time

from selenium import webdriver

from Dictionaries import Constructor
from Dictionaries import Driver


def GetDriversAndConstructors(login, password):
    driver = webdriver.Chrome()



    def site_login():
        driver.get(
            "https://account.formula1.com/#/en/login?redirect=https%3A%2F%2Ffantasy.formula1.com%2F&lead_source"
            "=web_fantasy")
        driver.find_element_by_name("Login").send_keys(login)
        driver.find_element_by_name("Password").send_keys(password + "\n")

    site_login()
    time.sleep(3)
    driver.get("https://fantasy.formula1.com/edit-team/slot/1")
    time.sleep(5)

    dropdown = driver.find_element_by_xpath("//*[@id='dropdownMenuFilterPositions']").click()
    dropdownOptions = driver.find_elements_by_class_name("position-tab")
    dropdownOptions[2].click()

    constructorDivs = driver.find_elements_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[4]/div")

    # Store all Constructors in List
    constructors = []
    for row in constructorDivs:
        name = row.find_element_by_class_name("name").text.replace("CR ", "")
        points = row.find_element_by_class_name("pts").text.replace(" Pts", "")
        price = row.find_element_by_class_name("price").text.replace("$", "").replace("m", "")
        newConstructor = Constructor(name, int(points), float(price))
        constructors.append(newConstructor)

    # Change filter back to "Drivers"
    dropdown = driver.find_element_by_xpath("//*[@id='dropdownMenuFilterPositions']").click()
    dropdownOptions = driver.find_elements_by_class_name("position-tab")
    dropdownOptions[1].click()

    # Store all drivers in list
    drivers = []
    for c in constructors:
        driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[3]/div[1]/div/input").clear()
        driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[3]/div[1]/div/input").send_keys(c.name)
        driverDivs = driver.find_elements_by_xpath("/html/body/div[2]/div[6]/div[1]/div[1]/div[4]/div")
        for row in driverDivs:
            name = row.find_element_by_class_name("name").text.replace("DR ", "").split(" ")[1]
            points = row.find_element_by_class_name("pts").text.replace(" Pts", "")
            price = row.find_element_by_class_name("price").text.replace("$", "").replace("m", "")
            newDriver = Driver(name, int(points), float(price))
            exists = False
            for d in drivers:
                if (d.name == newDriver.name):
                    exists = True
            if not (exists):
                drivers.append(newDriver)
    driver.close()
    return drivers, constructors

# for c in constructors:
#     print(c.name)
#     print(" Pts:"+str(c.points))
#     print(" Prc:"+str(c.price))
#
# for d in drivers:
#     print(d.name)
#     print(" Pts:"+str(d.points))
#     print(" Prc:"+str(d.price))
