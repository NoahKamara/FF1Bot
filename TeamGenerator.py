from itertools import combinations

from Dictionaries import Team


# def generateTableCell(content, maxSpace):
#     newContent = content.rjust(maxSpace - len(content))
#     return newContent
# never used (sören)


def GenerateFrom(drivers, constructors):
    # Create All Possible Driver combinations
    driverTeams = list(combinations(drivers, 5))

    # Create all possible combinations of Driver Teams and Constructors
    fullTeams = []
    for driverTeam in driverTeams:
        for constructor in constructors:
            newFullTeam = Team(driverTeam, constructor)
            fullTeams.append(newFullTeam)

    # Remove Teams over 100Mio
    fullAffordableTeams = []
    for fullTeam in fullTeams:
        if fullTeam.calculatePrice() <= float(100):
            fullAffordableTeams.append(fullTeam)

    # OUTPUT Stats of All Possible Combinations and all possible combinations with money limit
    print("----------------------------------------------------")
    print("STATS:")
    print("\tPossible Combinations:   " + str(len(fullTeams)))
    print("\tWith Money Limit (100m): " + str(len(fullAffordableTeams)))
    print("----------------------------------------------------")

    # Calculate Team with most Points
    bestTeam = max(fullAffordableTeams, key=lambda i: float(i.calculatePoints()))

    # never used aswell (sören)
    # OUTPUT
    print("BEST POSSIBLE TEAM:")
    print(" DRIVERS:")
    print("\t" + "Name".center(13, " ") + "|" + "Turbo".center(7, " ") + "|" + "Points".center(8, " ") + "|" + (
        "Price in Mio").center(14, " "))
    print("\t" + "".center(13, " ") + "|" + "".center(7, " ") + "|" + "".center(8, " ") + "|")
    for driver in bestTeam.drivers:
        name = driver.name.ljust(13, " ")
        turbo = " "
        if bestTeam.turboedDriver().name == driver.name:
            turbo = "TURBO".center(7, " ")
        turbo = turbo.center(7, " ")
        price = str(round(driver.price, 3)).rjust(7, " ") + "Mio"
        points = str(driver.points).center(8, " ")
        dlm = "|"
        print("\t" + name + dlm + turbo + dlm + points + dlm + price)
    print("")
    print(" KONSTRUKTEUR:")
    print("\t" + "Name".center(13, " ") + "|" + "Points".center(8, " ") + "|" + "Price in Mio".center(14, " "))
    print("\t" + bestTeam.constructor.name.center(13, " ") + "|" + (str(bestTeam.constructor.points)).center(8,
                                                                                                             " ") + "|" + (
                  str(bestTeam.constructor.price) + "Mio").center(14, " "))
    print("")
    print(" TEAM STATS:")
    print("   Price:  " + str(round(bestTeam.calculatePrice(), 2)) + " Mio USD")
    print("   Points: " + str(bestTeam.calculatePoints()))
    print("----------------------------------------------------")
    return fullAffordableTeams.sort(key=lambda x: x.calculatePoints())
