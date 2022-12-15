if __name__ == '__main__':

    for h in range(24):
        for m in range(60):
            currentHour = 'insert into dbo.Czas("Godzina", Minuta) values ('
            currentHour += str(h) + ', '
            currentHour += str(m)
            currentHour += ");"
            print(currentHour)

            # insert into dbo.Czas("Godzina", Minuta) values (0, 0);
