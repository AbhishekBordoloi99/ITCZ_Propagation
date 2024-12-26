import numpy as np
import xarray as xr
import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap
import cmaps
from matplotlib.colors import ListedColormap

def clm_itcz():
    path_precip='/Vol4/DATA/Rainfall/GPCP/GPCP_1DD_v1.2_199610-201510.nc'
    itcz=xr.open_dataset(path_precip).sel(lat=slice(50,-50)).groupby('time.dayofyear').mean('time')
    plt.rcParams['figure.figsize']=[20,20]
    for i in range(1,365):
        itcz_dayclm=itcz.sel(dayofyear=i).PREC.values
        custom_cmap = ListedColormap(['White', '#ADD8E6','#6F8FAF','#6495ED','#50C878','#FFC000','#FFA500','red','darkred'])
        lon=itcz['lon']
        lat=itcz['lat']
        Lon,Lat=np.meshgrid(lon,lat)
        map=Basemap(projection='merc',
                    lat_ts=10,
                    llcrnrlon=lon.min(),
                    urcrnrlon=lon.max(),
                    llcrnrlat=lat.min(),
                    urcrnrlat=lat.max(),
                    resolution='c'
                    )
        x,y=map(Lon,Lat)
        cs=map.contourf(x,y,itcz_dayclm,cmap=custom_cmap,levels=np.linspace(2,10,9),extend='both')
        map.drawcoastlines(linewidth=1,color='black')
        map.drawmapboundary()
        map.drawparallels(np.arange(-60,60,10.),labels=[1,0,0,0],fontsize=12)
        map.drawmeridians(np.arange(0,360,20.),labels=[0,0,0,1],fontsize=12)
        colbar=map.colorbar(cs,cmap=cmaps.MPL_jet)
        colbar.ax.tick_params(labelsize=14)
        if(i<10):
            plt.savefig('/Vol3/abhishek/CODES/github/itcz_plots/00'+str(i)+'.png')
        elif(i<100 and i>=10):
            plt.savefig('/Vol3/abhishek/CODES/github/itcz_plots/0'+str(i)+'.png')
        else:
            plt.savefig('/Vol3/abhishek/CODES/github/itcz_plots/'+str(i)+'.png')
    return 0
clm_itcz()