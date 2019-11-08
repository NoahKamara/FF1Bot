import os.path
import pickle

from selenium import webdriver
from DriversAndConstructors import GetDriversAndConstructors

import FormulaDatabase
from DriversAndConstructors import GetDriversAndConstructors
from TeamGenerator import makeBestTeamListUnder100M
from TeamStatRefresh import refreshTeam
from ChangeProposer import proposeChange
import TeamSaver
from Configuration import isFirstTimeLaunch, loadConfig, saveConfig, AuthCred, Configuration, performSetup
from TeamManager import createNewTeam, changeTeamMember

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


# FormulaDatabase.insertDrivers(drivers)

if __name__ == '__main__':
    if isFirstTimeLaunch():
        performSetup()
    config = loadConfig()
    auth = config.auth
    drivers, constructors = GetDriversAndConstructors(auth.login, auth.password, webdriver.Chrome())
    FormulaDatabase.insertDrivers(drivers)
    if not (os.path.exists('team.pkl')):
        makeBestTeamListUnder100M(drivers, constructors)
        team = TeamSaver.load()
        createNewTeam(team)
    else:
        formerTeam = TeamSaver.load()
        refreshTeam(drivers, constructors)
        proposedTeam = proposeChange(drivers, constructors)
        new = None
        for driver in proposedTeam.drivers:
            if not (driver in formerTeam.drivers):
                newDriver = driver
                break

        old = None
        for driver in formerTeam.drivers:
            if not (driver in proposedTeam.drivers):
                oldDriver = driver
                break
        if (old == None) or (new == None):
            new = formerTeam.constructor
            old = proposedTeam.constructor

        if not ((old == None) or (new == None) or (old.name == new.name)):
            changeTeamMember(old, new)
