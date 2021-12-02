import numpy as np
from pylab import *
from math import e
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import fileinput
import os

def mobs(adder):

    def generate_specific_rows(filePath, row_indices=[]):
        with open(filePath) as f:
            for i, line in enumerate(f):
                if i in row_indices:
                    yield line
    #Calls a specific row from a text file

    gbt = generate_specific_rows("/Users/alexh/Desktop/Coding/Pulsars/observatories.dat",row_indices = [5])
    gbt_coords = loadtxt(gbt, skiprows=0,unpack=True,usecols=(0,1,2,3,4),dtype=str)
    name1 = "tag\t\t\tgbt"
    #Calls GBT telescope coords from Observatory file

    newx1 = float(gbt_coords[0])+adder
    newy1 = float(gbt_coords[1])+adder
    newz1 = float(gbt_coords[2])+adder
    #Adds some amount of distance to each direction


    filename = "observatories.dat"

    with fileinput.FileInput(filename, inplace = True, backup ='.bak') as f:
        for line in f:
            if "gbt" in line:
                print("\t",newx1,"\t",newy1,"\t",newz1,"\t\t\t",name1,
                      end ='\n')
            else:
                print(line, end ='')
    #puts new coordinates (the ones updated with the adder) into observatory file
    #copies original file before adder as .bak as well 

if __name__ == "__main__":
    globals()[sys.argv[1]]()
