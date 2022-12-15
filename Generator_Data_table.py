from datetime import datetime, timedelta


def getMonthName(monthNum):
    if monthNum == 1:
        return "Styczeń"
    elif monthNum == 2:
        return "Luty"
    elif monthNum == 3:
        return "Marzec"
    elif monthNum == 4:
        return "Kwiecień"
    elif monthNum == 5:
        return "Maj"
    elif monthNum == 6:
        return "Czerwiec"
    elif monthNum == 7:
        return "Lipiec"
    elif monthNum == 8:
        return "Sierpień"
    elif monthNum == 9:
        return "Wrzesień"
    elif monthNum == 10:
        return "Październik"
    elif monthNum == 11:
        return "Listopad"
    elif monthNum == 12:
        return "Grudzień"


def getWeekdayName(weekDayName):
    if weekDayName == "Monday":
        return "Poniedziałek"
    elif weekDayName == "Tuesday":
        return "Wtorek"
    elif weekDayName == "Wednesday":
        return "Środa"
    elif weekDayName == "Thursday":
        return "Czwartek"
    elif weekDayName == "Friday":
        return "Piątek"
    elif weekDayName == "Saturday":
        return "Sobota"
    elif weekDayName == "Sunday":
        return "Niedziela"


if __name__ == '__main__':
    yearStart = 2020
    yearEnd = 2022
    currentdate = datetime(yearStart, 1, 1)

    for y in range(yearStart, yearEnd):  # rok
        for d in range(365):
            insertString = 'insert into dbo.Data("Rok", "Miesiąc", "Numer_miesiąca","Dzień", "Dzień_tygodnia", "Numer_dnia_tygodnia") values ('

            insertString += currentdate.strftime("%Y") + ', '
            insertString += "'" + getMonthName(int(currentdate.strftime("%m"))) + "'" + ', '
            insertString += currentdate.strftime("%m") + ', '
            insertString += currentdate.strftime("%d") + ', '
            insertString += "'" + getWeekdayName(currentdate.strftime("%A")) + "'" + ', '
            weekDayNum = int(currentdate.strftime("%w"))
            if weekDayNum == 0: weekDayNum = 7
            insertString += str(weekDayNum)
            insertString += ');'
            print(insertString)
            currentdate += timedelta(days=1)

