import pandas as pd 
from sklearn.neighbors import BallTree
import numpy as np

traffic_df = pd.read_csv('data/Traffic_Crashes.csv')
red_light_df = pd.read_csv('data/Red_Light.csv')

#Longitutde and latitude boundaries cleaning, based on the following locations: 
upper_left_lat = 41.954500 #W Irving Park Rd
upper_left_lon = -87.745480 #Cicero Ave
lower_right_lat = 41.765300 #71st St
lower_right_lon = -87.550018 #Lake Michigan


def clean_dataframe(df):
    df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])
    df = df[(df['LATITUDE'] >= lower_right_lat) & (df['LATITUDE'] <= upper_left_lat) &
            (df['LONGITUDE'] >= upper_left_lon) & (df['LONGITUDE'] <= lower_right_lon)]
    return df

#drop rows with missing values in INJURIES_TOTAL and filter for relevant traffic control devices that indicate intersections
traffic_df = clean_dataframe(traffic_df)
traffic_df = traffic_df.dropna(subset=['INJURIES_TOTAL'])
traffic_df = traffic_df[traffic_df['TRAFFIC_CONTROL_DEVICE'].isin(['FLASHING CONTROL SIGNAL', 'TRAFFIC SIGNAL'])]

red_light_df = clean_dataframe(red_light_df)

#write cleaned dataframes to new csv files
traffic_df.to_csv('data/cleaned_Traffic_Crashes.csv', index=False)
red_light_df.to_csv('data/cleaned_Red_Light.csv', index=False)

red_light_df = red_light_df.reset_index(drop=True)
red_light_df['red_light_id'] = np.arange(1, len(red_light_df) + 1)

# convert to radians for haversine distance
traffic_rad = np.radians(traffic_df[['LATITUDE', 'LONGITUDE']].values)
red_rad = np.radians(red_light_df[['LATITUDE', 'LONGITUDE']].values)

# build spatial index on red light cameras
tree = BallTree(red_rad, metric='haversine')

# find nearest red light camera for each crash
dist, ind = tree.query(traffic_rad, k=1)
traffic_df['dist_to_red_light_m'] = dist[:, 0] * 6371000  # Earth radius in meters

# threshold = 50 meters for "near" a red light camera
threshold = 50

# create binary indicator
traffic_df['has_red_light'] = (traffic_df['dist_to_red_light_m'] <= threshold).astype(int)
traffic_df['matched_red_light_id'] = red_light_df.iloc[ind[:, 0]]['red_light_id'].values


traffic_matched_df = traffic_df.copy()
cols_to_keep = [
    'CRASH_RECORD_ID',
    'CRASH_DATE',
    'POSTED_SPEED_LIMIT',
    'INJURIES_TOTAL',
    'INJURIES_FATAL',
    'INJURIES_INCAPACITATING',
    'INJURIES_NON_INCAPACITATING',
    'INJURIES_REPORTED_NOT_EVIDENT',
    'INJURIES_NO_INDICATION',
    'INJURIES_UNKNOWN',
    'LATITUDE',
    'LONGITUDE',
    'dist_to_red_light_m',
    'has_red_light',
    'matched_red_light_id'
]

traffic_matched_df = traffic_matched_df[cols_to_keep]
traffic_matched_df.to_csv('data/crashes_camera.csv', index=False)
