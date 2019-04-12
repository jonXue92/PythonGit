# -*- coding: utf-8 -*-

import sys
import time
import random
from multiprocessing import Process, Queue

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from tqdm import tqdm

WORKCOUNT = 8
TRIALCOUNT = 10

def main():
    listlengths = range(2, 10)
    times = []
    for listlength in listlengths:
        print(listlength)
        trials = {'time': [], 'cycles': []}
        for trial in tqdm(range(TRIALCOUNT)):
            stime = time.time()
            array = random.sample(list(range(listlength)), k=listlength)

            workers = []
            output = Queue()
            counts = Queue()
            for _ in range(WORKCOUNT):
                w = Sorter(array, output, counts)
                workers.append(w)
                w.start()

            result = output.get()

            total_count = 0
            for _ in range(WORKCOUNT):
                total_count += counts.get()

            for _ in range(WORKCOUNT):
                output.put('DEATH')

            for w in workers:
                w.join()

            etime = time.time()
            trials['time'].append(etime - stime)
            trials['cycles'].append(total_count)
        times.append(trials)

    fig, axarr = plt.subplots(2, 1, figsize=(8, 6))

    for i, (length, trial) in enumerate(zip(listlengths, times)):
        axarr[0].plot(np.ones(TRIALCOUNT) * length, np.log(trial['time']), 'rx', alpha=0.4)
    axarr[0].plot(listlengths, [np.log(sum(t['time']) / len(t['time'])) for t in times], label='Average Result')
    axarr[0].legend(loc=0)
    axarr[0].set_xlabel('Length of Initial List')
    axarr[0].set_ylabel('Average Time Elapsed - ln(seconds)')

    for i, (length, trial) in enumerate(zip(listlengths, times)):
        axarr[1].plot(np.ones(TRIALCOUNT) * length, np.log(trial['cycles']), 'rx', alpha=0.4)
    axarr[1].plot(listlengths, [np.log(sum(t['cycles']) / len(t['cycles'])) for t in times], label='Average Result')
    axarr[1].plot(listlengths, np.log([n * factorial(n) for n in listlengths]), label=r'$n \cdot n!$')
    axarr[1].legend(loc=0)
    axarr[1].set_xlabel('Length of Initial List')
    axarr[1].set_ylabel('Average Time Elapsed - ln(Operations)')

    fig.suptitle('Parallel Bogosort')
    plt.tight_layout()
    plt.savefig('bogosort.png')

def is_sorted(some_list):
    for x, y in zip(some_list[:-1], some_list[1:]):
        if x > y:
            return False
    return True

class Sorter(Process):
    def __init__(self, array, output, counts, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.array = array
        self.length = len(array)
        self.output = output
        self.count = 0
        self.counts = counts

    def run(self):
        while True:
            if self.output.empty():
                new_list = random.sample(self.array, k=len(self.array))
                self.count += self.length   # not just one, we have to check all items 
                if is_sorted(new_list):
                    self.counts.put(self.count)
                    self.output.put(new_list)
                    break
            else:
                self.counts.put(self.count)
                break

if __name__ == '__main__':
    sys.exit(main())