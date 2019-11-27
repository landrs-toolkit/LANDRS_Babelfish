import gpxpy
import pandas as pd

gpx_file = open('test.gpx', 'r')
gpx = gpxpy.parse(gpx_file)

# read and record the trackpoints
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            trkpt_data = segment.points

trkpt_df = pd.DataFrame(columns=['lon', 'lat', 'alt'])

for point in trkpt_data:
    trkpt_df = trkpt_df.append({'lon': point.longitude, 'lat': point.latitude, 'alt': point.elevation},
                               ignore_index=True)

# read and record the waypoints
for waypoint in gpx.waypoints:
    wpt_data = gpx.waypoints

wpt_df = pd.DataFrame(columns=['lon', 'lat'])

for waypoint in wpt_data:
    wpt_df = wpt_df.append({'lon': waypoint.longitude, 'lat': waypoint.latitude}, ignore_index=True)

