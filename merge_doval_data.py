import pandas as pd
import os

# This program sets the working directory to the folder where this script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# This program loads Statcast and FanGraphs datasets for Camilo Doval
statcast = pd.read_csv('camilo_doval_5yr_statcast.csv')
fangraphs = pd.read_csv('doval_advanced_stats.csv')

# This program converts game_date to datetime and extracts the season year
statcast['game_date'] = pd.to_datetime(statcast['game_date'], errors='coerce')
statcast['Season'] = statcast['game_date'].dt.year

# This program aggregates Statcast data by season and averages key metrics
statcast_summary = statcast.groupby('Season').agg({
    'release_speed': 'mean',
    'release_spin_rate': 'mean',
    'release_extension': 'mean'
}).reset_index()

# This program rounds values for easier viewing and interpretation
statcast_summary = statcast_summary.round(2)

# This program merges FanGraphs season-level data with Statcast averages using the Season column
merged = pd.merge(fangraphs, statcast_summary, on='Season', how='left')

# This program saves the combined dataset as a new CSV file
merged.to_csv('doval_complete_profile.csv', index=False)
print('Merged dataset saved to doval_complete_profile.csv')
