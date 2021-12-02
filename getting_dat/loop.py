import numpy as np
from pylab import *
from math import e
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import fileinput
import os
from moveobsfun import mobs
import glob

dxyz = np.array([0, 1, 10, 100, 1000, 2000, 5000, 8000, 10000, 20000, 50000, 80000, 100000])
#dxyz = np.array([800000])

stit = np.array(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'])

for i in range(len(dxyz)):
    mobs(dxyz[i])
    os.system("mv observatories.dat /home/ahigley/newplace/tempo2_aho/observatory")
    os.system("tempo2 -newpar -f J0931-1902.working.par J0931-1902.working.tim")
    #path = '/Users/alexh/Desktop/Coding/Pulsars/'
    path = '/home/ahigley/timing_practice'
    os.rename('new.par', os.path.join(path, 's' + stit[i] + '.par'))
    os.system('mv observatories.dat.bak observatories.dat')
