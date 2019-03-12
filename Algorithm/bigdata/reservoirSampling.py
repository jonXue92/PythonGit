# -*- coding: utf-8 -*-

import random
SAMPLE_COUNT = 10

# Force the value of the seed so the results are repeatable
random.seed(12345)

sample_titles = []
for index, line in enumerate(open("")):
    # Generate the reservoir
    if index < SAMPLE_COUNT:
        sample_titles.append(line)
    else:
        # Randomly replace elements in the reservoir with a decreasing probability.
        # Choose an integer between 0 and index (inclusive)
        r = random.randint(0, index)
        if r < SAMPLE_COUNT:
            sample_titles[r] = line
            
print sample_titles