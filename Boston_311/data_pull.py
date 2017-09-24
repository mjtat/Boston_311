import urllib
import json
from json import *
import pandas as pd
from urllib import request

class Data_Pull(object):

    def __init__(self,
                url,
                num_records,
                case_status,
                neighborhood = 'all',
                case_type = 'all'
                calculate_diff = False):

        self.url = url
        self.num_records = num_records
        self.case_status = case_status
        self.neighborhood = neighborhood
        self.case_type = case_type

    def read_url(self):

        url = str(self.url)
        num_records = str(self.num_records)
        url = url[0:-1] + num_records
        fileobj = urllib.request.urlopen(url)
        file = json.loads(fileobj.read().decode('utf-8'))
        df = pd.DataFrame.from_dict(file['result']['records'])

        return df

    def get_cases(self):

        df = self.read_url()
        df = df[df['CASE_STATUS'] == self.case_status]

        return df

    def list_case_types(self):

        df = self.get_cases()
        case_types = df['TYPE'].unique()

        for case_type in case_types:
            if case_type is NULL:
                continue

            else:
                print(case_type)

    def list_neighborhoods(self):

        df = self.get_cases()
        neighborhoods = df['neighborhood'].unique()

        for neighborhood in neighborhoods:
            if neighborhood is NULL:
                continue

            else:
                print(neighborhood)

    def select_case_type(self, df):

        if self.case_type == 'all':
            return df

        else:
            df = df
            df = df[df['TYPE'] == self.case_type]
            return df

    def select_neighborhood(self, df):

        if self.neighborhood == 'all':
            return df

        else:
            df = df
            df = df[df['neighborhood'] == self.neighborhood]
            return df

    def calculate_diff(self, df):

        df = df
        df['open_dt'] = pd.to_datetime(df['open_dt'])
        df['closed_dt'] = pd.to_datetime(df['closed_dt'])
        df['time_to_close'] = (df['closed_dt'] - df['open_dt']).astype('timedelta64[h]')

        return df

    def return_data(self):

        df = self.get_cases()
        df = self.select_case_type(df)
        df = self.select_neighborhood(df)

        return df
