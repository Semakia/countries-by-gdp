import unittest
import os
import numpy as np
import pandas as pd
from etl_project_gdp import extract_data, transform_data, load_data

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
json_path = '~/projects/etl_prohect_gdp/Countries_by_GDP.json'
# json_path = 'Countries_by_GDP.json'
db_table = 'Countries_by_GDP' 
db_name = 'World_Economies.db'

log_file = 'etl_project_log.txt'

class TestETLProjectGDP(unittest.TestCase):

    def test_extract_data(self):
        # Create an empty DataFrame to simulate df
        df = pd.DataFrame(columns=["Country", "GDP_USD_billion"])
       
        data = extract_data(url, df)
        
        self.assertTrue(len(data) > 0) # Make sure the returned DataFrame contains data

    

if __name__ == '__main__':
    unittest.main()
