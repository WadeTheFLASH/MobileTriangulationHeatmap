# MobileTriangulationHeatmap

Simulates real-time tracking of WiFi sources using randomized latitude and longitude coordinates, visualized as a heat map. The long-term goal is to integrate real data from an antenna array system to replace the simulated values.

## 🔧 Tech Stack
- Python
- Folium
- tkinter
- JavaScript
- CSS
- OpenStreetMaps

## 🚀 Getting Started

## Installation
1. Clone or download the repository.
2. Download the `heatmap.py` script.
3. Download the required JavaScript and CSS files (included in this repo).
4. Place all files in the same directory.

## Optional: Download Map Tiles
To enable offline use or improve tile loading:
- Use MOBAC (Mobile Atlas Creator).
- Save the map tiles in the format: `/z/x/y.png`.

## ▶️ Running the App
1. Open a terminal or command prompt.
2. Navigate to the folder containing `heatmap.py`.
3. Run the script: bash python heatmap.py (A user interface should appear to help you generate the heat map.)

## 📋 Usage
Instructions are embedded as comments within heatmap.py. These guide the user through customizing coordinates, adjusting simulation parameters, and rendering the map.

## ✨ Features
Simulates real-time tracking of WiFi signal sources.
Interactive UI with tkinter.
Generates dynamic heat maps using Folium and OpenStreetMaps.
Prepares for future integration with real-world antenna array data.

## 👤 Contributors
Danny as a member of the Mobile Radio Triangulation Student team at the University of Utah

## ❓ FAQ
Q: Can I use this with real GPS or signal data?
A: Not yet — but that’s the end goal! Right now, the system uses randomized coordinates for simulation.

Q: Why use MOBAC?
A: MOBAC helps download map tiles so you can use them offline or avoid slow loading.

Q: What data is needed to replace the simulation?
A: The system will eventually accept GPS coordinates and AoA (Angle of Arrival) data from a mobile antenna array.

Q: Do I need internet to run the map?
A: No as long as you download the necessary js and css files in the repo. You will need to predownload the map tiles i.e. MOBAC.

## 📄 License
This project is currently not licensed. Feel free to explore and experiment, but please contact before redistributing or using in commercial applications.
