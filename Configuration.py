import os.path
import pickle

class AuthCred:
    def __init__(self, login, password):
        self.login = login
        self.password = password

class Configuration:
    def __init__(self, auth):
        self.auth = auth

def isFirstTimeLaunch():
    if not (os.path.exists('config.pkl')):
        return True
    else:
        return False

def loadConfig():
    with open("config.pkl", 'rb') as f:
        return pickle.load(f)

def saveConfig(config):
    with open("config.pkl", 'wb') as f:
        pickle.dump(config, f, pickle.HIGHEST_PROTOCOL)

def performSetup():
    print("Enter your login Credentials:")
    login = input("Email:    ")
    password = input("Password: ")
    cred = AuthCred(login, password)
    config = Configuration(cred)
    saveConfig(config)