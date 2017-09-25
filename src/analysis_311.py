from Boston_311.data_pull import Data_Pull
from Boston_311.analysis import Analysis


url = 'https://data.boston.gov/api/action/datastore_search?resource_id=2968e2c0-d479-49ba-a884-4ef523ada3c0&limit=5'
num_records = 400
case_status = 'all'
neighborhood = 'Jamaica Plain'
department = 'Public Works Department'

# Create a query for Jamaica Plain
jp = Data_Pull(url,
               num_records,
               case_status,
               department,
               neighborhood)

# Get all the data for the Jamaica Plain
jp.get_cases()

df = jp.return_data()

df_analysis = Analysis(df)

df_analysis.calculate_diff()
df_analysis.write_data(csv = True)
