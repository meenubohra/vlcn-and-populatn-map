import folium
import pandas

volcano = pandas.read_csv("Volcanoes.txt")
lat = list(volcano["LAT"])
lon = list(volcano["LON"])
elv = list(volcano["ELEV"])


def color_volcanoes(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")

# Volcanoes added as a layer in Contol panel
fgv = folium.FeatureGroup(name='Volcanoes')

for lt, lg, el in zip(lat, lon, elv):
    fgv.add_child(folium.Marker(location=[lt, lg],
                                popup=str(el)+" m", icon=folium.Icon(color=color_volcanoes(el))))

# Population added as a layer in Contol panel
fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'yellow' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
# the latest version of folium nees str for data and not file hence using read() function.


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")


# import folium  # module
# print(dir(folium))  # all the objects(classes,functions) in folium module
# help(folium.Map) #help with Map class parameters and there description

# latitute range -80 to 80 and longitute -180 to 180 ==>map object
# tiles = "Stamen Terrain" ==>its a basemap default id openstreetmap
# map = folium.Map(location=[38.58, -99.09],
#                  zoom_start=6, tiles="Stamen Terrain")

# add child in the map ,icon plugin is object of folium.Icon class
# map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I'am Marker"))

# save the map generated above by pointing the map object to save method
# map.save("Map1.html")  # 53.51639149794159, -2.217951612691518

# create featuregroup,add multiple childs into the group and then add fg to map
# map-->fg-->nultiple childs

# add for loop to add multiple markers
# for cordinates in [[38.2, -99.1], [39.2, -97.1]]:
#     fg.add_child(folium.Marker(location=cordinates,
#                                popup="Hi I'am Marker", icon=folium.Icon(color="green")))


# Layers in MAP ==>BaseLayer ,Point Layer(Volcanoe points/location),Polygon or line layer(All country population(Roads/lines/areas))
# folium.Map() ,folium.Marker(),folium.GeoJson()

# help(folium.GeoJson())
# class GeoJson(folium.map.Layer)
#  |  GeoJson(data, style_function=None, highlight_function=None, name=None, overlay=True, control=True, show=True, smooth_factor=None, tooltip=None, embed=True, popup=None)
# Parameters
#  |  ----------
#  |  data: file, dict or str.

# Examples
# Providing string.
#  |  >>> GeoJson(open('foo.json').read())
#  |
#  |  >>> # Provide a style_function that color all states green but Alabama.
#  |  >>> style_function = lambda x: {'fillColor': '#0000ff' if
#  |  ...                             x['properties']['name']=='Alabama' else
#  |  ...                             '#00ff00'}

# imp feauture group and map
# we can directly create child using map object but to create 60 volcanoe points we need to use 60 map.add_child lines so instead create a loop and add feature group to add the volcanoe points.60 mapp add child means 60 layers of volcxanoe in layercontrol panel as well.
# To generate different layers use different feature group and then call the LayerControl class.
