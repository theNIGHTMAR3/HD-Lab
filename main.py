import csv
import random
from datetime import datetime, timedelta

import pandas as pd
import time

from classes.Driver import Driver
from classes.Malfunction import Malfunction
from classes.MalfunctionSheet import MalfunctionSheet
from classes.Route import Route
from classes.Station import Station
from classes.Train import Train
from classes.TrainRun import TrainRun
from classes.TrainRunSheet import TrainRunSheet

cities = ["Gdańsk", "Warszawa", "Kraków", "Bydgoszcz", "Poznań", "Wrocław", "Białystok", "Szczecin"]
names = ["Adam", "Michał", "Krzysztof", "Alicja", "Marcel", "Mikołaj"]
surnames = ["Kowalski", "Nowak", "Stachura", "Nazar", "Kuprianowicz", "Jacyno"]
genders = ["Mężczyzna", "Kobieta"]
station_names = ["Główny", "Leśny", "Miasto", "Wschód", "Północ"]
train_types = ["Intercity", "Regio", "Arriva", "EIP", "SKM"]

issue_cause = ["Awaria silnika", "Zniszczone tory", "Awaria klimatyzacji"]

cargo_type = ["Elektronika", "Węgiel", "Paliwo", "Poczta"]


# from https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

# generates random delay for trainRun. 20% for delay not appearing, 80% for delay 0:01 - 2:59 equally distributed
def generateTimeDelta():
    hours = 0
    minutes = 0
    delay = random.randint(1, 10)
    if delay > 2:
        hours = random.randint(0, 2)
        minutes = random.randint(1, 59)
    return hours, minutes


def printDFFromDF(filename):
    newdf = pd.read_csv("generated_data/" + filename, index_col=False)
    print(newdf.to_string(index=False))
    print("\n\n")


def generatePESEL():
    result = ""
    for i in range(11):
        number = random.randint(0, 9)
        result += str(number)
    return result


def generateDrivers(multiplier, time):
    drivers = []
    for i in range(5 * multiplier):
        PESEL = generatePESEL()
        name = random.choice(names)
        surname = random.choice(surnames)
        gender = ""
        if name[-1] == 'a':
            gender = "Kobieta"
        else:
            gender = "Mężczyzna"
        drivers.append(Driver(PESEL, name, surname, gender))

    driversDF = pd.DataFrame.from_records([d.to_dict() for d in drivers])
    driversDF.to_csv("generated_data/drivers", index=False)

    newdf = pd.read_csv("generated_data/drivers", index_col=False)
    print(newdf.to_string(index=False))
    print("\n\n")

    return drivers


def generateStations(multiplier, time):
    stations = []
    for i in range(10 * multiplier):
        id = i
        name = str(random.choice(cities) + ' ' + random.choice(station_names))
        city = random.choice(cities)
        stations.append(Station(id, name, city))

    stationsDF = pd.DataFrame.from_records([d.to_dict() for d in stations])
    stationsDF.to_csv("generated_data/stations", index=False)
    newdf = pd.read_csv("generated_data/stations", index_col=False)
    print(newdf.to_string(index=False))
    print("\n\n")
    return stations


def generateTrains(multiplier, time):
    trains = []
    for i in range(10 * multiplier):
        id = i
        type = random.choice(train_types)
        carts = random.randint(2, 20)
        seats = random.randint(10, carts * 80)
        capacity = random.randint(1000, carts * 1000)
        trains.append(Train(id, type, carts, seats, capacity))

    trainsDF = pd.DataFrame.from_records([d.to_dict() for d in trains])
    trainsDF.to_csv("generated_data/trains", index=False)
    newdf = pd.read_csv("generated_data/trains", index_col=False)
    print(newdf.to_string(index=False))
    print("\n\n")
    return trains


def generateRoutes(multiplier, time, stations):
    routes = []
    for i in range(10 * multiplier):
        id = i
        randomStation = random.choice(stations)
        id_station_start = randomStation.id
        copy_list = stations.copy()
        copy_list.remove(randomStation)
        id_station_end = random.choice(copy_list).id

        # TODO: calculate distance based on longitude and latitude
        distance = random.randint(10, 1000)
        routes.append(Route(id, id_station_start, id_station_end, distance))

    routesDF = pd.DataFrame.from_records([d.to_dict() for d in routes])
    routesDF.to_csv("generated_data/routes", index=False)
    newdf = pd.read_csv("generated_data/routes", index_col=False)
    print(newdf.to_string(index=False))
    print("\n\n")
    return routes


def generateTrainRuns(multiplier, time, trains, routes, drivers):
    trainRuns = []
    dateTimeFormat = '%m/%d/%Y %I:%M %p'

    # TODO: solbe the types problelm
    # https://bobbyhadz.com/blog/python-add-time-to-datetime-object
    
    for i in range(50 * multiplier):
        id = i
        planned_departure = random_date("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random())
        date_time_obj = datetime.strptime(planned_departure, dateTimeFormat)
        # planned train run takes 2 to 8 hours
        planned_arrival_min = date_time_obj + timedelta(hours=2, minutes=0, seconds=0)
        planned_arrival_max = date_time_obj + timedelta(hours=8, minutes=0, seconds=0)
        planned_arrival = random_date(str(planned_arrival_min), str(planned_arrival_max), random.random())

        date_time_obj = datetime.strptime(planned_departure, dateTimeFormat)
        # TODO: types of delay(departure, arrival)
        delayHours, delayMinutes = generateTimeDelta()
        real_departure = date_time_obj + timedelta(hours=delayHours, minutes=delayMinutes, seconds=0)

        date_time_obj = datetime.strptime(planned_arrival, dateTimeFormat)
        delayHours, delayMinutes = generateTimeDelta()
        real_arrival = date_time_obj + timedelta(hours=delayHours, minutes=delayMinutes, seconds=0)

        id_train = random.choice(trains).id
        id_route = random.choice(routes).id
        PESEL = random.choice(drivers).PESEL
        trainRuns.append(TrainRun(id, planned_departure, planned_arrival, real_departure, real_arrival, id_train,
                                  id_route, PESEL))

    trainRunsDF = pd.DataFrame.from_records([d.to_dict() for d in trainRuns])
    trainRunsDF.to_csv("generated_data/trainRuns", index=False)
    newdf = pd.read_csv("generated_data/trainRuns", index_col=False)
    print(newdf.to_string(index=False))
    print("\n\n")
    return trainRuns


def generateMalfunctions(multiplier, time, trainRuns):
    malfunctions = []
    malfunctionsSheet = []
    for i in range(5 * multiplier):
        id = i
        train_run = random.choice(trainRuns).id
        # TODO: set the range of random dates based on @time parameter
        date = random_date("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random())
        repaired = bool(random.getrandbits(1))
        cause = random.choice(issue_cause)

        malfunctions.append(Malfunction(id, train_run, date, repaired))
        malfunctionsSheet.append(MalfunctionSheet(id, train_run, date, repaired, cause))

    malfunDF = pd.DataFrame.from_records([m.to_dict() for m in malfunctions])
    malfunsheetDF = pd.DataFrame.from_records([m.to_dict() for m in malfunctionsSheet])
    malfunDF.to_csv("generated_data/malfunction", index=False)
    malfunsheetDF.to_csv("generated_data/malfunction_sheet", index=False)
    newMalfunDF = pd.read_csv("generated_data/malfunction", index_col=False)
    newMalfunSheetDF = pd.read_csv("generated_data/malfunction_sheet", index_col=False)
    print(newMalfunDF.to_string(index=False))
    print("\n\n")
    print(newMalfunSheetDF.to_string(index=False))
    print("\n\n")


def generateData(multiplier, time):
    drivers = generateDrivers(multiplier, time)
    stations = generateStations(multiplier, time)
    trains = generateTrains(multiplier, time)
    routes = generateRoutes(multiplier, time, stations)

    trainRuns = generateTrainRuns(multiplier, time, trains, routes, drivers)

    generateMalfunctions(multiplier, time, trainRuns)


if __name__ == '__main__':
    generateData(1, "t0")
