import requests
import json
from unidecode import unidecode  # can tai pip install unicode
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import sys

# sys.stdin.reconfigure(encoding='utf-8')
# sys.stdout.reconfigure(encoding='utf-8')


# def updateDB(graph,news):


def draw7daysChart(x):
    data = eval(x)
    df = pd.json_normalize(data["overview"])
    ax = df.plot.bar(
        x="date",
        y=["cases", "death", "recovered"],
        figsize=[8, 6],
        title="VIET NAM WEEKLY COVID-19'S STATISTICS OVERVIEW",
    )
    df.plot(
        x="date",
        y="avgCases7day",
        c="b",
        ax=ax,
        style="--",
    )
    df.plot(
        x="date",
        y="avgRecovered7day",
        c="g",
        ax=ax,
        style="--",
    )
    # plt.xticks(label=none)#xoay label
    plt.legend(fontsize=6, loc="upper right")
    plt.gca().axes.set(xlabel=None)  # hide xlabel
    # plt.show()
    fig = plt.gcf()
    fig.set_size_inches(7, 5)
    plt.savefig("7daysChart.png", dpi=100)
