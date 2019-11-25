import gpxpy
import pandas as pd
import geojson

gpx_file = open('test.gpx', 'r')  # read gpx file
gpx = gpxpy.parse(gpx_file)  # extract data from gpx file

# read and record trackpoints
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            trkpt_data = segment.points

trkpt_df = pd.DataFrame(columns=['lon', 'lat', 'alt'])

for point in trkpt_data:
    trkpt_df = trkpt_df.append({'lon': point.longitude, 'lat': point.latitude, 'alt': point.elevation},
                               ignore_index=True)

# read and record waypoints
for waypoint in gpx.waypoints:
    wpt_data = gpx.waypoints

wpt_df = pd.DataFrame(columns=['lon', 'lat'])

for waypoint in wpt_data:
    wpt_df = wpt_df.append({'lon': waypoint.longitude, 'lat': waypoint.latitude}, ignore_index=True)

# write dataframes to geoJSON
coordinates = []
trkpt_df.apply(lambda X: coordinates.append([X['lon'], X['lat'], X['alt']]), axis=1)

coordinates2 = []
wpt_df.apply(lambda X: coordinates2.append([X['lon'], X['lat']]), axis=1)

my_line =  geojson.LineString(coordinates)
my_line2 = geojson.LineString(coordinates2)

features = [geojson.Feature(geometry=my_line, properties={"name": "Trackpoints"}),
            geojson.Feature(geometry= my_line2, properties={"name": "Waypoints"})]
feature_collection = geojson.FeatureCollection(features)

with open('map.geojson', 'w') as fp:
    geojson.dump(feature_collection, fp)
