import pandas as pd


def generateTime():
    hours = []
    for g in range(24):
        for m in range(60):
            hours.append(g)

    minutes = []
    for g in range(24):
        for m in range(60):
            minutes.append(m)

    d = {'godzina': hours, 'minuta': minutes}
    timeset = pd.DataFrame(data=d)

    return timeset


if __name__ == '__main__':
    timeset = generateTime()
    timeset.to_csv("Czas_tabela.csv", index=False)
