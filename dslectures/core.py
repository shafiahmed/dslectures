# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/00_core.ipynb (unless otherwise specified).

__all__ = ['get_dataset']

# Cell
from nbdev.showdoc import *
import wget
import os

# Cell
def get_dataset(dataset_name: str):
    """
    Download datasets from Google Drive.
    """

    name_to_id = {
        "word2vec-google-news-300.pkl": "1dRwSXbFTcQbn8c3V24G92wFY4DXZ1SDt",
        "imdb.csv": "1wF0YEmQOwceJz2d6w4CfhBgydU87dPGl",
        "housing.csv": "1d7oOKdDmZFx8wf0c8OfuTW1FpUyJHABh",
        "housing_gmaps_data_raw.csv": "1R1RUHAXxzrIngRJMFwyp4vZRVICd-I6T",
        "housing_addresses.csv": "1mOK0uyRz5Zs-Qo7mVMlxwtb2xn1E6N9Q",
        "housing_merged.csv": "1bdYuBtIPrKiU-ut2MeSSsL47onPtZrRt"
    }

    path = '../data/'
    gdrive_path = "https://docs.google.com/uc?export=download&id="
    if dataset_name in name_to_id:
        if os.path.exists(path + dataset_name):
            print(f"Dataset already exists at '{path + dataset_name}' and is not downloaded again.")
            return
        try:
            file_url =  gdrive_path + name_to_id[dataset_name]
            wget.download(file_url, out=path)
        except Exception as e:
            print("Something went wrong during download. Try again.")
            raise e
        print(f"Download of {dataset_name} dataset complete.")
    else:
        raise KeyError("File not on Google Drive.")