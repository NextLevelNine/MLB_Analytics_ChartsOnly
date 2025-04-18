# This program imports required libraries: pybaseball to pull Statcast data and pandas to manage it
from pybaseball import playerid_lookup, statcast_pitcher
import pandas as pd
import os

# This program sets the working directory to the location of this script
# This ensures files are saved in the same folder as the script, regardless of where it's run from
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# This program looks up Camilo Doval’s MLB player ID using his first and last name
# The playerid_lookup function returns a table with multiple ID types
player_info = playerid_lookup('Doval', 'Camilo')
print(player_info)

# This program uses the MLBAM ID (from the lookup table above)
# The ID is stored in the 'key_mlbam' column, which is what Statcast uses
doval_id = int(player_info.loc[0, 'key_mlbam'])

# This program initializes an empty DataFrame to collect all pitch-level data across seasons
all_data = pd.DataFrame()

# This program loops over each year and pulls Statcast data for Camilo Doval between March 1 and October 31
# This range typically covers the full regular season
for year in range(2020, 2026):  # Includes 2020–2025
    print(f"Fetching data for {year}...")
    season_data = statcast_pitcher(f"{year}-03-01", f"{year}-10-31", player_id=doval_id)
    all_data = pd.concat([all_data, season_data], ignore_index=True)

# This program saves the full 5-year dataset as a CSV file for later analysis or visualization
all_data.to_csv("camilo_doval_5yr_statcast.csv", index=False)
print("Data saved to camilo_doval_5yr_statcast.csv")
