import TeamSaver
from Dictionaries import Driver,Constructor,Team


def refreshTeam(driverList, constructorList):
    team = TeamSaver.load()
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
    TeamSaver.save(newTeam)
    return newTeam