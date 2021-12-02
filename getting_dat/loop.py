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

# my small, poorly named function that calls mobs from moveobsfun and performs most of the simulating of the data. 
# dxyz represents adder from moveobsfun— that is, how much distance is being added onto the original coordinate for the observatory 
# stit is just an array of strings to help with naming the simulated pulsar data that comes out the other end as 13 text files (one for each adder)
# The loop does several things. First it calls mobs which moves the observatory. Then, it runs TEMPO2 which takes in the .par and .tim files for
# the desired pulsar and produces the new .par file withe the predicted measurements. It will be different than the input .par file because the observatoy
# position has changed. That being said, not much change happens at small differences in position. 
# It renames the .par file with my naming system and then replaces the observatory file (which now has altred coordinates) with the original. 
# This process is then repeated for each adder. 
# This was the program that was ran with SLURM on bowser, some pulsars taking a few seconds and others taking days depending on how many TOAs (time of arrivals)
# were in the .tim file. For example, pulsars that have been observed a lot took the most time 
