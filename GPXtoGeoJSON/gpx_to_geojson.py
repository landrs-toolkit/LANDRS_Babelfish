import gpxpy
import pandas as pd
import geojson
import xml.etree.ElementTree as ET


def read_gpx(filename):
    gpx_file = open(filename, 'r')  # read gpx file
    gpx = gpxpy.parse(gpx_file)  # extract data from gpx file
    return gpx

def read_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return root


def get_trkpts(parsed_gpx):
    # read and record trackpoints
    for track in parsed_gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                trkpt_data = segment.points
                # extensions = point.extensions
    return trkpt_data
    # return extensions


def get_trkptDF(trkpt_data):
    trkpt_df = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time', 'course'])

    for point in trkpt_data:
        trkpt_df = trkpt_df.append({'lon': point.longitude, 'lat': point.latitude, 'alt': point.elevation,
                                    'time': point.time, 'course': point.course}, ignore_index=True)
    return trkpt_df


def get_wpts(parsed_gpx):
    # read and record waypoints
    for waypoint in parsed_gpx.waypoints:
        wpt_data = gpx.waypoints
    return wpt_data


def get_wptDF(wpt_data):
    wpt_df = pd.DataFrame(columns=['lon', 'lat'])
    for waypoint in wpt_data:
        wpt_df = wpt_df.append({'lon': waypoint.longitude, 'lat': waypoint.latitude}, ignore_index=True)
    return wpt_df


def write_geojson(trkpt_df, wpt_df, root):
    # write dataframes to geoJSON
    trkpt_coordinates = []
    trkpt_df.apply(lambda X: trkpt_coordinates.append([X['lon'], X['lat']]), axis=1)

    wpt_coordinates = []
    wpt_df.apply(lambda X: wpt_coordinates.append([X['lon'], X['lat']]), axis=1)

    trkpt_line = geojson.LineString(trkpt_coordinates)
    wpt_line = geojson.LineString(wpt_coordinates)

    altitude = []
    trkpt_df.apply(lambda X: altitude.append(X['alt']), axis=1)
    time = []
    trkpt_df.apply(lambda X: time.append(X['time'].__str__()), axis=1)
    course = []
    trkpt_df.apply(lambda X: course.append(X['course']), axis=1)

    pitch = []
    for trkpt in root.iter('{http://www.topografix.com/GPX/1/1}pitch'):
        pitch.append(float(trkpt.text))

    roll = []
    for trkpt in root.iter('{http://www.topografix.com/GPX/1/1}roll'):
        roll.append(float(trkpt.text))

    features = [geojson.Feature(geometry=trkpt_line, properties={"name": "Trackpoints", "altitude": altitude,
                                                                 "time": time, "course": course, "roll": roll, "pitch": pitch}),
                geojson.Feature(geometry=wpt_line, properties={"name": "Waypoints"})]

    feature_collection = geojson.FeatureCollection(features)

    with open('map.geojson', 'w') as fp:
        geojson.dump(feature_collection, fp)


gpx = read_gpx('test.gpx')
root = read_xml('test.gpx')
# print(gpx)
trkpt_data = get_trkpts(gpx)
# print(trkpt_data)
trkpt_df = get_trkptDF(trkpt_data)
wpt_data = get_wpts(gpx)
wpt_df = get_wptDF(wpt_data)
write_geojson(trkpt_df, wpt_df, root)


