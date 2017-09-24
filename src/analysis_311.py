from Boston_311.data_pull import Data_Pull


url = 'https://data.boston.gov/api/action/datastore_search?resource_id=2968e2c0-d479-49ba-a884-4ef523ada3c0&limit=5'
num_records = 20000
case_status = 'all'
neighborhood = 'Jamaica Plain'
department = 'Public Works Department'

# Create a query for Jamaica Plain
back_bay_parking = Data_Pull(url,
                      num_records,
                      case_status,
                      department,
                      neighborhood)

# Get all the data for the Jamaica Plain
jp.list_case_types()
df = jp.return_data()
df
# Write data to a csv
df.to_csv('jp.csv', index = False)
