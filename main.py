import pandas as pd
from geopy.geocoders import Nominatim
import time

# Load the National ChargePoint Registry CSV file into a Pandas dataframe
df = pd.read_csv('national-charge-point-registry1.csv')

# Split the dataframe into multiple dataframes with 1000 rows each
dfs = [df[i:i + 500] for i in range(0, len(df), 500)]

# Initialize a geolocator object to get the county information from latitude and longitude coordinates
geolocator = Nominatim(user_agent='my_app')

# Loop over each dataframe and add a county column to each row
for i, df in enumerate(dfs):
    # Initialize an empty county column
    df['county'] = ''

    # Loop over each row in the dataframe and add the county information
    for j, row in df.iterrows():
        lat = row['latitude']
        lon = row['longitude']

        # Use geopy's Nominatim geolocator to get the county information from latitude and longitude coordinates
        location = geolocator.reverse(f'{lat}, {lon}', timeout=None)
        county = location.raw['address']['county'] if 'county' in location.raw['address'] else ''

        # Set the county value for the current row
        df.at[j, 'county'] = county

        # Print the row count for each row processed
        print(f"Processed row {j + 1} of {len(df)} for dataframe {i + 1} of {len(dfs)}")

        # Wait for one second after each row
        time.sleep(0.50)


    # Save the current dataframe to a CSV file
    df.to_csv(f'df_{i + 1}.csv', index=False)

    # Print the first 10 rows of the dataframe with the added county column
    print(df.head(10))