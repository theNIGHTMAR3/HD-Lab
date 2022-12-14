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

cities = ["Gdansk", "Warszawa", "Krakow", "Bydgoszcz", "Poznan", "Wroclaw", "Bialystok", "Szczecin", "Mielno"]
names = ["Adam", "Michal", "Krzysztof", "Alicja", "Marcel", "Mikolaj"]
surnames = ["Kowalski", "Nowak", "Stachura", "Nazar", "Kuprianowicz", "Jacyno"]
genders = ["Mezczyzna", "Kobieta"]
station_names = ["Glowny", "Lesny", "Miasto", "Wschod", "Zachod", "Polnoc", "Poludnie"]
train_types = ["Intercity", "Regionalny", "Arriva", "EIP", "SKM"]

issue_cause = ["Awaria silnika", "Zniszczone tory", "Awaria klimatyzacji"]

cargo_types = ["Elektronika", "Wegiel", "Paliwo", "Poczta"]

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
    newdf = pd.read_csv("generated_data_task_5/" + filename, index_col=False)
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


def generateDrivers(multiplier, time):
    drivers = []
    dataSize = 1 * multiplier
    for j in range(time + 1):
        for i in range(dataSize):
            PESEL = generatePESEL()
            name = random.choice(names)
            surname = random.choice(surnames)
            gender = ""
            if name[-1] == 'a':
                gender = "Kobieta"
            else:
                gender = "Mezczyzna"
            drivers.append(Driver(PESEL, name, surname, gender))

        driversDF = pd.DataFrame.from_records([d.to_dict() for d in drivers])
        driversDF.to_csv("generated_data_task_5/drivers" + str(j) + ".csv", index=False)
        print(driversDF.head())
        # newdf = pd.read_csv("generated_data_task_5/drivers" + str(j), index_col=False)
        # print(newdf.to_string(index=False))
        # print("\n\n")

    return drivers


def generateStations(multiplier, time):
    used_enc = 'utf-8'
    stations = []
    dataSize = 1 * multiplier
    # for j in range(time + 1):
    for i in range(dataSize):
        id = i + 1
        city = str(cities[i])
        name = str(city + ' ' + random.choice(station_names))
        renovation_year = random.randint(1900, 2020)
        stations.append(Station(id, name, city, renovation_year))

    stationsDF = pd.DataFrame.from_records([d.to_dict() for d in stations])
    stationsDF.to_csv("generated_data_task_5/stations" + str(0) + ".csv", index=False, encoding=used_enc)
    print(stationsDF.head())

    selected = random.sample(stations, int(100))
    stations2 = []

    for s in selected:
        stations2.append(Station(s.id, s.station_name, s.city, s.renovation_year + 1))

    stationsDF = pd.DataFrame.from_records([d.to_dict() for d in stations2])
    stationsDF.to_csv("generated_data_task_5/stations" + str(1) + ".csv", index=False, encoding=used_enc)

    # newdf = pd.read_csv("generated_data_task_5/stations" + str(j), index_col=False)
    # print(newdf.to_string(index=False))
    # print("\n\n")
    return stations


def generateTrains(multiplier, time):
    trains = []
    dataSize = 1 * multiplier
    for j in range(time + 1):
        for i in range(dataSize):
            id = i + j * dataSize + 1
            type = random.choice(train_types)
            cargo_type = random.choice(cargo_types)
            # carts = random.randint(2, 20)
            # seats = random.randint(10, carts * 80)
            # capacity = random.randint(1000, carts * 1000)
            trains.append(Train(id, type, cargo_type))

        trainsDF = pd.DataFrame.from_records([d.to_dict() for d in trains])
        trainsDF.to_csv("generated_data_task_5/trains" + str(j) + ".csv", index=False)
        print(trainsDF.head())
        # newdf = pd.read_csv("generated_data_task_5/trains" + str(j), index_col=False)
        # print(newdf.to_string(index=False))
        # print("\n\n")
    return trains


def generateRoutes(multiplier, time, stations):
    routes = []
    dataSize = 1 * multiplier
    for j in range(time + 1):
        for i in range(dataSize):
            id = i + j * dataSize + 1
            randomStation = random.choice(stations)
            id_station_start = randomStation.id
            copy_list = stations.copy()
            copy_list.remove(randomStation)
            id_station_end = random.choice(copy_list).id
            distance = random.randint(10, 1000)
            routes.append(Route(id, id_station_start, id_station_end, distance))

        routesDF = pd.DataFrame.from_records([d.to_dict() for d in routes])
        routesDF.to_csv("generated_data_task_5/routes" + str(j) + ".csv", index=False)
        print(routesDF.head())
        # newdf = pd.read_csv("generated_data_task_5/routes" + str(j), index_col=False)
        # print(newdf.to_string(index=False))
        # print("\n\n")
    return routes


def generateTrainRuns(multiplier, time, trains, routes, drivers):
    trainRuns = []
    trainRunsSheet = []
    dataSize = 1 * multiplier
    for j in range(time + 1):
        begin_date = timeSets[j][0]
        end_date = timeSets[j][1]
        for i in range(dataSize):
            id = i + j * dataSize + 1

            planned_departure = randomDateNew(begin_date, end_date)
            # planned train run takes 2 to 8 hours
            planned_arrival_min = planned_departure + timedelta(hours=2, minutes=0, seconds=0)
            planned_arrival_max = planned_departure + timedelta(hours=8, minutes=0, seconds=0)
            planned_arrival = randomDateNew(planned_arrival_min, planned_arrival_max)

            delayHours, delayMinutes = generateTimeDelta()
            real_departure = planned_departure + timedelta(hours=delayHours, minutes=delayMinutes, seconds=0)

            delayHours, delayMinutes = generateTimeDelta()
            real_arrival = planned_arrival + timedelta(hours=delayHours, minutes=delayMinutes, seconds=0)
            delayInMinutes = delayHours * 60 + delayMinutes

            id_train = random.randint(1, dataSize-1)
            id_route = random.randint(1, dataSize - 1)
            driver_id = random.randint(1, dataSize - 1)
            trainRuns.append(TrainRun(id, planned_departure, planned_arrival, real_departure,
                                      real_arrival, id_train, id_route, driver_id))

            selected_train = [e for e in trains if e.id == id_train][0]
            capacity = random.randint(100, 5000)
            items_mass = random.randrange(0, capacity)
            items_type = random.choice(cargo_types)
            # get the maximum capacity of train
            train_seats_max = random.randint(500, 1000)
            train_seats_taken = random.randrange(0, train_seats_max)

            if_malfunction_happened = random.randint(0, 1)  # bool

            trainRunsSheet.append(TrainRunSheet(id, items_mass, train_seats_taken, train_seats_max, capacity, driver_id,
                                                real_arrival, delayInMinutes, if_malfunction_happened))

        trainRunsDF = pd.DataFrame.from_records([d.to_dict() for d in trainRuns])
        trainRunsSheetDF = pd.DataFrame.from_records([d.to_dict() for d in trainRunsSheet])
        trainRunsDF.to_csv("generated_data_task_5/trainRuns" + str(j) + ".csv", index=False)
        trainRunsDF.to_excel("generated_data_task_5/trainRuns" + str(j) + ".xlsx", index=False)
        trainRunsSheetDF.to_csv("generated_data_task_5/trainRunsSheet" + str(j) + ".csv", index=False)
        trainRunsSheetDF.to_csv("generated_data_task_5/trainRunsSheet" + str(j) + ".xlsx", index=False)
        # print(trainRunsDF.head())
        # print(trainRunsSheetDF.head())

        # newdf = pd.read_csv("generated_data_task_5/trainRuns" + str(j), index_col=False)
        # newdfSheet = pd.read_csv("generated_data_task_5/trainRunsSheet" + str(j), index_col=False)
        # print(newdf.to_string(index=False))
        # print("\n")
        # print(newdfSheet.to_string(index=False))
        # print("\n\n")

    return trainRuns, trainRunsSheet


def generateMalfunctions(multiplier, time, trainRuns):
    malfunctions = []
    malfunctionsSheet = []
    dataSize = 1 * multiplier
    for j in range(time + 1):
        begin_date = timeSets[j][0]
        end_date = timeSets[j][1]
        for i in range(dataSize):
            id = i + j * dataSize + 1
            train_run = random.randint(1,dataSize-1)
            # print("Selected times: ", begin_date, end_date)
            date = randomDateNew(begin_date, end_date)

            repaired = random.randint(0, 1)
            repairing_time = random.randint(10, 200)

            malfunctions.append(Malfunction(id, train_run, date))
            malfunctionsSheet.append(MalfunctionSheet(id, train_run, date, repaired, repairing_time))

        malfunDF = pd.DataFrame.from_records([m.to_dict() for m in malfunctions])
        malfunsheetDF = pd.DataFrame.from_records([m.to_dict() for m in malfunctionsSheet])
        malfunDF.to_csv("generated_data_task_5/malfunction" + str(j) + ".csv", index=False)
        malfunDF.to_excel("generated_data_task_5/malfunction" + str(j) + ".xlsx", index=False)

        malfunsheetDF.to_csv("generated_data_task_5/malfunction_sheet" + str(j) + ".csv", index=False)
        malfunsheetDF.to_excel("generated_data_task_5/malfunction_sheet" + str(j) + ".xlsx", index=False)
        print(malfunDF.head())
        print(malfunsheetDF.head())

        # newMalfunDF = pd.read_csv("generated_data_task_5/malfunction" + str(j), index_col=False)
        # newMalfunSheetDF = pd.read_csv("generated_data_task_5/malfunction_sheet" + str(j), index_col=False)
        # print(newMalfunDF.to_string(index=False))
        # print("\n\n")
        # print(newMalfunSheetDF.to_string(index=False))
        # print("\n\n")
    return malfunctions, malfunctionsSheet


def generateData(multiplier, time):
    drivers = generateDrivers(multiplier, time)
    stations = generateStations(multiplier, time)
    trains = generateTrains(multiplier, time)
    routes = generateRoutes(multiplier, time, stations)

    trainRuns, trainRunsSheet = generateTrainRuns(multiplier, time, trains, routes, drivers)

    malfunctions, malfunctionsSheet = generateMalfunctions(multiplier, time, trainRuns)


def getNamesOfCities(filename):
    df = pd.read_csv(filename, sep=";", encoding='utf-8')
    df['city_name'] = df['nazwa miasta'].str.lower() + ' ' + df['nazwa wojew??dztwa'].str.lower()

    # replace polish special letters
    df['city_name'] = df['city_name'].str.replace('??', 's')
    df['city_name'] = df['city_name'].str.replace('??', 'z')
    df['city_name'] = df['city_name'].str.replace('??', 'z')
    df['city_name'] = df['city_name'].str.replace('??', 'a')
    df['city_name'] = df['city_name'].str.replace('??', 'e')
    df['city_name'] = df['city_name'].str.replace('??', 'c')
    df['city_name'] = df['city_name'].str.replace('??', 'o')
    df['city_name'] = df['city_name'].str.replace('??', 'l')
    df['city_name'] = df['city_name'].str.replace('??', 'n')

    return df['city_name']


if __name__ == '__main__':
    # stored as pairs of BeginDate and EndDate
    set0 = (datetime(2021, 1, 1), datetime(2021, 6, 30))
    timeSets.append(set0)

    set1 = (datetime(2021, 7, 1), datetime(2021, 12, 31))
    timeSets.append(set1)

    set2 = (datetime(2022, 1, 1), datetime(2022, 6, 30))
    timeSets.append(set2)

    # time modes available: 0, 1, 2
    # timeMode = 0
    # timeMode = 1
    timeMode = 2

    # number of rows in datasheet = 100 * dataSizeMultiplier * (timeMode + 1)
    # for example: 1000 rows for dataSizeMultiplier = 10
    dataSizeMultiplier = 1000
    # dataSizeMultiplier = 2
    # dataSizeMultiplier = 3

    cities = getNamesOfCities("cities.csv")

    generateData(len(cities), timeMode)

    # data = {
    #     "Godzina": [1, 2, 3],
    #     "Minuta": [4, 5, 6]
    # }
    #
    # # load data into a DataFrame object:
    # df = pd.DataFrame(data)
    #
    # df.to_csv('test_time.csv', index=False)
    # print(df.head())
