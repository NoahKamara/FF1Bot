import os.path
import pickle

import FormulaDatabase
from DriversAndConstructors import GetDriversAndConstructors
from TeamGenerator import GenerateFrom


class AuthCred:
    def __init__(self, login, password):
        self.login = login
        self.password = password


def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


login = ""
password = ""
cred = AuthCred("", "")
if not (os.path.isfile("authCred.pkl")):
    print("Enter your login Credentials:")
    login = input("Email:    ")
    password = input("Password: ")
    cred = AuthCred(login, password)
    save_obj(cred, "authCred")
else:
    cred = load_obj("authCred")
drivers, constructors = GetDriversAndConstructors(cred.login, cred.password)

print("DRIVERS: " + str(len(drivers)) + "\t CONSTRUCTORS: " + str(len(constructors)))
FormulaDatabase.insertDrivers(drivers)
GenerateFrom(drivers, constructors)
