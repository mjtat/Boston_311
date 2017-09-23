# Boston_311 Data Munging Package

This package can be used to do some simple operations using the Boston 311 data set.

Directory Structure
---------------------
```
root
|
+---Boston_311
|   |
|   | data_pull.py
|
+---src
|   |
|   | analysis_311.py
|
| README.md
```
Usage
--------

Clone this directory. At the moment, place any anlysis script in the `src`
directory. Import the package using the following command: `from Boston_311.data_pull import Data_Pull`.

*Methods in Boston_311*
The class `Data_Pull` takes three arguments: url, num_records, and case_status.
* url: The API url taken from the Boston 311 open dataset. An example of this is as follows:
```
url  = 'https://data.boston.gov/api/action/datastore_search?resource_id=2968e2c0-d479-49ba-a884-4ef523ada3c0&limit=5'
```
* num_records: The number of records to retrieve. An integer between 0 and the total
number of 311 records.

* case_status: Either "Open", or "Closed".

There are several helper functions. `read_url()` takes the url and reads the data
into a DataFrame. `get_cases()` retrieved open or closed cases. `calculate_diff()`
takes the difference in time between closed and opened cases, and returns a number
in hours.
