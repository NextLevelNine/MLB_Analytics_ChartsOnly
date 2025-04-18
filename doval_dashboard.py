import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64

# Import only the remaining HTML content section
from doval_intro import section_dashboard_insights

# Load and encode logo
def load_logo(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

base64_logo = load_logo("Next Level Nine Logo.png")

# Set page config
st.set_page_config(page_title='📊 MLB Pitching Dashboard', page_icon='⚾', layout='wide')

# Intro Summary for the Dashboard
#st.markdown(section_dashboard_insights, unsafe_allow_html=True)
#st.markdown('---')

# Load dataset
file_path = 'camilo_doval_5yr_statcast.csv'
df = pd.read_csv(file_path)
df['game_date'] = pd.to_datetime(df['game_date'], errors='coerce')
df['year'] = df['game_date'].dt.year

# -----------------------------
# SECTION: Velocity & Spin Rate
# -----------------------------
st.header('Velocity & Spin Rate by Year')
st.markdown('* **Release Speed (MPH)**: The speed at which the ball leaves the pitcher’s hand.')
st.markdown('* **Spin Rate (RPM)**: How many times the ball spins per minute. Higher values often lead to more movement.')

velocity_spin = df.groupby('year')[['release_speed', 'release_spin_rate']].mean().round(2)
st.dataframe(velocity_spin)

fig1, ax1 = plt.subplots(figsize=(5, 3))
velocity_spin.plot(marker='o', ax=ax1)
ax1.set_title('Velocity & Spin Rate by Year')
ax1.set_xlabel('Year')
ax1.set_ylabel('Average')
ax1.grid(True)
ax1.set_xticks(velocity_spin.index)
ax1.set_xticklabels(velocity_spin.index.astype(int))
st.pyplot(fig1)

# -----------------------------
# SECTION: Pitch Usage Percentages
# -----------------------------
st.header('Pitch Usage Percentages by Year')
st.markdown('* Shows the percentage mix of pitches used each year.')
st.markdown('Pitch Types: SL (Slider), FC (Cutter), FF (4-Seamer), SI (Sinker)')

pitch_counts = df.groupby(['year', 'pitch_type']).size().unstack(fill_value=0)
pitch_percent = pitch_counts.div(pitch_counts.sum(axis=1), axis=0).round(3) * 100
st.dataframe(pitch_percent)

fig2, ax2 = plt.subplots(figsize=(5, 3))
pitch_percent.plot(kind='bar', stacked=True, ax=ax2)
ax2.set_title('Pitch Usage Percentages by Year')
ax2.set_ylabel('Percentage (%)')
ax2.set_xlabel('Year')
ax2.set_xticks(range(len(pitch_percent.index)))
ax2.set_xticklabels(pitch_percent.index.astype(str), rotation=0)
ax2.legend(title='Pitch Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
st.pyplot(fig2)

# -----------------------------
# SECTION: Release Extension
# -----------------------------
st.header('Average Release Extension by Year')
st.markdown('* Measures how far off the mound the ball is released. Greater extension can reduce perceived reaction time for hitters.')

extension_summary = df.groupby('year')['release_extension'].mean().round(2)
st.dataframe(extension_summary)

fig3, ax3 = plt.subplots(figsize=(5, 3))
extension_summary.plot(marker='o', color='green', ax=ax3)
ax3.set_title('Release Extension by Year')
ax3.set_ylabel('Feet')
ax3.set_xlabel('Year')
ax3.grid(True)
ax3.set_xticks(extension_summary.index)
ax3.set_xticklabels(extension_summary.index.astype(int))
st.pyplot(fig3)

# -----------------------------
# SECTION: Whiff Rate
# -----------------------------
st.header('Whiff Rate by Year')
st.markdown('* A **whiff** is a swing-and-miss.')
st.markdown('* **Whiff Rate = Swinging Strikes ÷ Total Swings**')

df['description'] = df['description'].fillna('')
df['swinging'] = df['description'].str.contains('swing', case=False)
df['whiff'] = df['description'] == 'swinging_strike'

swing_data = df[df['swinging']]
whiff_rate = swing_data.groupby('year')['whiff'].mean().round(3)
st.dataframe(whiff_rate)

fig4, ax4 = plt.subplots(figsize=(5, 3))
whiff_rate.plot(marker='o', color='red', ax=ax4)
ax4.set_title('Whiff Rate by Year')
ax4.set_ylabel('Whiff Rate')
ax4.set_xlabel('Year')
ax4.grid(True)
ax4.set_xticks(whiff_rate.index)
ax4.set_xticklabels(whiff_rate.index.astype(int))
st.pyplot(fig4)

# -----------------------------
# SECTION: Strikeout Rate (K%)
# -----------------------------
st.header('Strikeout Rate (K%) by Year')
st.markdown('* Measures the percentage of plate appearances that result in a strikeout.')

df['k'] = df['events'] == 'strikeout'
k_rate = df.groupby('year')['k'].mean().round(3)
st.dataframe(k_rate)

fig5, ax5 = plt.subplots(figsize=(5, 3))
k_rate.plot(marker='o', color='purple', ax=ax5)
ax5.set_title('Strikeout Rate (K%) by Year')
ax5.set_ylabel('Strikeout Rate')
ax5.set_xlabel('Year')
ax5.grid(True)
ax5.set_xticks(k_rate.index)
ax5.set_xticklabels(k_rate.index.astype(int))
st.pyplot(fig5)

# -----------------------------
# SECTION: Zone Percentage (Zone%)
# -----------------------------
st.header('Zone Percentage (Zone%) by Year')
st.markdown('* Percentage of pitches thrown in the strike zone.')

zone_pct = df.groupby('year')['zone'].mean().round(3)
st.dataframe(zone_pct)

fig6, ax6 = plt.subplots(figsize=(5, 3))
zone_pct.plot(marker='o', color='teal', ax=ax6)
ax6.set_title('Zone Percentage by Year')
ax6.set_ylabel('Zone %')
ax6.set_xlabel('Year')
ax6.grid(True)
ax6.set_xticks(zone_pct.index)
ax6.set_xticklabels(zone_pct.index.astype(int))
st.pyplot(fig6)


# -----------------------------
# SECTION: Footer
# -----------------------------
st.markdown('---')
st.markdown('<center>Designed by Liza Osterdock.</center>', unsafe_allow_html=True)
st.markdown('<center>© 2025 Next Level Nine. All rights reserved.</center>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)

if base64_logo:
    image_html = f"<div style='text-align: center; margin-top: 10px;'><img src='data:image/png;base64,{base64_logo}' width='200'/></div>"
    st.markdown(image_html, unsafe_allow_html=True)
