from Dictionaries import Driver,Constructor,Team


def refreshTeam(team, driverList, constructorList):
    newTeam = Team([], None)
    for driver in driverList:
        for d in team.drivers:
            if (driver.name == d.name):
                newTeam.drivers.append(driver)
                break

    for constructor in constructorList:
        if (constructor.name == team.constructor.name):
            newTeam.constructor = constructor
            break
    return newTeam