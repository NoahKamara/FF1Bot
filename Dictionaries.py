class Driver:
  def __init__(self, name, points, price):
    self.name = name
    self.points = points
    self.price = price

class Constructor:
  def __init__(self, name, points, price):
    self.name = name
    self.points = points
    self.price = price

class Team:
    def __init__(self, drivers, constructor):
        self.drivers = drivers
        self.constructor = constructor

    def turboedDriver(self):
        availDrivers = []
        for driver in self.drivers:
            if float(driver.price) <= float(19):
                availDrivers.append(driver)#max(s, key=lambda i: i.arity())
        return max(availDrivers, key=lambda i: float(i.points))

    def calculatePrice(self):
        driverPrice = sum(driver.price for driver in self.drivers)
        completePrice = driverPrice+self.constructor.price
        return completePrice

    def calculatePoints(self):
        driverPoints = sum(driver.points for driver in self.drivers)
        completePoints = driverPoints+self.constructor.points
        return completePoints+self.turboedDriver().points
