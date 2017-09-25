import pandas as pd

class Analysis(object):

    def __init__(self, df):

        self.data = df

    def calculate_diff(self):

        data = self.data
        data['open_dt'] = pd.to_datetime(data['open_dt'])
        data['closed_dt'] = pd.to_datetime(data['closed_dt'])
        data['target_dt'] = pd.to_datetime(data['target_dt'])
        data['time_to_close'] = (data['closed_dt'] - data['open_dt']).astype('timedelta64[h]')
        data['time_off_target'] = (data['closed_dt'] - data['target_dt']).astype('timedelta64[h]')


        return data

    def summary_statistics(self, df, fields_to_group, field_to_summarize):

        """
        Fields_to_group is a list of fields.
        """

        df = df

        summaries = []

        for field in fields_to_group:
            summary_df = data.groupby([field])[field_to_summarize].describe()
            print(summary_df)
            summaries.append(summary_df)

        return summaries

    def write_data(self, csv = True):

        data = self.calculate_diff()

        if csv == True:
            data.to_csv('data.csv', index = False)

        elif csv == False:
            data.to_json('data.json', orient = 'columns')
