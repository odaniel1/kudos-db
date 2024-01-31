import pandas as pd
import sys

def update_cache(new_df, cache_path, return_new = False):

    # read in cache if available, if not initialise with new_df
    try:
        cache_df = pd.read_csv(cache_path)

    except:
        print(f"No cache found at {cache_path}, initialising with entries from new_df.")
        new_df.to_csv(cache_path, index=False)
        return return_object(new_df, return_new)
    
    # reduce new_df to uncached records
    uncached_df = new_df[~new_df['id'].isin(cache_df['id'])]
    n_new_records = uncached_df.shape[0]

    if n_new_records > 0:
         # append to cache and write to disk
        cache_df = pd.concat([uncached_df, cache_df], ignore_index=True)
        cache_df.to_csv(cache_path, index = False)
        
        print(f"Writing {n_new_records} new records to {cache_path}")
        return return_object(uncached_df, return_new)
    
    else:
        print("No new records available.")
        return
    

def test_df_comparable(df1, df2):
    # remove index columns if they exist
    df1 = df1.reset_index(drop=True)
    df2 = df2.reset_index(drop=True)

    # Compare column names
    if ~df1.columns.equals(df2.columns):
        print(df1.columns)
        print(df2.columns)
        print("Data frames have different column names.")
        sys.exit("Data frames have different column names.")

    if ~df1.dtypes.equals(df2.dtypes):
        print("Data frames have different column types.")
        sys.exit("Data frames have different column types.")

    return

def return_object(obj, x = True):
    if x == True:
        return obj
    else:
        return