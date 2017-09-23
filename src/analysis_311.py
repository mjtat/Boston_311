import urllib
import json
import urllib.request
import pandas as pd
import os
import DataPull
import datetime
from datetime import timedelta

url = 'https://data.boston.gov/api/action/datastore_search?resource_id=2968e2c0-d479-49ba-a884-4ef523ada3c0&limit=5'
num_records = 100
case_status = 'Closed'

df = Data_Pull(url, num_records, case_status).calculate_diff()
df
