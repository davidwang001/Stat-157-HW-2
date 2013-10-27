# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Stat 157 Project 2

# <headingcell level=2>

# Group 8: David Wang, Hyungkyu Chang, Bonghyun Kim, Sung Hoon Choi

# <headingcell level=3>

# Objective: The first objective of this assignment is to improve the data handling of the code by upgrading from the deprecated data source to the new data source which uses a different data format called JSON.
# 
# Since we are working with live data we also need to cache the data so that we can reliably re-run the code using the same data (or optionally with the live data).
# 
# The second objective is that we would like to be able to see data for earthquakes in states other than Alaska, so the next part of the assignment requires refactoring the code to parameterize the function definition instead of relying on the hard-coded values for latitude and longitude of the bounding box around the region of interest.
# 
# This assignment features two main roles: the Data Curator and the Visualizer. All 4 members of your vertical group should work together no matter what individual roles you have assigned.

# <headingcell level=4>

# Steps Taken:

# <markdowncell>

# Bonghyun took the steps and produced the code to curate the data. David, our visualizer, got the codes done to produce the map we needed.
# Sung and Hyungkyu helped along the way to provide feedback and point out the problems we had with the code.

# <markdowncell>

# Our Code:

# <codecell>

import urllib
import json
import sys
import datetime

url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
data = json.load(urllib.urlopen(url))

from mpl_toolkits.basemap import Basemap
def plotQuakes(place, data):
    lats = []
    longs = []
    magnitude = []
    depth = []
    for f in data['features']:
        if place in f['properties']['place']:
            longs.append(f['geometry']['coordinates'][0])
            lats.append(f['geometry']['coordinates'][1])
            magnitude.append(f['properties']['place'][0])
            depth.append(f['geometry']['coordinates'][2])
    center_Lat = mean(lats)
    center_Long = mean(longs)
    margin=50
    maxLong = center_Long+margin
    maxLat = center_Lat+margin
    minLat = center_Lat-margin
    minLong = center_Long-margin

    print "hello"

    #normalize depth data to convert into colors
    #normal_depth = (depth-min(depth))/(max(depth)-min(depth))
    #depth_color = 0
    
    m = Basemap(llcrnrlon=minLong,llcrnrlat=minLat,
                urcrnrlon=maxLong,urcrnrlat=maxLat,
                resolution='l',area_thresh=1000.,projection='merc',
                lat_0=center_Lat,lon_0=center_Long)
            
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='coral',lake_color='blue')
    m.drawmapboundary(fill_color='aqua')
    m.plot(longs, lats, 'k.','MarkerSize',magnitude)
    return m
    
plotQuakes('Alaska', data)

# <codecell>

m = Basemap(llcrnrlon=-180,llcrnrlat=50.,
            urcrnrlon=-120.,urcrnrlat=72,
            resolution='l',area_thresh=1000.,projection='merc',
            lat_0=62.9540,lon_0=-149.2697)
m.plot?

# <headingcell level=4>

# Problems:

# <markdowncell>

# We should have cached the data to make the data more reproducible.
# As the data is stores in our local directories, other people are unable to reproduce this data.
# Also, we tried our best to make the code work for other states as well, which will be explained more in the Roadblocks section below.

# <headingcell level=4>

# Roadblocks:

# <markdowncell>

# We encountered some major roadblocks during this project.
# 
# The main roadblock was communication.
# We set up office hours and time to meet. However, it was difficult to get everyone to respond and share their available times with each other.
# Everyone had things they needed to do other than the project, and could not get enough time to meet up and had to leave after a while. 
# Also, we had trouble sending each other codes as we could not find an adequate method to do so.
# As a result, some people ended up with the code other members created, others didn't.
# In fact, the code to generalize and make the plot work for other states was not passed on correctly and didn't get to the member who is responsible for creating the iPython on time. 
# 
# Another major roadblock was the familiarity with codes.
# Certain members were extremely unfamiliar with the codes and could not help with the coding stage of the project.
# This resulted in other members stressing more over the codes and debugging, while the members could not help but sit back and watch.
# We tried to address this problem by assigning people to specific roles that did not involve the coding, but the first roadblock made it difficult to do so.

