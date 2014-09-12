import matplotlib.patches as patches
import matplotlib.path as path                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
from pylab import plotfile, show, gca
import matplotlib.cbook as cbook
import pandas as pd # great library for examining data \('3')/
import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np
import pytz
import time
import csv

#default condtions to for csv. commands =================================================================================
dia = csv.excel()
dia.quoting = csv.QUOTE_NONE

#user specifies location
#location=raw_input("What data do you want to process?:")
location='C:\Users\SMathew\Desktop\TEMP\Cathy.csv'
print "I thought so"

df=pd.read_csv(location)
#kicks=raw_input("What column do you want to look at?")#Energy
kicks='Alarm Status Flag'
local_0=df[kicks]# you can index this list of values by doing local_0[i]

baby={}
children={}
Length={}# creates a full array comparable to the data in the sheet.
child=''
total=int()
teen=''
mob={}
ticker=int()
a=int()
o=0


#function reads selected column's indexed data from location !!!!REPEAT!!!!!

def read_data(location): #=============================================================================================
        df=pd.read_csv(location, index_col=[0])
        local_0=df[kicks]# you can index this listof values by doing local_0[i]
        #print 'yes!'
        return

def histogram(children,mob):#==========================================================================================
        total=mob.count(children, start= 0,end=len(string))
        #print total
        return


def pattern_discovery(i,m):#===========================================================================================
        while m<10:
                read_data(location)
                while len(Length)<20:
                        #print len(local_0)-1
                        match(i)
                        #print i
                        #print len(local_0)-1
                        i=i+1
               
                child=str(Length)
                child= child.replace("0: '", "")
                child= child.replace("1: '", "")
                child= child.replace("2: '", "")
                child= child.replace("3: '", "")
                child= child.replace("4: '", "")
                child= child.replace("5: '", "")
                child= child.replace("6: '", "")
                child= child.replace("7: '", "")
                child= child.replace("8: '", "")
                child= child.replace("9: '", "")
                child= child.replace("10: '", "")
                child= child.replace("11: '", "")
                child= child.replace("12: '", "")
                child= child.replace("13: '", "")
                child= child.replace("14: '", "")
                child= child.replace("15: '", "")
                child= child.replace("16: '", "")
                child= child.replace("17: '", "")
                child= child.replace("18: '", "")
                child= child.replace("19: '", "")
                child= child.replace("', ", "")
                child= child.replace("'", "")
                child= child.replace("{", "")
                child= child.replace("}", "")
                children[m]=child
                
                #print children
                #print teen
                #histogram(children,mob)
                #print total
                m=m+1
        return  

def match(i):#============================================================================================================
        if local_0[i]=='0x10':
                Length[i]='1'     
        elif local_0[i]=='0x00':
                Length[i]='0'  
        else:
                o=o+1
        return  Length



def circle_of_life(ticker,mob,a):#naaa zabanennyaaa!!!!!==================================================================
           while a<len(ticker):
                if local_0[a]=='0x10':
                        local_0[a]='1'
                        a=a+1
                        mob[a]='1'
                elif local_0[a]=='0x00':
                        local_0[a]='0'
                        a=a+1
                        mob[a]='0'
                else:
                        o=o+1
        
        mob=str(mob)
        mob= mob.replace("2","")
        mob= mob.replace("3","")
        mob= mob.replace("4","")
        mob= mob.replace("5","")
        mob= mob.replace("6","")
        mob= mob.replace("7","")
        mob= mob.replace("8","")
        mob= mob.replace("9","")        
        mob= mob.replace("1:", "")
        mob= mob.replace("0:", "")#be careful, DO NOT RUN THIS TWICE OR YOU WILL TAKE OUT EXTRA ZERO VALUE PART OF THE HEX!
        mob= mob.replace(" :", "")
        mob= mob.replace(" ", "")
        mob= mob.replace(",", "")
        mob= mob.replace("'", "")
        mob= mob.replace("{", "")
        mob= mob.replace("}", "")
        
        pattern_discovery(0,0)

        print mob
        return


#==========================================================================================================================
o=0
circle_of_life(local_0,mob,0)

#Leave an uplifting message================================================================================================

print "Up up up!"        
     


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
