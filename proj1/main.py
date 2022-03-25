import pandas as pd
import matplotlib.pyplot as plt


def matt1():
    years = pd.read_csv('query/matt1.csv')

    print(years)

    fig, ax = plt.subplots()

    x = years['YEAR'].tolist()
    y = years['TOTAL'].tolist()

    x = [float(i.replace("'", "")) for i in x]
    y = [float(i.replace("'", "")) for i in y]

    ax.set(title="US citizen deaths per year", xlabel="Year", ylabel="deaths")

    ax.plot(x, y)

    plt.show()


def corinne1():

    data = pd.read_csv('query/corinne1.csv')

    x = data['COUNTRY']
    y = data['TOTALSUCCESS']

    fig, ax = plt.subplots()

    ax.set(title="Attacks per Terrorist Country", xlabel="Country", ylabel="Number of Attacks")
    ax.bar(x, y)

    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    print(data)


def corinne3():

    data = pd.read_csv('query/corinne3.csv')

    year = data['year'].tolist()
    t = data['T'].tolist()

    attacks = {y: {1: 0, 0: 0} for (y) in year}

    for x, y in zip(year, t):
        attacks[x][y] += 1

    pos = [(i, v[1]) for i, v in attacks.items()]
    neg = [(i, v[0]) for i, v in attacks.items()]

    fig, ax = plt.subplots()
    ax.set(title='Taliban Attacks Over Time', xlabel="Year", ylabel="Number of Attacks",)

    ax.bar([i[0] for i in neg], [i[1] for i in neg], label='failed', bottom=[i[1] for i in pos])
    ax.bar([i[0] for i in pos], [i[1] for i in pos], label='successful')

    ticks = [2000, 2005, 2010, 2015, 2020]
    plt.xticks(ticks, ticks)
    ax.legend()
    plt.show()

    print(data)


def corinne4():

    data = pd.read_csv('query/corinne4.csv')

    years = data['YEAR'].tolist()
    methods = data['ATTACKMETHOD'].tolist()

    attacks = {m: {y: 0 for y in set(years)} for m in set(methods)}

    for i, j in zip(methods, years):
        attacks[i][j] = attacks.get(i, 0).get(j, 0) + 1

    fig, ax = plt.subplots(figsize=(10, 7))

    del attacks['0']
    del attacks['1']

    for m in attacks.keys():
        print(m)
        x, y = zip(*attacks[m].items())
        ax.plot(x, y, label=m)

    ax.set(title='Terrorist Methods Over Time', xlabel="Year", ylabel="Attack Frequency")
    ax.legend()
    plt.tight_layout()
    plt.show()


corinne4()
