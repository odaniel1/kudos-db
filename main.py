import pandas as pd

from src import authorize
from src import get_methods
from src import db_methods

token = authorize.get_acces_token()

activities_df = get_methods.get_activities(token, per_page = 200)

# write activities to cache
new_activities_df = db_methods.update_cache(activities_df, 'data/activities_cache.csv', return_new = True)

if new_activities_df is not None:
    kudos = [get_methods.get_kudoers(id,token) for id in new_activities_df['id']]
    kudos_df = pd.concat(kudos,ignore_index=True)

    db_methods.update_cache(kudos_df, 'data/kudos_cache.csv')
