import os
import pandas as pd
import matplotlib.pyplot as plt

# This program sets the working directory to the folder containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# This program loads the Statcast CSV file for Camilo Doval
df = pd.read_csv("camilo_doval_5yr_statcast.csv")

# This program converts game_date to datetime and extracts the year
df['game_date'] = pd.to_datetime(df['game_date'], errors='coerce')
df['year'] = df['game_date'].dt.year

# This program groups by year and calculates average velocity and spin rate
velocity_spin = df.groupby('year')[['release_speed', 'release_spin_rate']].mean()

# This program calculates pitch type usage counts and percentages by year
pitch_counts = df.groupby(['year', 'pitch_type']).size().unstack(fill_value=0)
pitch_percent = pitch_counts.div(pitch_counts.sum(axis=1), axis=0) * 100

# This program calculates average release extension by year
extension_summary = df.groupby('year')['release_extension'].mean()

# This program calculates whiff rate by identifying swinging strikes
df['description'] = df['description'].fillna('')
df['swinging'] = df['description'].str.contains('swing', case=False)
df['whiff'] = df['description'] == 'swinging_strike'
swing_data = df[df['swinging']]
whiff_rate = swing_data.groupby('year')['whiff'].mean()

# This program plots velocity and spin rate by year
velocity_spin.plot(marker='o', title="Camilo Doval - Avg Velocity & Spin Rate by Year")
plt.xlabel("Year")
plt.ylabel("Average")
plt.grid(True)
plt.tight_layout()
plt.savefig("velocity_spin.png")
plt.show()
plt.close()

# This program plots pitch usage percentage by year
pitch_percent.plot(kind='bar', stacked=True, title="Camilo Doval - Pitch Usage % by Year")
plt.ylabel("Percentage (%)")
plt.xlabel("Year")
plt.legend(title="Pitch Type", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("pitch_usage_percent.png")
plt.show()
plt.close()

# This program plots average release extension by year
extension_summary.plot(marker='o', color='green', title="Camilo Doval - Avg Release Extension by Year")
plt.ylabel("Release Extension (ft)")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig("release_extension.png")
plt.show()
plt.close()

# This program plots whiff rate by year
whiff_rate.plot(marker='o', color='red', title="Camilo Doval - Whiff Rate by Year")
plt.ylabel("Whiff Rate")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig("whiff_rate.png")
plt.show()
plt.close()

# This program prints a confirmation message when all charts are generated and saved
print('We are done. Thank you!')
