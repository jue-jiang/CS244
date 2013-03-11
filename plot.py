'''
Plot
'''

import matplotlib as m
m.use("Agg")
import matplotlib.pyplot as plt

from argparse import ArgumentParser

import string

parser = ArgumentParser(description="Jellyfish Plots")
parser.add_argument('-i',
                    help="Input file for the plot.",
                    dest="in",
                    default=None)

parser.add_argument('-o',
                    help="Output png file for the plot.",
                    dest="out",
                    default=None) # Will show the plot

args = parser.parse_args()

def plotData(filename, label, color):
    f = open(filename)
    lines = f.readlines()

    keys = []
    values = []
    cdf = 0
    for line in lines:
        datum = string.split(line.strip(), " ")
        values.append(int(datum[0]))
        cdf += int(datum[1])
        keys.append(cdf)

    plt.plot(keys, values, lw=1, label=label, color=color, drawstyle="steps-pre")

'''
plt.plot(keys, values, lw=2, label="8 shortest paths", color="blue", drawstyle="steps-pre")
plt.plot(keys, values, lw=1, label="64 way ecmp", color="green", drawstyle="steps-pre")
plt.plot(keys, values, lw=1, label="8 way ecmp", color="red", drawstyle="steps-pre")
'''
plotData('results/jf-ecmp', 'ECMP', 'red')
plotData('results/jf-ksp', 'KSP', 'blue')

#plt.xlim((start,end))
#plt.ylim((start,end))
plt.xlabel("Rank of Link")
plt.ylabel("# Paths Link is on")
plt.legend()

if args.out:
    print "Saving output to %s" % args.out
    plt.savefig(args.out)
else:
    plt.show()
