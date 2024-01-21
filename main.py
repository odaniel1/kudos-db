import pandas as pd

from src import authorize
from src import get_methods

token:str = authorize.get_acces_token()

activities = get_methods.get_activities(token)

kudos = [get_methods.get_kudoers(id,token) for id in activities['id']]
kudos_df = pd.concat(kudos,ignore_index=True)

kudos_summary = kudos_df.groupby(['name'])['name'].count().reset_index(name='count')
kudos_summary = kudos_summary.sort_values(['count'], ascending=False)

print(kudos_summary.to_string())
