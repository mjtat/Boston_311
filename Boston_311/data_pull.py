from urllib import request
import urllib
import json
from json import *
import pandas as pd

class Data_Pull(object):

    """
    This object retrieve Boston 311 data. It is initialized with the following
    information:

    url: A CKAN url from data.boston.gov

    num_records: The number of records to retrieve

    case_status: "Open", "Closed", or "all"

    neighborhood: A Boston neighborhood, e.g. "Jamaica Plain", "Roxbury". "all" by
    default.

    case_type: A 311 case_type e.g. "Parking Enforcement", "Requests for Street
    Cleaning"

    calculate_diff: True or False. If true, time difference between open and close dates
    is generated as a column in the resulting data frame.

    """


    def __init__(self,
                url,
                num_records,
                case_status = 'all',
                department = 'all',
                neighborhood = 'all',
                case_type = 'all',
                calculate_diff = False):

        self.url = url
        self.num_records = num_records
        self.case_status = case_status
        self.department = department
        self.neighborhood = neighborhood
        self.case_type = case_type

    def read_url(self):

        """
        read_url() takes a CKAN url, then translates the resulting json
        into a pandas dataframe.
        """

        url = str(self.url)
        num_records = str(self.num_records)
        url = url[0:-1] + num_records
        fileobj = urllib.request.urlopen(url)
        file = json.loads(fileobj.read().decode('utf-8'))
        df = pd.DataFrame.from_dict(file['result']['records'])

        return df

    def get_cases(self):

        """
        get_cases() takes a data frame of 311 results, and subsets it such that
        all the results are open, closed, or both.
        """

        #print('Getting {} cases...'.format(self.num_records))

        df = self.read_url()

        if self.case_status == 'all':
            return df

        elif self.case_status == 'Open':
            df = df[df['CASE_STATUS'] == 'Open']
            return df

        else:
            df = df[df['CASE_STATUS'] == 'Closed']
            return df

    def list_case_types(self):

        df = self.get_cases()
        case_types = df['TYPE'].unique()

        for case_type in case_types:
            if case_type is None:
                continue

            else:
                print(case_type)

    def list_neighborhoods(self):

        df = self.get_cases()
        neighborhoods = df['neighborhood'].unique()

        for neighborhood in neighborhoods:
            if neighborhood is None:
                continue

            else:
                print(neighborhood)

    def select_department(self, df):
        df = df

        if self.department == 'all':
            print('Selecting from all departments...')
            return df

        else:
            print('Selecting from {} deparment...'.format(self.department))
            df = df[df['SUBJECT'] == self.department]
            return df

    def select_case_type(self, df):

        print('Selecting {}'.format(self.case_type))

        if self.case_type == 'all':
            df = df
            return df

        else:
            df = df
            df = df[df['TYPE'] == self.case_type]
            return df

    def select_neighborhood(self, df):

        print('Selecting cases in {}'.format(self.neighborhood))
        if self.neighborhood == 'all':
            return df

        else:
            df = df
            df = df[df['neighborhood'] == self.neighborhood]
            return df

    def return_data(self):

        print('Retrieving data...')
        df = self.get_cases()
        df = self.select_department(df)
        df = self.select_case_type(df)
        df = self.select_neighborhood(df)
        print('{} number of entries retrieved after case and neighborhood selection'.format(len(df)))

        return df
