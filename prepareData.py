#!/usr/bin/python


import sys
import pandas as pd
import numpy as np

if(len(sys.argv) == 3):

    dfData = pd.read_excel(sys.argv[1]) # no error handling

    data = np.array(dfData.as_matrix().transpose())

    i = 0
    prep = []
    while(i < len(data)):
        prep.extend(data[i])
        i += 1

    prep = list(filter(lambda v: v==v, prep)) # remove NaN values

    dfPrep = pd.DataFrame(prep)

    dfPrep.to_excel((pd.ExcelWriter(sys.argv[2])))
else:
    print("need two arguments")
