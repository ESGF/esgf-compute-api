import cartopy.crs as ccrs
import cartopy.feature as cfeature
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from eofs.standard import Eof

# inFile = '/Users/tpmaxwel/Dropbox/Tom/Data/CIP/MERRA2/mon/tas/tas.1980-2015.nc'
# filename = '/dass/pubrepo/CREATE-IP/data/reanalysis/NOAA-NCEP/CFSR/mon/atmos/clt/clt_Amon_reanalysis_CFSR_197901-201712.nc'
filename = '/dass/adm/edas/eofs-1.3.0/lib/eofs/examples/example_data/sst_ndjfm_anom.nc'
ncin = Dataset(filename, 'r')

sst = ncin.variables['tas'][:]
lons = ncin.variables['longitude'][:]
lats = ncin.variables['latitude'][:]
ncin.close()

coslat = np.cos(np.deg2rad(lats))
wgts = np.sqrt(coslat)[..., np.newaxis]
solver = Eof(sst, weights=wgts)

eof1 = solver.eofsAsCorrelation(neofs=1)
pc1 = solver.pcs(npcs=1, pcscaling=1)

# Plot the leading EOF expressed as correlation in the Pacific domain.
clevs = np.linspace(-1, 1, 11)
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=190))
fill = ax.contourf(lons, lats, eof1.squeeze(), clevs, transform=ccrs.PlateCarree(), cmap=plt.cm.RdBu_r)
ax.add_feature(cfeature.LAND, facecolor='w', edgecolor='k')
cb = plt.colorbar(fill, orientation='horizontal')
cb.set_label('correlation coefficient', fontsize=12)
plt.title('EOF1 expressed as correlation', fontsize=16)

# Plot the leading PC time series.
plt.figure()
years = range(1979, 2017)
plt.plot(years, pc1, color='b', linewidth=2)
plt.axhline(0, color='k')
plt.title('PC1 Time Series')
plt.xlabel('Year')
plt.ylabel('Normalized Units')
plt.xlim(1979, 2017)
plt.ylim(-3, 3)

plt.show()
