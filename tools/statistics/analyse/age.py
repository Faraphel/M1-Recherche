from collections import Counter

import matplotlib.pyplot as plt

from tools.statistics import extract


def analyse(datas: list[dict]):
    ages_data = list(map(extract.age.extract, datas))

    counter = Counter(ages_data)
    x = list(counter.keys())
    y = list(counter.values())

    # prepare plotting
    figure: plt.Figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    axes.set_title("Nombre de personne par âge")

    # bar chart
    axes.bar(x, y)

    plt.show(block=True)
