from itertools import combinations
import TeamSaver
from Dictionaries import Team
import Outputter

# def generateTableCell(content, maxSpace):
#     newContent = content.rjust(maxSpace - len(content))
#     return newContent
# never used (sören)


def makeBestTeamListUnder100M(drivers, constructors):
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
    TeamSaver.save(bestTeam)
    Outputter.team(bestTeam)

    return fullAffordableTeams.sort(key=lambda x: x.calculatePoints())
