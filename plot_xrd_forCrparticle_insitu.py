# -*- coding: utf-8 -*-
"""
Created on Wed May 26 13:51:24 2021

@author: xiaoy
"""
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np
#import palettable.cartocolors.sequential as pld
import palettable.cartocolors.diverging as pld
import palettable.scientific.sequential as pss
import matplotlib.pylab as pylab
from matplotlib.ticker import FormatStrFormatter

#__________________________________________________________________________________
#extract scans from folder
#inpath = 'C://Research//2020_xiaoyang//MoltenSalt//202105_PDF//data//A4_1wtp_Cr3um_10atp_CrCl3_KClMgCl2_711//integration//'  #LCS A3
#files = glob.glob(inpath + '*.chi')
#files.sort()
#fileend = '_tth'
#for f in files:
#    if fileend in f:
#        files.remove(f)
#files.sort()
#for f in np.arange(0,len(files),6):
#    data = pd.read_csv(files[f],index_col=0)
#    name = os.path.splitext(os.path.basename(files[f]))[0]
#    data.to_csv('C://Research//2020_xiaoyang//MoltenSalt//202105_PDF//data//plot_figure//1wtpCr_10atp_CrCl3_KClMgCl2_insitu//'+name+'.chi')
#---------------------------------------------------------------------------


inpath = 'C://Research//2020_xiaoyang//MoltenSalt//202105_PDF//PDF_5wtpCr_insitu_aftercali-20220221T230811Z-001//PDF_5wtpCr_insitu_aftercali//'  #LCS A3
files = sorted(glob.glob(inpath + '*.xy'))
number = len(files)
palette = pss.get_map('Batlow_12',reverse=False)
cmap = palette.mpl_colormap
colors = [cmap(i) for i in np.linspace(0,1,number)]
f1, (ax1,ax2) = plt.subplots(1, 2)
blank = np.zeros([int(len(files)),2248])  #all: 2248
offset = 10#10
gap = 5#10

total_time = 680.75 # in minutes   #1wt%: 21.5min, 2wt%: 165min, 5wt%: 680.75min, 12.5wt%:255.75, pure_salt:12.15
time_interval = round((total_time/(number-1)),2)
time_list = np.arange(0, total_time+1, time_interval*gap)
#time_list_sub = np.arange(0, total_time+1, time_interval)
plt.figure()
color_idx = np.linspace(0, 1, time_list.shape[0])
Z = [[0,0],[0,0]]
#levels = color_idx*len(files)
#levels = color_idx*time_list.shape[0]
#levels = color_idx*total_time
#color_bar = plt.contourf(Z, np.round(levels,2), cmap=cmap) #plt.cm.autumn)
select_time_list = np.arange(0,len(time_list),4)
color_bar = plt.contourf(Z, time_list[select_time_list], cmap=cmap)
plt.close()
#test_scan = [0,10,20,30,50,80,120] #for checking Cr bcc structure disappearance
#test_scan = [0,120,150,180,210,250,300,350,390]

#for i in np.arange(0,len(files),gap):#range(len(files)):#np.arange(0,50,2):
for i in np.arange(0,len(files),gap):
#for i in range(len(files)):
    #if files[i] != 'C://Research//2020_xiaoyang//Hybrid coating//corrosion test//20201113\\20201113_20201110_batch24_LCS_b4_Cu20_PAMAM50_3p5NaCl_C06.txt': 
    data = pd.read_csv(files[i],delimiter='  ',skiprows = 23,header=None, names=['2theta','intensity'])
    name = os.path.splitext(os.path.basename(files[i]))[0]
    x = data['2theta'][0:2248]#[236:450]#  #change range accordingly
    y = data['intensity'][0:2248]#[236:450] 
    ax1.plot(x,y+(offset*i), '-',color=colors[i],linewidth=3.3)
    ax1.set_xlim(4.0,6.0)
    ax1.set_ylim(600,5400)
    ax2.plot(x,y+(offset*i), '-',color=colors[i],linewidth=3.3)
    ax2.set_xlim(6.0,10.0)
    ax2.set_ylim(400,5400)
bccCr_pdf = [4.68,6.62,8.109,9.368,10.475,11.478]
ax1.vlines(x=bccCr_pdf[0],ymin=600,ymax=900,linestyles='solid',colors='r',linewidth=3.3,label='bccCr')
ax2.vlines(x=bccCr_pdf[1:],ymin=400,ymax=700,linestyles='solid',colors='r',linewidth=3.3,label='bccCr')
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax2.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
params2 = {'legend.fontsize':10,
           'figure.figsize':(12,12),
           'image.aspect':1,
           'figure.subplot.wspace': 0.14,
           'axes.formatter.limits': [-7, 7],
          'axes.labelsize':24,
          'axes.titlesize':12,
          'xtick.labelsize':24,
          'ytick.labelsize':0,
          'axes.linewidth': 2,
          'ytick.major.width': 2,
          'xtick.major.width': 2,
          'ytick.major.size': 3.5,
          'figure.dpi': 100}
pylab.rcParams.update(params2)

cbar1 = f1.colorbar(color_bar,ax=[ax1,ax2], ticks=time_list[select_time_list],pad=0.01)
cbar1.set_label('Time (min)', fontsize = 22)
cbar1.ax.tick_params(labelsize=18) 

ax1.set_xlabel('2 theta (deg)')
ax1.set_ylabel('Intensity (a.u.)')
ax2.set_xlabel('2 theta (deg)')

#%%
import matplotlib as mpl
inpath = 'C://Research//2020_xiaoyang//MoltenSalt//202105_PDF//PDF_5wtpCr_insitu_aftercali-20220221T230811Z-001//PDF_5wtpCr_insitu_aftercali//'  #LCS A3
files = sorted(glob.glob(inpath + '*.xy'))
number = 10
palette = pss.get_map('Batlow_12',reverse=False)
cmap = palette.mpl_colormap
colors = [cmap(i) for i in np.linspace(0,1,number)]
f1, ax1 = plt.subplots(1, 1)
blank = np.zeros([int(len(files)),2248])  #all: 2248
offset = 25#10
gap = 1#10
time = 13.68
for i in np.arange(0,number,gap):
    data = pd.read_csv(files[i],delimiter='  ',skiprows = 23,header=None, names=['2theta','intensity'])
    name = os.path.splitext(os.path.basename(files[i]))[0]
    x = data['2theta'][0:2248]#[236:450]#  #change range accordingly
    y = data['intensity'][0:2248]#[236:450] 
    ax1.plot(x,y+(offset*i), '-',color=colors[i],linewidth=3.3)
    ax1.set_xlim(4.0,6.0)
    ax1.set_ylim(630,1000)
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax1.vlines(x=4.19,ymin=630,ymax=1000,linestyles='solid',colors='r',linewidth=3,label='dCr')
ax1.vlines(x=5.13,ymin=630,ymax=1000,linestyles='solid',colors='r',linewidth=3,label='dCr')

params2 = {'legend.fontsize':10,
           'figure.figsize':(12,12),
           'image.aspect':1,
           'figure.subplot.wspace': 0.1,
           'axes.formatter.limits': [-7, 7],
          'axes.labelsize':22,
          'axes.titlesize':12,
          'xtick.labelsize':18,
          'ytick.labelsize':0,
          'axes.linewidth': 2,
          'ytick.major.width': 2,
          'xtick.major.width': 2,
          'ytick.major.size': 3.5}
pylab.rcParams.update(params2)

norm = mpl.colors.Normalize(vmin=0, vmax=time)
cmap2 = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
cmap2.set_array([])
cbar = f1.colorbar(cmap2,orientation='vertical')
#cbar.outline.set_visible(False)
cbar.ax.tick_params(labelsize=22)
cbar.set_label('Time (min)', rotation=90,fontsize=24)

ax1.set_xlabel('2 theta (deg)')
ax1.set_ylabel('Intensity (a.u.)')
ax2.set_xlabel('2 theta (deg)')
