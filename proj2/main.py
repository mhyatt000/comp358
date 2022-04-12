import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def matt1():

    data = pd.read_csv('query/CustomerIDPurchases.csv')
    data = data.fillna(0)

    age = data['c.age'].tolist()
    num_purchases = data['num_purchases'].tolist()

    fig, ax = plt.subplots()

    ax.set(title="Number of Customer Purchases", xlabel="Purchases", ylabel="Frequency")

    ax.hist(num_purchases, bins=100)

    ax.set_yscale('log')
    # ax.set_xscale('log')

    plt.show()


def matt2():

    data = pd.read_csv('query/ProductPurchases.csv')
    data = data.fillna(0)

    name = data['a.product_type_name'].tolist()
    num_purchases = data['num_purchases'].tolist()

    all_purchases = sum(num_purchases)
    ppercent = [100*n/all_purchases for n in num_purchases]

    cutoff = 3
    others = sum([pp < cutoff for pp in ppercent])
    products = {n: pp for n, pp in zip(name, ppercent) if pp > cutoff}
    products[f'{others} others'] = sum([pp for pp in ppercent if pp < cutoff])

    print(products)

    fig, ax = plt.subplots()
    ax.pie(products.values(), labels=products.keys(),
           autopct='%1.1f%%', startangle=90, pctdistance=0.85)

    ax.set(title="Popular Clothing Items")

    plt.show()


# def corinne1():
#
#     data = pd.read_csv('query/corinne1.csv')
#
#     x = data['COUNTRY']
#     y = data['TOTALSUCCESS']
#
#     fig, ax = plt.subplots()
#
#     ax.set(title="Attacks per Terrorist Country", xlabel="Country", ylabel="Number of Attacks")
#     ax.bar(x, y)
#
#     plt.xticks(rotation=30)
#     plt.tight_layout()
#     plt.show()
#
#     print(data)
#
#
# def corinne3():
#
#     data = pd.read_csv('query/corinne3.csv')
#
#     year = data['year'].tolist()
#     t = data['T'].tolist()
#
#     attacks = {y: {1: 0, 0: 0} for (y) in year}
#
#     for x, y in zip(year, t):
#         attacks[x][y] += 1
#
#     pos = [(i, v[1]) for i, v in attacks.items()]
#     neg = [(i, v[0]) for i, v in attacks.items()]
#
#     fig, ax = plt.subplots()
#     ax.set(title='Taliban Attacks Over Time', xlabel="Year", ylabel="Number of Attacks",)
#
#     ax.bar([i[0] for i in neg], [i[1] for i in neg], label='failed', bottom=[i[1] for i in pos])
#     ax.bar([i[0] for i in pos], [i[1] for i in pos], label='successful')
#
#     ticks = [2000, 2005, 2010, 2015, 2020]
#     plt.xticks(ticks, ticks)
#     ax.legend()
#     plt.show()
#
#     print(data)
#
#
# def corinne4():
#
#     data = pd.read_csv('query/corinne4.csv')
#
#     years = data['YEAR'].tolist()
#     methods = data['ATTACKMETHOD'].tolist()
#
#     attacks = {m: {y: 0 for y in set(years)} for m in set(methods)}
#
#     for i, j in zip(methods, years):
#         attacks[i][j] = attacks.get(i, 0).get(j, 0) + 1
#
#     fig, ax = plt.subplots(figsize=(10, 7))
#
#     del attacks['0']
#     del attacks['1']
#
#     for m in attacks.keys():
#         print(m)
#         x, y = zip(*attacks[m].items())
#         ax.plot(x, y, label=m)
#
#     ax.set(title='Terrorist Methods Over Time', xlabel="Year", ylabel="Attack Frequency")
#     ax.legend()
#     plt.tight_layout()
#     plt.show()
#
#
matt1()
