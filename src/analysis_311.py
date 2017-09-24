import urllib
import json
import urllib.request
import pandas as pd
from Boston_311.data_pull import Data_Pull


url = 'https://data.boston.gov/api/action/datastore_search?resource_id=2968e2c0-d479-49ba-a884-4ef523ada3c0&limit=5'
num_records = 10000
case_status = 'Closed'
neighborhood = 'Back Bay'
case_type = 'Parking Enforcement'

query_one = Data_Pull(url,
                      num_records,
                      case_status,
                      neighborhood,
                      case_type)

cases = query_one.list_case_titles()

neighborhoods = query_one.list_neighborhoods()

query_one_df = query_one.calculate_diff(query_one_df)

query_one_df
