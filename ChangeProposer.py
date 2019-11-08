from Dictionaries import Driver, Constructor, Team
import random
import TeamSaver
import Outputter


def generateDummies():
    dummyDrivers = ["Dummy1", "Dummy2", "Dummy3", "Dummy4", "Dummy5"]
    drivers = []
    for d in dummyDrivers:
        ranPoints = random.randint(100, 500)
        ranPrice = float(random.randint(5, 20))
        newDriver = Driver(d, ranPoints, ranPrice)
        drivers.append(newDriver)
    return drivers

def others(team,drivers, constructors):
    oldDrivers = []
    for d in team.drivers:
        oldDrivers.append(d.name)
    newDrivers = []
    for driver in drivers:
        if not (driver.name in oldDrivers):
            newDrivers.append(driver)

    newConstructors = []
    for constructor in constructors:
        if not (constructor.name == newConstructors):
            newConstructors.append(constructor)
    return newDrivers, newConstructors


def DriverComparer(otherDrivers):
    formerTeam = TeamSaver.load()
    otherDrivers.sort(key=lambda x: x.points, reverse=True)
    possibleNewTeams = [formerTeam]
    for driver in formerTeam.drivers:
        for other in otherDrivers:
            if (other.price <= driver.price) and (other.points > driver.points):  # Other Driver is Cheaper or the same price AND has more points
                newTeam = Team([other], formerTeam.constructor)
                for d in formerTeam.drivers:
                    if not (d.name == driver.name):
                        newTeam.drivers.append(d)
                possibleNewTeams.append(newTeam)
                break
    print(len(possibleNewTeams))
    bestTeam = max(possibleNewTeams, key=lambda i: float(i.calculatePoints()))

    return bestTeam


def ConstructorCompare(otherConstructors):
    formerTeam = TeamSaver.load()
    newTeam = Team(formerTeam.drivers, formerTeam.constructor)
    otherConstructors.sort(key=lambda x: x.points, reverse=True)
    for other in otherConstructors:
        if (other.price <= formerTeam.constructor.price) and (
                other.points > formerTeam.constructor.points):  # Other Driver is Cheaper or the same price AND has more points
            newTeam = Team(formerTeam.drivers, other)
            break
    return newTeam

def proposeChange(drivers, constructors):
    formerTeam = TeamSaver.load()

    otherDrivers, otherConstructors = others(formerTeam, drivers, constructors)
    for d in otherDrivers:
        print(d.name)
    for d in otherConstructors:
        print(d.name)
    driverChangeBestTeam = DriverComparer(otherDrivers)
    constructorChangeBestTeam = ConstructorCompare(otherConstructors)
    bestTeam = max([driverChangeBestTeam, constructorChangeBestTeam], key=lambda i: float(i.calculatePoints()))
    Outputter.team(bestTeam)
    if (bestTeam == driverChangeBestTeam):
        new = None
        for driver in bestTeam.drivers:
            if not (driver in formerTeam.drivers):
                newDriver = driver
                break

        old = None
        for driver in formerTeam.drivers:
            if not (driver in bestTeam.drivers):
                oldDriver = driver
                break
        if not ((old == None) or (new == None)):
            Outputter.memberChange(old, new)
            print("As Yoda said : There is another (Driver)- And its better")
    elif (bestTeam == constructorChangeBestTeam):
        oldTeam = TeamSaver.load().constructor
        new = oldTeam.constructor
        old = bestTeam.constructor
        if not ((old == None) or (new == None)):
            Outputter.memberChange(old, new)
            print("As Yoda said : There is another (Constructor) - And its better")
    if (bestTeam == constructorChangeBestTeam) and (bestTeam == driverChangeBestTeam):
        print("There is no better Team. Yoda was wrong")
    return bestTeam