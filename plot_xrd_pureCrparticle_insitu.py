# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:12:42 2022

@author: xiaoy
"""

import numpy as np
import matplotlib as mpl
import os
import pandas as pd
import glob
import palettable.scientific.sequential as pss
import matplotlib.pylab as pylab
from matplotlib.ticker import FormatStrFormatter

time = [0,1.55,3.1,4.65,6.2,7.75,9.3,10.85,12.4,13.95]
path = 'C://Research//2020_xiaoyang//MoltenSalt//manuscript_prep//Crparticle//PDF_Cr_pure_3um_insitu//manual_calibrate_20221013//'
os.chdir(path)
files = sorted(glob.glob(path+'*.xy'))
fig, ax1 = pylab.subplots(1,1)#, figsize=(16,16))

number = len(files)
palette = pss.get_map('Batlow_12',reverse=False)
cmap = palette.mpl_colormap
colors = [cmap(i) for i in np.linspace(0,1,number)]
bccCr_pdf = [4.68,6.62,8.109,9.368,10.475,11.478]
for i,f in enumerate(files):
    data = pd.read_csv(f,skiprows=23,sep='  ', names=['2theta','intensity'])
    name = os.path.splitext(os.path.basename(f))[0]
    x = np.asarray(data['2theta'])
    y = np.asarray(data['intensity'])+i*750
    ax1.plot(x,y,'-',linewidth=3,color=colors[i],label=name)

#ax1.legend()
ax1.vlines(x=bccCr_pdf,ymin=0,ymax=380,linestyles='solid',colors='r',linewidth=3.3,label='bccCr')
ax1.set_xlabel('2 theta (deg)')
ax1.set_ylabel('Intensity (a.u.)')
ax1.set_xlim([3, 12])
ax1.set_ylim([0, 9500])
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
params = {'legend.fontsize':10,
          'figure.figsize':(6,12),
          'axes.labelsize':24,
          'axes.titlesize':18,
          'xtick.labelsize':24,
          'ytick.labelsize':0,
          'axes.linewidth': 2.6,
          'ytick.major.width': 2.5,
          'xtick.major.width': 2.5,
          'ytick.major.size': 3.5,
          'figure.dpi': 100}
pylab.rcParams.update(params)

norm = mpl.colors.Normalize(vmin=min(time), vmax=round(max(time)))
cmap2 = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
cmap2.set_array([])
cbar = fig.colorbar(cmap2,orientation='vertical')
#cbar.outline.set_visible(False)
cbar.ax.tick_params(labelsize=23)
cbar.set_label('Time (min)', rotation=90,fontsize=24)
#cbar.ax.set_title('Time (min)',fontsize=14,loc='right',y=0.5)

#%%
time = np.arange(0,20,1.41)
path = 'C://Research//2020_xiaoyang//MoltenSalt//202105_PDF//PDF_5wtpCr_insitu_aftercali-20220221T230811Z-001//PDF_5wtpCr_insitu_aftercali//'
os.chdir(path)
files = glob.glob(path+'*.xy')[0:14]
fig, ax1 = pylab.subplots(1,1)#, figsize=(16,16))

number = len(files)
palette = pss.get_map('Batlow_12',reverse=False)
cmap = palette.mpl_colormap
colors = [cmap(i) for i in np.linspace(0,1,number)]

for i,f in enumerate(files):
    data = pd.read_csv(f,skiprows=23,sep='  ', names=['2theta','intensity'])
    name = os.path.splitext(os.path.basename(f))[0]
    x = np.asarray(data['2theta'])
    y = np.asarray(data['intensity'])+i*400
    ax1.plot(x,y,'-',linewidth=3,color=colors[i],label=name)

#ax1.legend()
ax1.set_xlabel('2 theta (deg)')
ax1.set_ylabel('Intensity (a.u.)')
ax1.set_xlim([2, 16])
ax1.set_ylim([0, 7000])
params = {'legend.fontsize':10,
          'figure.figsize':(12,12),
          'axes.labelsize':18,
          'axes.titlesize':16,
          'xtick.labelsize':18,
          'ytick.labelsize':0,
          'axes.linewidth': 1.5,
          'ytick.major.width': 1.5,
          'xtick.major.width': 1.5,
          'ytick.major.size': 3.5}
pylab.rcParams.update(params)

norm = mpl.colors.Normalize(vmin=min(time), vmax=round(max(time)))
cmap2 = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
cmap2.set_array([])
cbar = fig.colorbar(cmap2,orientation='vertical')
#cbar.outline.set_visible(False)
cbar.ax.tick_params(labelsize=16)
cbar.set_label('Time (min)', rotation=90,fontsize=18)

#%%together
fig, (ax1,ax2) = pylab.subplots(1,2)
time_pristine = [0,1.55,3.1,4.65,6.2,7.75,9.3,10.85,12.4,13.95]
path1 = 'C://Research//2020_xiaoyang//MoltenSalt//manuscript_prep//Crparticle//PDF_Cr_pure_3um_insitu//manual_calibrate_20220920//'
os.chdir(path1)
files1 = glob.glob(path1+'*.xy')
number = len(files)
palette = pss.get_map('Batlow_12',reverse=False)
cmap = palette.mpl_colormap
colors1 = [cmap(i) for i in np.linspace(0,1,number)]

for i,f in enumerate(files1):
    data = pd.read_csv(f,skiprows=23,sep='  ', names=['2theta','intensity'])
    name = os.path.splitext(os.path.basename(f))[0]
    x1 = np.asarray(data['2theta'])
    y1 = np.asarray(data['intensity'])+i*350
    ax1.plot(x1,y1,'-',linewidth=3,color=colors1[i],label=name)
ax1.set_xlabel('2 theta (deg)')
ax1.set_ylabel('Intensity (a.u.)')
ax1.set_xlim([3, 16])
ax1.set_ylim([0, 6500])


time_salt = np.arange(0,20,1.41)
path2 = 'C://Research//2020_xiaoyang//MoltenSalt//202105_PDF//PDF_5wtpCr_insitu_aftercali-20220221T230811Z-001//PDF_5wtpCr_insitu_aftercali//'
os.chdir(path2)
files2 = glob.glob(path2+'*.xy')[0:14]
number2 = len(files2)
palette = pss.get_map('Batlow_12',reverse=False)
colors2 = [cmap(i) for i in np.linspace(0,1,number)]
for i,f in enumerate(files2):
    data = pd.read_csv(f,skiprows=23,sep='  ', names=['2theta','intensity'])
    name = os.path.splitext(os.path.basename(f))[0]
    x2 = np.asarray(data['2theta'])
    y2 = np.asarray(data['intensity'])+i*350
    ax2.plot(x2,y2,'-',linewidth=3,color=colors[i],label=name)

#ax1.legend()
ax2.set_xlabel('2 theta (deg)')
ax2.set_ylabel('Intensity (a.u.)')
ax2.set_xlim([3, 16])
ax2.set_ylim([0, 6500])

params = {'legend.fontsize':10,
          'figure.figsize':(5,12),
          'axes.labelsize':20,
          'axes.titlesize':16,
          'xtick.labelsize':20,
          'ytick.labelsize':0,
          'axes.linewidth': 1.5,
          'ytick.major.width': 1.5,
          'xtick.major.width': 1.5,
          'ytick.major.size': 3.5,
          'figure.subplot.wspace': 0.05}
pylab.rcParams.update(params)

norm = mpl.colors.Normalize(vmin=min(time_pristine), vmax=round(max(time_pristine)))
cmap2 = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
cmap2.set_array([])
cbar = fig.colorbar(cmap2,ax=ax1,orientation='vertical',pad=0.02)
#cbar.outline.set_visible(False)
cbar.ax.tick_params(labelsize=16)
cbar.set_label('Time (min)', rotation=90,fontsize=18)

norm = mpl.colors.Normalize(vmin=min(time_salt), vmax=round(max(time_salt)))
cmap2 = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
cmap2.set_array([])
cbar = fig.colorbar(cmap2,ax=ax2,orientation='vertical',pad=0.02)
#cbar.outline.set_visible(False)
cbar.ax.tick_params(labelsize=16)
cbar.set_label('Time (min)', rotation=90,fontsize=18)

#%%  similiar time point comapre
file_pCr = 'C://Research//2020_xiaoyang//MoltenSalt//manuscript_prep//Crparticle//PDF_Cr_pure_3um_insitu//manual_calibrate_20220920//A2_pure_Cr3um_711_20210527-035527_7bc3fd_0001_corrected.xy'
file_pCr_first = 'C://Research//2020_xiaoyang//MoltenSalt//manuscript_prep//Crparticle//PDF_Cr_pure_3um_insitu//manual_calibrate_20220920//A2_pure_Cr3um_711_20210527-034130_7117d8_0001_corrected.xy'
file_salt = 'C://Research//2020_xiaoyang//MoltenSalt//202105_PDF//PDF_5wtpCr_insitu_aftercali-20220221T230811Z-001//PDF_5wtpCr_insitu_aftercali//B2_5wtp_Cr3um_KClMgCl2_insitu711_20210525-232700_2d97d8_0001_dark_corrected_img.xy'
file_salt_first = 'C://Research//2020_xiaoyang//MoltenSalt//202105_PDF//PDF_5wtpCr_insitu_aftercali-20220221T230811Z-001//PDF_5wtpCr_insitu_aftercali//B2_5wtp_Cr3um_KClMgCl2_insitu711_20210525-231319_77631c_0001_dark_corrected_img.xy'
file_salt_last = 'C://Research//2020_xiaoyang//MoltenSalt//202105_PDF//PDF_5wtpCr_insitu_aftercali-20220221T230811Z-001//PDF_5wtpCr_insitu_aftercali//B2_5wtp_Cr3um_KClMgCl2_insitu711_20210526-110514_b4424c_0001_dark_corrected_img.xy'

#file_bccCr_PDFcard = 'C://Research//2020_xiaoyang//MoltenSalt//manuscript_prep//Crparticle//Figures_formanuscript//PDF_Card//04-004-2650 (Calc)_Cr.xy' 
#file_dCr_PDFcard = 'C://Research//2020_xiaoyang//MoltenSalt//manuscript_prep//Crparticle//Figures_formanuscript//PDF_Card//00-019-0323 (Exp-based)_Cr4.xy' 
fig2,ax2_1 = pylab.subplots(1,1)

data_pCr = pd.read_csv(file_pCr,skiprows=23,sep='  ', names=['2theta','intensity'])
x_pCr = np.asarray(data_pCr['2theta'])
y_pCr = np.asarray(data_pCr['intensity'])
data_salt = pd.read_csv(file_salt,skiprows=23,sep='  ', names=['2theta','intensity'])
x_salt = np.asarray(data_salt['2theta'])
y_salt = np.asarray(data_salt['intensity'])-250
data_pCr_first = pd.read_csv(file_pCr_first,skiprows=23,sep='  ', names=['2theta','intensity'])
x_pCr_first = np.asarray(data_pCr_first['2theta'])
y_pCr_first = np.asarray(data_pCr_first['intensity'])-50
data_salt_first = pd.read_csv(file_salt_first,skiprows=23,sep='  ', names=['2theta','intensity'])
x_salt_first = np.asarray(data_salt_first['2theta'])
y_salt_first = np.asarray(data_salt_first['intensity'])-300
data_salt_last = pd.read_csv(file_salt_last,skiprows=23,sep='  ', names=['2theta','intensity'])
x_salt_last = np.asarray(data_salt_last['2theta'])
y_salt_last = np.asarray(data_salt_last['intensity'])-110

bccCr_pdf = [4.653,6.583,8.064,9.315,10.417,11.414]
dCr_pdf = [4.149,4.657,5.095,5.924,6.624,6.882,7.194,7.493,7.787,8.339,9.345,9.532,9.760,10.486,11.198,11.447,11.772]

'''
data_bccCr = pd.read_csv(file_bccCr_PDFcard,sep='\t',names=['2theta','intensity'])
x_bccCr = np.asarray(data_bccCr['2theta'])
y_bccCr = np.asarray(data_bccCr['intensity'])
data_dCr = pd.read_csv(file_dCr_PDFcard,sep='\t',names=['2theta','intensity'])
x_dCr = np.asarray(data_dCr['2theta'])
y_dCr = np.asarray(data_dCr['intensity'])
'''

ax2_1.plot(x_pCr,y_pCr,'-',linewidth=3,color='g',label='Cr_13.95min')
ax2_1.plot(x_salt,y_salt,'-',linewidth=3,color='r',label='Crsalt_13.68min')
ax2_1.plot(x_pCr_first,y_pCr_first,'--',linewidth=3,color='g',label='Cr_first')
ax2_1.plot(x_salt_first,y_salt_first,'--',linewidth=3,color='r',label='Crsalt_0')
ax2_1.plot(x_salt_last,y_salt_last,'-.',linewidth=3,color='r',label='Crsalt_last')
#ax2_1.plot(x_bccCr,y_bccCr,'-',linewidth=3,color='b',label='bccCr')
#ax2_1.plot(x_dCr,y_dCr,'-',linewidth=3,color='k',label='dCr')
ax2_1.vlines(x=bccCr_pdf,ymin=0,ymax=150,linestyles='solid',colors='c',linewidth=3,label='bccCr')
ax2_1.vlines(x=dCr_pdf,ymin=0,ymax=120,linestyles='solid',colors='m',linewidth=3,label='delta_Cr')

ax2_1.set_xlabel('2 theta (deg)')
ax2_1.set_ylabel('Intensity (a.u.)')
ax2_1.set_xlim([3.3, 10])
ax2_1.set_ylim([0, 700])
#ax2_1.legend()

params = {'legend.fontsize':26,
          'figure.figsize':(12,12),
          'axes.labelsize':18,
          'axes.titlesize':16,
          'xtick.labelsize':18,
          'ytick.labelsize':0,
          'axes.linewidth': 1.5,
          'ytick.major.width': 1.5,
          'xtick.major.width': 1.5,
          'ytick.major.size': 3.5,
          'figure.subplot.wspace': 0.05}
pylab.rcParams.update(params)





