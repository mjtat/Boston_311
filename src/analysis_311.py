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

# Create a query for back bay parking enforcement
back_bay_parking = Data_Pull(url,
                      num_records,
                      case_status,
                      neighborhood,
                      case_type)

# Get all the data for the back bay
df = back_bay_parking.return_data()

# Write data to a csv
df.to_csv('back_bay.csv', index = False)
