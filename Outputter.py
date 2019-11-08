from Dictionaries import Team, Driver, Constructor
def team(team):
    print("----------------------------------------------------")
    print(" DRIVERS:")
    print("\t" + "Name".center(13, " ") + "|" + "Turbo".center(7, " ") + "|" + "Points".center(8, " ") + "|" + (
        "Price in Mio").center(14, " "))
    print("\t" + "".center(13, " ") + "|" + "".center(7, " ") + "|" + "".center(8, " ") + "|")
    for driver in team.drivers:
        name = driver.name.ljust(13, " ")
        turbo = " "
        if team.turboedDriver().name == driver.name:
            turbo = "TURBO".center(7, " ")
        turbo = turbo.center(7, " ")
        price = str(round(driver.price, 3)).rjust(7, " ") + "Mio"
        points = str(driver.points).center(8, " ")
        dlm = "|"
        print("\t" + name + dlm + turbo + dlm + points + dlm + price)
    print("")
    print(" KONSTRUKTEUR:")
    print("\t" + "Name".center(13, " ") + "|" + "Points".center(8, " ") + "|" + "Price in Mio".center(14, " "))
    print("\t" + team.constructor.name.center(13, " ") + "|" + (str(team.constructor.points)).center(8,
                                                                                                             " ") + "|" + (
                  str(team.constructor.price) + "Mio").center(14, " "))
    print("")
    print(" TEAM STATS:")
    print("   Price:  " + str(round(team.calculatePrice(), 2)) + " Mio USD")
    print("   Points: " + str(team.calculatePoints()))
    print("----------------------------------------------------")

def memberChange(old, new):
    print("----------------------------------------------------")
    print("CHANGE: "+old.name+" -> "+new.name)
    print("\t" + "Name".center(13, " ") + "|"+ "Points".center(8, " ") + "|" + (
        "Price in Mio").center(14, " "))
    for driver in [old, new]:
        name = driver.name.ljust(13, " ")
        price = str(round(driver.price, 3)).rjust(7, " ") + "Mio"
        points = str(driver.points).center(8, " ")
        dlm = "|"
        print("\t" + name + dlm + points + dlm + price)
    print("----------------------------------------------------")