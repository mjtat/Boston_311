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
|   | analysis.py
|
+---src
|   |
|   | analysis_311.py
|
| README.md
```
Usage
--------

Clone this directory. At the moment, place any analysis script in the `src` directory. Import the package using the following commands: `from Boston_311.data_pull import Data_Pull` and `from Boston_311.analysis import Analysis`.

Methods in Boston_311
-----------------------

**The class `Data_Pull` takes five arguments: url, num_records, case_status, neighborhood, and case_type.**

* `url`: The API url taken from the Boston 311 open dataset. An example of this is as follows:
```
url  = 'https://data.boston.gov/api/action/datastore_search?resource_id=2968e2c0-d479-49ba-a884-4ef523ada3c0&limit=5'
```
* `num_records`: The number of records to retrieve. An integer between 0 and the total
number of 311 records.

* `case_status`: Either "Open", or "Closed".

* `neighborhood`: A neighborhood in Boston (e.g., "Jamaica Plain"). Default is set to 'all'.

* `case_type`: A case type (e.g., 'Parking Enforcement'). Default is set to 'all'.

**There are several helper functions.**

* `read_url()` takes the url and reads the data.
into a DataFrame.  

* `get_cases()` retrieves open or closed cases.

* `list_case_titles()` lists all case types.

* `list_neighborhoods()` lists all neighborhoods.

* `select_case_type()` selects the case type. The default selects all cases, unless otherwise specified.

* `select_neighborhood()` selects the appropriate neighborhood (e.g., 'Roxbury', 'Jamaica Plain'). The default selects all neighborhoods unless otherwise specified.

* `select_department()` selects the department of interest (e.g., 'Public Works Department'). The default selects all unless otherwise specified.

* `return_data()` returns all the requested data in the pipeline.

*NOTE*: helper functions can be run individually, though if you only care to return all the data, all at once, the `return_data()` method should be the only one you should care about.

**The class `Analysis` takes one argument: a data frame with which to do some basic analyses on. This class also has several helper functions.**

* `calculate_diff()` takes a 311 data frame, converts the `open_dt` and `close_dt` columns to the appropriate datetime format, then finds their difference in hours, creating a column titled `time_to_close`. Additionally, it takes the difference between `close_dt` and `target_dt` to determine how on or off time (in hours), a request was. This returns a data frame that can be fed into other methods.

* `summary_statistics()` takes three arguments: a 311 data frame, different fields to group by (a list of strings, e.g., ['REASON', 'Source']) and a field to get summary stats on (e.g., time_to_close). This returns a list of data frames that consist of basic summary statistics for the different fields you specified.

* `write_data()` takes two arguments, a 311 dataframe, and csv (set to True by default). Setting csv == True outputs a csv file, setting csv to false outputs as JSON file.S
