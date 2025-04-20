# Mobile Radio Triangulation for WiFi Source Mapping
# This script will generate a heatmap using Folium to simulate what the heatmap will look like
# Author: Danny Pham

import tkinter as tk
#import numpy as np
#####################################################################################################
import random as rd # Used for the simulation
from shapely.geometry import Point, Polygon # This is only for the simulation and can be deleted later
#####################################################################################################
import webview # Mapping window
import folium # allows interactive maps
from folium.plugins import HeatMap, MousePosition, Fullscreen
import time # for refresh capability for real time tracking
import threading #allows multiple executions at the same time when running code. used for real time refreshing


# Variables to be used for the map and the simulation
# This can be deleted later
merrill_coords = [40.7685, -111.8362] # Merrill engineering building approximate coordinates
u_of_u_bounds = [(40.78, -111.85),  # NW
                 (40.78, -111.82),  # NE
                 (40.76, -111.82),  # SE
                 (40.76, -111.85)]  # SW

# To limit where the simulation populates the coordinates so that it is concentrated on the UofU campus
# Just used for testing and this will be removed when implemented with the antenna system
# Uses the polygon library
u_of_u_polygon = Polygon(u_of_u_bounds)

# This creates the initial UI that the user can use to interact with the system
# Goal is to implement it with the whole system and not just the heatmap portion
# Uses the Tkinter library
root = tk.Tk() # Defines the UI variable
root.title("Heatmap Triangulation") # Title of the window
root.geometry("300x150") # Sets the size of the GUI window

# These variables are essential for storing the array of data fed into this system (in this case, the
# simulation does that) and auto refresh (real-time tracking)
points = [] # Stores the data into an array called "points"
running = False # Sets value to false to signify to the application that the heatmap is not operating

####################################################################################################

# This function generates random latitude and longitude coordinates that will simulate
# what we anticipate when the data from our antenna array goes into our system for the heatmap
# This will not be needed when full implementation to the system is done
def simulator(polygon: Polygon):
    min_lon, min_lat, max_lon, max_lat = polygon.bounds # This makes sure the random points stay within bounds
    while True:
        lon = rd.uniform(min_lon, max_lon) # Pulls a random number within the bounds and stores as lon
        lat = rd.uniform(min_lat, max_lat) # Pulls a random number within the bounds and stores as lat
        point = Point(lon, lat)
        if point.within(polygon):
            return (lon, lat)

#######################################################################################################

# This is the function that creates the initial base map layer. This is needed for full
# mapping capabilities offline. This is because Folium uses Leaflet which uses an internet connection
# to retrieve the javascript and css files needed to run those libraries.
def base_map():

    # This calls the base map layer and sets the coordinates onto the merrill engineering building
    # with zoom starting at 15
    m = folium.Map(location=merrill_coords, zoom_start=15, tiles=None)

    # This is the tile layer that goes over the base map that will pull from the offline map tiles
    # whenever you pull from offline tiles, these must be in the following format:
    # {z}/{x}/{y}.png format which is what Folium uses. The z stands for zoom and then the x and y
    # are the individual tiles and the coordinates for each zoom level.
    folium.TileLayer(tiles="utah_tiles/{z}/{x}/{y}.png",
                     attr="OpenStreetMaps", # attribute OpenStreetMaps
                     name="Utah Heatmap",
                     min_zoom=6, #This needs to match the zoom levels for the file
                     max_zoom=15).add_to(m) # This needs to match the zoom levels for the file

    # This enables the map to be interacted with such as whenever you hover over an area of the map
    # it will display the coordinates on the top right corner
    # Also contains formatting information
    # There is more customization to be done and will have to be done in the .js file of MousePosition
    formatter = "function(num) {return L.Util.formatNum(num, 5) + ' º ';};"
    mouse_position = MousePosition(
        position='topright',
        separator=' | ',
        empty_string='NaN',
        lng_first=False,
        num_digits=20,
        prefix='Coordinates:',
        lat_formatter=formatter,
        lng_formatter=formatter,
    )
    m.add_child(mouse_position) # Adds it to the folium map

    '''# Adds full screen capability for map
    full_screen_toggle = Fullscreen(
        position="bottomleft",
        title="Full Screen",
        title_cancel="Exit Full Screen",
        force_separate_button=False,
    )
    m.add_child(full_screen_toggle)'''

    return m


####################################################################################################

# This is the real-time tracking function.
def realtime_tracking():
    global points, running, window

    # if the running variable is True, then the real time tracking will run the simulator and add to the map
    # This will have to be modified when implemented into full system
    while running:
        new_point = simulator(u_of_u_polygon)
        points.append(new_point)

        m = base_map() # Calls the base map function and stores it in m
        HeatMap(points, radius=40).add_to(m) # adds heatmap layer. The radius is the size of each point on the map
        m.save('heatmap.html')

        # Refresh the mapping window and loads the heatmap.html file to update as data is added
        if window:
            window.load_url('heatmap.html')

        time.sleep(1) # How often the map updates so that data is displayed. Updates ever 1 second


####################################################################################################

# Creates heatmap and displays the map when user hits the "start mapping" button on the UI
def create_heatmap():
    global points, running, window

    if not running: # Once the user presses "start mapping", it will change the value of running to true
        running = True
        points = []

        m = base_map()
        m.save('heatmap.html')

        # This is needed for real time updates and tracking
        threading.Thread(target=realtime_tracking, daemon=True).start()

        # Without this, the mapping window will not update accurately. It stores it as a reference
        # so that you can still see the other points on the heatmap
        window = webview.create_window("Heatmap", "heatmap.html", width=1200, height=1200)
        webview.start()


    else:
        running = False
        if window:
            window.destroy()  # When user hits "close mapping application" it will destroy the data
        window = None

####################################################################################################

# GUI Buttons
# Creates start button and adds it to the UI
start_mapping = tk.Button(root, text="Start Mapping", command=create_heatmap)
start_mapping.pack(pady=10)

# Creates pause button and adds it to the UI
pause_mapping = tk.Button(root, text="Pause Mapping", command=None)
pause_mapping.pack(pady=10)

# Creates the close mapping button and adds it to the UI
close_mapping_app = tk.Button(root, text="Close Mapping Application", command=root.destroy)
close_mapping_app.pack(pady=10)

####################################################################################################

# Loops the tkinter window (UI window)
root.mainloop()

####################################################################################################
# Quality of life fixes
    # add markers that pop up the latest point that pops up?
        # maybe a car icon?
        # Needs to be able to track accurately with the car and the direction of the car, etc.
    # Implement pause mapping
    # Any saving capabilities?

# Documentation
    # To get Folium to work for offline use
        # Download open street map 'map' tiles
            # Use MOBAC to download the tiles
            # Format needs to be in {z}/{x}/{y}.png {zoom}/{x coordinate}/{y coordinate}.png
        # Store tiles in project folder i.e. 'utah_tiles'
        # Folium uses Leaflet which is a Python mapping library and will require specific .js and css files to work offline
            # These can be retrieved from the leaflet github page
                # awesome-markers.js (Needed for markers)
                # awesome_markers_css.css
                # awesome markers font.css
                # awesome rotate css.css
                # bootstrap.js
                # bootstrap.css
                # glyphicons.css
                # jquery.js
                # l.control.mouse position.css
                # l.control.mouseposition.js
                # leaflet.css
                # leaflet.js
                # leaflet-heat.js (for the heatmap)
            # These js and css scripts need to be stored in the project folder i.e. 'static'
            # Folium has a script where you will need to alter the code to retrieve from these js and css files

