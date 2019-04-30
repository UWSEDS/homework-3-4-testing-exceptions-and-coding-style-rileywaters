'''Includes functions for reading in dataframes from urls'''

import io
import requests
import pandas as pd


def read_weather_data():
    '''Reads in a weather dataframe from a url containing information about
    Seattle weather stations, their air temperature, and the reading datetime'''

    # Read in three rows of the csv and store as pandas dataframe
    url = 'https://data.seattle.gov/api/views/egc4-d24i/rows.csv?accessType=DOWNLOAD'
    weather_content = requests.get(url).content
    data_frame = pd.read_csv(io.StringIO(weather_content.decode('utf-8')))
    data_frame = data_frame[['StationName', 'DateTime', 'AirTemperature']]

    # Validate the column names
    valid_col_list = ['StationName', 'DateTime', 'AirTemperature']
    for valid_col_name in valid_col_list:
        if not valid_col_name in data_frame.columns:
            raise ValueError('Error: Unexpected column names.')
    return data_frame
