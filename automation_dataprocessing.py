                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
import csv
import pytz
import pandas as pd # great library for examining data \('3')/
from pandas import DataFrame
import matplotlib.pyplot as plt
from pylab import plotfile, show, gca
import matplotlib.cbook as cbook
import time

plt.figure('Energy') # Name the graph antyhing you want!

#default condtions to for csv. commands=================================================================================
dia = csv.excel()
dia.quoting = csv.QUOTE_NONE
o=0# bla 

#user specifies location
#location=raw_input("What data do you want to process?:")
location='C:\Users\SMathew\Desktop\TEMP\Cathy.csv'
print "I thought so"

df=pd.read_csv(location, index_col=[0])
#kicks=raw_input("What column do you want to look at?")#Energy
kicks='Fixed Speed'
local_0=df[kicks]# you can index this list of values by doing local_0[i]
length=[0]*len(local_0)# creates a full array comparable to the data in the sheet.
#time=[1,2,3,4,45,5,6,7,7,88,90,5,3,2]# for a sample x-axis, not very important
count=0

#function reads selected column's indexed data from location !!!!REPEAT!!!!!

def read_data(location): #=============================================================================================
        df=pd.read_csv(location, index_col=[0])
        local_0=df[kicks]# you can index this listof values by doing local_0[i]
        return

def cycle_find(i):#==========================================================================================
        while i<len(local_0):
            if local_0[i]=='0x10':
                length[i]=1
                i=i+1
            elif local_0[i]=='0x00':
                length[i]=0
                i=i+1
            else:
                local_0[i]==length[i]
                
        plt.plot(length,'b*-')
        plt.axis([0, 100, 0, 6000]) # axis scales, don't worry  we zoom in. #len(local_0)
        plt.xlabel('X-title')
        plt.ylabel('Y-title')
        plt.title('EBB S/N')
        plt.annotate('A graph!', xy=(2, 1), xytext=(3, 1.5),arrowprops=dict(facecolor='black', shrink=0.05))
        plt.show()#um, you want to show the plot on the figure right?

cycle_find(0)# this is the key function being carried out to find your phases

#Leave an uplifting message

print "Wow, that was fast"        
     


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
