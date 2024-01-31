# adapted from https://github.com/Cloudy17g35/strava-api/tree/main
import requests
import pandas as pd

def get_activities(access_token, per_page = 30):
    # get data from strava api
    headers = {'Authorization': f'Authorization: Bearer {access_token}'}
    activities = requests.get(f"https://www.strava.com/api/v3/athlete/activities?per_page={per_page}", headers=headers).json()
    
    # cast to dataframe, retaining only required fields
    activities_df = pd.json_normalize(activities)
    activities_df = activities_df[['id', 'start_date', 'trainer', 'distance', 'average_speed', 'total_elevation_gain', 'type']]
    
    return activities_df

def get_kudoers(activity_id, access_token):
    # get data from strava api
    headers = {'Authorization': f'Authorization: Bearer {access_token}'}
    url = "https://www.strava.com/api/v3/activities/"+str(activity_id)+"/kudos"
    kudoers = requests.get(url, headers=headers).json()

    # cast to dataframe, retaining only required fields
    kudoers_df = pd.json_normalize(kudoers)

    if len(kudoers_df) == 0:
        kudoers_df = pd.DataFrame(columns=['firstname', 'lastname'])

    kudoers_df['name'] = kudoers_df['firstname']+ ' ' + kudoers_df['lastname']
    kudoers_df.insert(0, 'activity_id', activity_id)
    kudoers_df = kudoers_df[['activity_id', 'name']]
    
    return kudoers_df