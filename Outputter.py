from Dictionaries import Team, Driver, Constructor
import PySimpleGUI as sg


def team(team):
    drivers = []
    for d in team.drivers:
        drivers.append(d)
    print("----------------------------------------------------")
    print(" DRIVERS:")
    print("\t" + "Name".center(13, " ") + "|" + "Turbo".center(7, " ") + "|" + "Points".center(8, " ") + "|" + (
        "Price in Mio").center(14, " "))
    print("\t" + "".center(13, " ") + "|" + "".center(7, " ") + "|" + "".center(8, " ") + "|")
    
    drivers.sort(key=lambda x: x.name, reverse=False)
    driverstringlist = []
    for driver in drivers:
        name = driver.name.ljust(13, " ")
        turbo = " "
        if team.turboedDriver().name == driver.name:
            pass
            turbo = "TURBO".center(7, " ")
        turbo = turbo.center(7, " ")
        price = str(round(driver.price, 3)).rjust(7, " ") + "Mio"
        points = str(driver.points).center(8, " ")
        dlm = "|"
        driverstringlist.append("\t" + name + dlm + turbo + dlm + points + dlm + price)
    print(" KONSTRUKTEUR:")
    print("\t" + "Name".center(13, " ") + "|" + "Points".center(8, " ") + "|" + "Price in Mio".center(14, " "))
    print("\t" + team.constructor.name.center(13, " ") + "|" + (str(team.constructor.points)).center(8,
                                                                                                             " ") + "|" + (
                  str(team.constructor.price) + "Mio").center(14, " "))
    print(" TEAM STATS:")
    print("   Price:  " + str(round(team.calculatePrice(), 2)) + " Mio USD")
    print("   Points: " + str(team.calculatePoints()))
    layout = [[sg.T("\n".join(driverstringlist))],[sg.T(" KONSTRUKTEUR:")],[sg.T("\t" + "Name".center(13, " ") + "|" + "Points".center(8, " ") + "|" + "Price in Mio".center(14, " "))],[sg.T("\t" + team.constructor.name.center(13, " ") + "|" + (str(team.constructor.points)).center(8,
                                                                                                             " ") + "|" + (
                  str(team.constructor.price) + "Mio").center(14, " "))],[sg.T(" TEAM STATS:")],[sg.T("   Price:  " + str(round(team.calculatePrice(), 2)) + " Mio USD")],[sg.T("   Points: " + str(team.calculatePoints()))],[sg.Button("Ok")]]
    x = sg.Window("Team", layout)
    event,_ = x.read()
    x.close()

def memberChange(old, new):
    # print("CHANGE: "+old.name+" -> "+new.name)
    # print("\t" + "Name".center(13, " ") + "|"+ "Points".center(8, " ") + "|" + (
    #     "Price in Mio").center(14, " "))
    driverlist = []
    for driver in [old, new]:
        name = driver.name.ljust(13, " ")
        price = str(round(driver.price, 3)).rjust(7, " ") + "Mio"
        points = str(driver.points).center(8, " ")
        dlm = "|"
        driverlist.append("\t" + name + dlm + points + dlm + price)
    layout = [[sg.T("\n".join(driverlist))],
    [sg.T("CHANGE: "+old.name+" -> "+new.name)],
    [sg.T("\t" + "Name".center(13, " ") + "|"+ "Points".center(8, " ") + "|" + "Price in Mio".center(14, " "))],
    [sg.T("\t" + name + dlm + points + dlm + price)],[sg.Button("Ok")]]
    x = sg.Window("Member Change", layout)
    event,_ = x.read()
    x.close()
