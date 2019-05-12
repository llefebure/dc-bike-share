"""Download and preprocess data for analysis

All of the raw data files are obtained from:
https://s3.amazonaws.com/capitalbikeshare-data/index.html
"""
import os
import logging
import zipfile
from urllib.request import urlretrieve

from src import HOME_DIR

FILENAME_FORMAT = "{}-capitalbikeshare-tripdata.zip"
REMOTE_PATH = "https://s3.amazonaws.com/capitalbikeshare-data/"
LOCAL_PATH = os.path.join(HOME_DIR, "data/external/")

def download_data(
    versions=["201901", "201902", "201903", "201904"]
):
    for version in versions:
        filename = FILENAME_FORMAT.format(version)
        destination = os.path.join(LOCAL_PATH, filename)
        if os.path.exists(destination):
            logging.info("Path already exists {}", destination)
        else:
            url = os.path.join(REMOTE_PATH, filename)
            logging.info("Downloading {}", url)
            urlretrieve(url, destination)

def unzip_files():
    zipped_files = filter(lambda x: x.endswith(".zip"), os.listdir(LOCAL_PATH))
    for zipped_file in zipped_files:
        zipped_path = os.path.join(LOCAL_PATH, zipped_file)
        if os.path.isfile(zipped_path.replace("zip", "csv")):
            logging.info("File already unzipped {}", zipped_path)
        zip_ref = zipfile.ZipFile(zipped_path, "r")
        zip_ref.extractall(LOCAL_PATH)
        zip_ref.close()

if __name__ == "__main__":
    download_data()
    unzip_files()
