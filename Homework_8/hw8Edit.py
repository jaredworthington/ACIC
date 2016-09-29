from netCDF4 import Dataset #access netcdf data
import plotly.offline as py
import plotly.graph_objs as go #use plotly
import sys

try:  
    with Dataset(sys.argv[1], "r") as tmin:
        tempMinJ = tmin.variables["tmin"][0]
        tempMinA = tmin.variables["tmin"][91]
        tempMinY = tmin.variables["tmin"][182]
        tempMinO = tmin.variables["tmin"][274] #min temps at certain days of year
except:
    print "Invalid, or no file name provided"

#of course I would loop this through every day of the year if I wasn't just doing four for now...
#plot the heatmaps for tmin with the same zmin and zmax values
data = [go.Heatmap(
    z = tempMinJ,
    zmin = -7,
    zmax = 27,
    )]
py.plot(data)

data = [go.Heatmap(
    z = tempMinA,
    zmin=-7,
    zmax=27,
    )]
py.plot(data)

data = [go.Heatmap(
    z = tempMinY,
    zmin=-7,
    zmax=27,
    )]
py.plot(data)

data = [go.Heatmap(
    z = tempMinO,
    zmin=-7,
    zmax=27,
    )]
py.plot(data) #check your browser for the images (they're interactive!)
