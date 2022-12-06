import csv
import random
from datetime import datetime, timedelta

import pandas as pd

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
train_types = ["Intercity", "Regionalny", "Arriva", "EIP", "SKM"]

issue_cause = ["Awaria silnika", "Zniszczone tory", "Awaria klimatyzacji"]

cargo_type = ["Elektronika", "Węgiel", "Paliwo", "Poczta"]

timeSets = []


def randomDateNew(start_date, end_date):
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date


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


# from https://pl.python.org/forum/index.php?topic=10389.0
def generatePESEL():
    year = random.randint(1950, 2010)

    if year <= 1999:
        month = random.randint(1, 12)
    elif year >= 2000:
        month = random.randint(1, 12) + 20  # to distinguish between centuries

    # I need to put months in a category to choose correct range of possible days for each one
    odd_months = (1, 3, 5, 7, 8, 10, 12, 21, 23, 25, 27, 28, 30, 32)
    even_months = (4, 6, 9, 11, 24, 26, 29, 31)

    if month in odd_months:
        day = random.randint(1, 31)

    elif month in even_months:
        day = random.randint(1, 30)
        # this is for february
    else:
        if year % 4 == 0 and year != 1900:
            day = random.randint(1, 29)  # leap year

        else:
            day = random.randint(1, 28)  # usual year

    four_random = random.randint(1000, 9999)
    four_random = str(four_random)

    # here comes the equation part, it calculates the last digit

    y = '%02d' % (year % 100)
    m = '%02d' % month
    dd = '%02d' % day

    a = y[0]
    a = int(a)

    b = y[1]
    b = int(b)

    c = m[0]
    c = int(c)

    d = m[1]
    d = int(d)

    e = dd[0]
    e = int(e)

    f = dd[1]
    f = int(f)

    g = four_random[0]
    g = int(g)

    h = four_random[1]
    h = int(h)

    i = four_random[2]
    i = int(i)

    j = four_random[3]
    j = int(j)

    check = a + 3 * b + 7 * c + 9 * d + e + 3 * f + 7 * g + 9 * h + i + 3 * j

    last_digit = 0

    if not check % 10 == 0:
        last_digit = 10 - (check % 10)

    result = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j) + str(last_digit)
    return result


def saveListToCSV(list_of_elements, filename):
    DataFrame_save = pd.DataFrame.from_records([d.to_dict() for d in list_of_elements])
    DataFrame_save.to_csv(filename, index=False)


def readListFromCSV(filename):
    DataFrame_read = pd.read_csv(filename, index_col=False)
    print(DataFrame_read.to_string(index=False))
    print("\n\n")


def generateDrivers(multiplier, time):
    drivers = []
    dataSize = 5 * multiplier
    for j in range(time + 1):
        for i in range(dataSize):
            PESEL = generatePESEL()
            name = random.choice(names)
            surname = random.choice(surnames)
            gender = ""
            if name[-1] == 'a':
                gender = "Kobieta"
            else:
                gender = "Mężczyzna"
            drivers.append(Driver(PESEL, name, surname, gender))

        driversDF_save = pd.DataFrame.from_records([d.to_dict() for d in drivers])
        driversDF_save.to_csv("generated_data/drivers" + str(j), index=False)

        newdf_read = pd.read_csv("generated_data/drivers" + str(j), index_col=False)
        print(newdf_read.to_string(index=False))
        print("\n\n")

    return drivers


def generateStations(multiplier, time):
    stations = []
    dataSize = 10 * multiplier

    start_date = timeSets[0][0]
    end_date = timeSets[2][1]

    for j in range(time + 1):
        for i in range(dataSize):
            id = i + j * dataSize
            name = str(random.choice(cities) + ' ' + random.choice(station_names))
            city = random.choice(cities)

            in_renovation = bool(random.getrandbits(1))

            station_start_date = start_date
            station_end_date = end_date

            renovation_start_date = start_date

            # SCD2
            chance_of_scd2 = random.randint(0, 100)
            if chance_of_scd2 < 10:
                renovation_start_date = randomDateNew(station_start_date, station_end_date)
                stations.append(Station(id, name, city, in_renovation, start_date, renovation_start_date, False))
                stations.append(Station(id, name, city, in_renovation, renovation_start_date, end_date, True))
            else:
                stations.append(Station(id, name, city, in_renovation, start_date, end_date, True))

        filename = "generated_data/stations" + str(j)
        saveListToCSV(stations, filename)
        readListFromCSV(filename)

    return stations


def generateTrains(multiplier, time):
    trains = []
    dataSize = 10 * multiplier
    for j in range(time + 1):
        for i in range(dataSize):
            id = i + j * dataSize
            type = random.choice(train_types)
            carts = random.randint(2, 20)
            seats = random.randint(10, carts * 80)
            capacity = random.randint(1000, carts * 1000)
            trains.append(Train(id, type, seats, capacity))

        filename = "generated_data/trains" + str(j)
        saveListToCSV(trains, filename)
        readListFromCSV(filename)

    return trains


def generateRoutes(multiplier, time, stations):
    routes = []
    dataSize = 10 * multiplier
    for j in range(time + 1):
        for i in range(dataSize):
            id = i + j * dataSize
            randomStation = random.choice(stations)
            id_station_start = randomStation.id
            copy_list = stations.copy()
            copy_list.remove(randomStation)
            id_station_end = random.choice(copy_list).id

            # TODO: calculate distance based on longitude and latitude
            distance = random.randint(10, 1000)
            routes.append(Route(id, id_station_start, id_station_end, distance))

        filename = "generated_data/routes" + str(j)
        saveListToCSV(routes, filename)
        readListFromCSV(filename)

    return routes


def generateTrainRuns(multiplier, time, trains, routes, drivers):
    trainRuns = []
    trainRunsSheet = []
    dataSize = 20 * multiplier
    for j in range(time + 1):
        start_date = timeSets[j][0]
        end_date = timeSets[j][1]
        for i in range(dataSize):
            id = i + j * dataSize

            planned_departure = randomDateNew(start_date, end_date)
            # planned train run takes 2 to 8 hours
            planned_arrival_min = planned_departure + timedelta(hours=2, minutes=0, seconds=0)
            planned_arrival_max = planned_departure + timedelta(hours=8, minutes=0, seconds=0)
            planned_arrival = randomDateNew(planned_arrival_min, planned_arrival_max)

            delayHours, delayMinutes = generateTimeDelta()
            real_departure = planned_departure + timedelta(hours=delayHours, minutes=delayMinutes, seconds=0)

            delayHours, delayMinutes = generateTimeDelta()
            real_arrival = planned_arrival + timedelta(hours=delayHours, minutes=delayMinutes, seconds=0)

            id_train = random.choice(trains).id
            id_route = random.choice(routes).id
            PESEL = random.choice(drivers).PESEL
            trainRuns.append(TrainRun(id, planned_departure, planned_arrival, real_departure, real_arrival, id_train,
                                      id_route, PESEL))

            selected_train = [e for e in trains if e.id == id_train][0]
            train_capacity_max = selected_train.capacity
            items_mass = random.randrange(0, train_capacity_max)
            items_type = random.choice(cargo_type)

            # get the maximum capacity of train
            train_seats_max = selected_train.seats
            train_seats_taken = random.randrange(0, train_seats_max)
            trainRunsSheet.append(TrainRunSheet(id, items_mass, items_type, train_seats_taken))

        filename_1 = "generated_data/trainRuns" + str(j)
        saveListToCSV(trainRuns, filename_1)
        readListFromCSV(filename_1)

        filename_2 = "generated_data/trainRunsSheet" + str(j)
        saveListToCSV(trainRunsSheet, filename_2)
        readListFromCSV(filename_2)

    return trainRuns, trainRunsSheet


def generateMalfunctions(multiplier, time, trainRuns):
    malfunctions = []
    malfunctionsSheet = []
    dataSize = 5 * multiplier
    for j in range(time + 1):
        start_date = timeSets[j][0]
        end_date = timeSets[j][1]
        for i in range(dataSize):
            id = i + j * dataSize
            train_run = random.choice(trainRuns).id
            print("Selected times: ", start_date, end_date)
            date = randomDateNew(start_date, end_date)

            repaired = bool(random.getrandbits(1))
            cause = random.choice(issue_cause)
            reparing_time = random.randint(0, 200)

            malfunctions.append(Malfunction(id, train_run, date, repaired))
            malfunctionsSheet.append(MalfunctionSheet(id, train_run, date, repaired, cause, reparing_time))

        filename_1 = "generated_data/malfunction" + str(j)
        saveListToCSV(malfunctions, filename_1)
        readListFromCSV(filename_1)

        filename_2 = "generated_data/malfunction_sheet" + str(j)
        saveListToCSV(malfunctionsSheet, filename_2)
        readListFromCSV(filename_2)

    return malfunctions, malfunctionsSheet


def generateData(multiplier, time):
    drivers = generateDrivers(multiplier, time)
    stations = generateStations(multiplier, time)
    trains = generateTrains(multiplier, time)
    routes = generateRoutes(multiplier, time, stations)

    trainRuns, trainRunsSheet = generateTrainRuns(multiplier, time, trains, routes, drivers)

    malfunctions, malfunctionsSheet = generateMalfunctions(multiplier, time, trainRuns)


def runMain():
    # stored as pairs of start_date and end_date
    set0 = (datetime(2021, 1, 1), datetime(2021, 6, 30))
    timeSets.append(set0)

    set1 = (datetime(2021, 7, 1), datetime(2021, 12, 31))
    timeSets.append(set1)

    set2 = (datetime(2022, 1, 1), datetime(2022, 6, 30))
    timeSets.append(set2)

    # choose one of the available time modes
    timeMode = 1
    # timeMode = 1
    # timeMode = 2

    # choose one of the available data size multipliers
    dataSizeMultiplier = 1
    # dataSizeMultiplier = 2
    # dataSizeMultiplier = 3

    generateData(dataSizeMultiplier, timeMode)

if __name__ == '__main__':
    # runMain()
    import time

    start_time = time.time()
    for i in range(pow(10,9)):
        a = i*10
    print("--- %s seconds ---" % (time.time() - start_time))

