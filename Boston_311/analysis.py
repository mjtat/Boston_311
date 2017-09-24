import pandas as pd

class Analysis(object):

    def __init__(self, df):
        
        self.data = df

    def calculate_diff(self):

        data = self.data
        data['open_dt'] = pd.to_datetime(data['open_dt'])
        data['closed_dt'] = pd.to_datetime(data['closed_dt'])
        data['time_to_close'] = (data['closed_dt'] - data['open_dt']).astype('timedelta64[h]')

        return data

    def write_data(self, csv = True, json = False):

        data = self.calculate_diff()

        if csv == True:
            data.to_csv('data.csv', index = False)

        elif csv == False and json == True:
            data.to_json('data.json', orient = 'columns')
