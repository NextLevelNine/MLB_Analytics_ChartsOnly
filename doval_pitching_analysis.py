
import pandas as pd

# This program loads the saved Statcast CSV for Camilo Doval
df = pd.read_csv("camilo_doval_5yr_statcast.csv")

# This program converts game_date to datetime and extracts the year
df['game_date'] = pd.to_datetime(df['game_date'], errors='coerce')
df['year'] = df['game_date'].dt.year

# This program creates columns to analyze swinging and whiffing pitches
df['description'] = df['description'].fillna('')
df['swinging'] = df['description'].str.contains('swing', case=False)
df['whiff'] = df['description'] == 'swinging_strike'

# =========================
# VELOCITY & SPIN
# =========================
# This program calculates yearly averages for velocity and spin rate
print("\n--- Yearly Averages: Velocity & Spin Rate ---")
velocity_spin = df.groupby('year')[['release_speed', 'release_spin_rate']].mean().round(2)
print(velocity_spin)

# =========================
# PITCH USAGE 
# =========================
# This program calculates pitch usage counts and percentages by year
print("\n--- Pitch Usage by Year ---")
pitch_counts = df.groupby(['year', 'pitch_type']).size().unstack(fill_value=0)
pitch_percent = pitch_counts.div(pitch_counts.sum(axis=1), axis=0).round(3) * 100
print("Pitch Counts:")
print(pitch_counts)
print("\nPitch Percentages (%):")
print(pitch_percent)

# =========================
# RELEASE EXTENSION 
# =========================
# This program calculates average release extension by year
print("\n--- Average Release Extension by Year ---")
extension_summary = df.groupby('year')['release_extension'].mean().round(2)
print(extension_summary)

# =========================
# WHIFF RATE 
# =========================
# This program calculates whiff rate (swinging strikes ÷ total swings) per year
print("\n--- Whiff Rate by Year ---")
swing_data = df[df['swinging']].copy()
whiff_rate_by_year = {}

for year in swing_data['year'].unique():
    year_data = swing_data[swing_data['year'] == year]
    total_swings = len(year_data)
    total_whiffs = year_data['whiff'].sum()
    whiff_rate = round(total_whiffs / total_swings, 3)
    whiff_rate_by_year[year] = whiff_rate

whiff_rate_df = pd.DataFrame.from_dict(whiff_rate_by_year, orient='index', columns=['whiff_rate'])
print(whiff_rate_df)

# This program saves all summary outputs to CSV files
velocity_spin.to_csv("doval_velocity_spin_by_year.csv")
pitch_percent.to_csv("doval_pitch_usage_percent_by_year.csv")
extension_summary.to_csv("doval_release_extension_by_year.csv")
whiff_rate_df.to_csv("doval_whiff_rate_by_year.csv")

print("\nAnalysis complete. Summary files saved.")
