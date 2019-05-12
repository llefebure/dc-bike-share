"""Utils for loading data"""
import pandas as pd
import os

from src import HOME_DIR

def load_trip_data():
    trip_data_files = filter(
        lambda x: x.endswith("csv"),
        os.listdir(os.path.join(HOME_DIR, "data/external"))
    )
    all_data = pd.concat([
        pd.read_csv(os.path.join(HOME_DIR, "data/external", filename))
        for filename in trip_data_files
    ])
    all_data["Start date"] = pd.to_datetime(all_data["Start date"])
    all_data["End date"] = pd.to_datetime(all_data["End date"])
    all_data = all_data.reindex()
    return all_data
