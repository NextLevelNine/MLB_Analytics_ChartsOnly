from pybaseball import pitching_stats
import pandas as pd

# Load pitching stats for a single year
df = pitching_stats(2023)

# Print all unique pitcher names to see how Camilo Doval appears
pd.set_option('display.max_rows', None)  # Show all rows
print(df[['Name']].drop_duplicates().sort_values('Name'))
