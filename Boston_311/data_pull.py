import urllib
import json
from json import *
import pandas as pd
from urllib import request

class Data_Pull(object):

    def __init__(self, url, num_records, case_status):
        self.url = url
        self.num_records = num_records
        self.case_status = case_status

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

    def calculate_diff(self):

        df = self.get_cases()
        df['open_dt'] = pd.to_datetime(df['open_dt'])
        df['closed_dt'] = pd.to_datetime(df['closed_dt'])
        df['time_to_close'] = (df['closed_dt'] - df['open_dt']).astype('timedelta64[h]')

        return df
