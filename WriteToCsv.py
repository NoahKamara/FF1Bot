import csv
import os
import os.path
from datetime import datetime



def WriteDrivers(drivers):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if not (os.path.isfile("driverStats.csv")):
        with open('driverStats.csv', 'a') as f:
            firstLine = ["DATE"]
            drivers.sort(key=lambda x: x.name)
            for d in drivers:
                firstLine.append(d.name)
            f.write(';'.join(map(str, firstLine)))
        with open('driverStats.csv', 'a') as f:
            line = [dt_string]
            drivers.sort(key=lambda x: x.name)
            for d in drivers:
                line.append(d.points)
            f.write("\n"+";".join(map(str, line)))
    else:
        with open('driverStats.csv', 'a') as f:
            line = [dt_string]
            drivers.sort(key=lambda x: x.name)
            for d in drivers:
                line.append(d.points)
            f.write("\n"+";".join(map(str, line)))

