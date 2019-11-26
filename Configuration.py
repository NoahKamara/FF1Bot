import os.path
import pickle
import PySimpleGUI as sg
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
    config = loadConfig()
    auth = config.auth
    window = sg.Window("Account", [[sg.Button("new account"), sg.Button(auth.login)]])
    event, values = window.read()
    window.close()
    if event == "new account":
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
    x = sg.Window("Enter your login Credentials:", [[sg.T("Email:"),sg.I(), sg.T("Password:"),sg.I(password_char="*"),sg.Submit()]])
    _,values = x.read()
    # print("Enter your login Credentials:")
    # login = input("Email:    ")
    # password = input("Password: ")
    cred = AuthCred(values[0], values[1])
    config = Configuration(cred)
    saveConfig(config)
    x.close()
    