import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import collections

def gather_aborts():
    aborts_dict = {}
    files = [file for file in os.listdir(".") if "stats_T" in file]
    #print(files)
    for file in files:
        gvcs, aborts = pd.read_csv(file).to_dict('list').values()
        for gvc in gvcs:
            aborts_dict.update({gvc: aborts_dict.setdefault(gvc, 0) + 1})
    return collections.OrderedDict(sorted(aborts_dict.items()))

def plot_aborts(aborts_dict):
    gvcs = list(aborts_dict.keys())
    aborts = list(aborts_dict.values())
    print(gvcs)
    print(aborts)
    # evaluate the cumulative
    cumulative = np.cumsum(aborts)
    # plot the cumulative function
    plt.plot(gvcs, cumulative, c='blue')
    # plot the survival function
    #plt.plot(data, len(data) - cumulative, c='green')
    plt.show()
    print('total aborts: ' + str(sum(aborts)))

if __name__ == '__main__':
    print(gather_aborts())
    plot_aborts(gather_aborts())