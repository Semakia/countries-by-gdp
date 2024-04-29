

import os
import numpy as np
import pandas as pd
import requests
import sqlite3
from datetime import datetime
import xml.etree.ElementTree as EM
from bs4 import BeautifulSoup



url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
json_path = '~/projects/etl_prohect_gdp/Countries_by_GDP.json'
# json_path = 'Countries_by_GDP.json'
db_table = 'Countries_by_GDP' 
db_name = 'World_Economies.db'

log_file = 'etl_project_log.txt'

# create an empty data frame to hold extracted data 
df = pd.DataFrame(columns=["Country", "GDP_USD_billion"])



def extract_data(url, df) :
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')
    tables = data.find_all('tbody')
    rows = tables[2].find_all('tr')

    # extract from url 
    for row in rows :
        col = row.find_all('td')
        
        if len(col)>=3 :
            country_link = col[0].find('a')
            if country_link:
                country = country_link.get_text(strip=True)
            else:
                country = col[0].get_text(strip=True)
            
            # convert the value of gdp in float
            gdp_value = col[2].contents[0].replace(",", "").replace(".", "")  
            if gdp_value == '—':
                # Si la valeur est '—', vous pouvez la remplacer par NaN ou ignorer cette entrée
                gdp_value = np.nan
            else:
                gdp_value = float(gdp_value) 
            data_dict ={"Country" : country,
                        "GDP_USD_billion" : gdp_value

                        }
            df1 = pd.DataFrame(data_dict, index = [0])
            df = pd.concat([df, df1], ignore_index = True)
    
    return df 


def transform_data(data) :
    #process the data 
    data['GDP_USD_billion'] = round(data['GDP_USD_billion'], 2) #rounding GDP_USD_billion to 2 decimal places
    return data
        
    
def load_data(data, db_name, db_table, target_file) :
    data.to_json(target_file)
    conn = sqlite3.connect(db_name)
    data.to_sql(db_table, conn, if_exists='replace', index=False)
    conn.close()


def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now() #get current timestmap
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + ',' + message + '\n')


def execute_query(query, db_name) :
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    result = cursor.execute(query)
    return result







#log the intialization of the ETL process
log_progress('ETL process started')

#log the beginning of the Extraction process

log_progress('Extraction started')
data_extracted = extract_data(url, df)

#log the completion of the extraction process
log_progress('Extraction finished')

#log the beginning of the transform process
log_progress('Transforming started')

data_processed = transform_data(data_extracted)
print(data_processed)

#log the completion of transform process
log_progress('Transforming finished')

#log the beginning of the transform process
log_progress('Loading started')

load_data(data_processed, db_name, db_table, json_path)

#log the completion of the transform process
log_progress('Loading finished')

#log the completion of the ETL process
log_progress('ETL process finished !')



# Get the countries which have gdp more thant 100 USD Billion

countries_more_than_100 = execute_query("SELECT * FROM Countries_by_GDP WHERE GDP_USD_billion >= 100 ", db_name)

for row in countries_more_than_100 :
    print(row)

