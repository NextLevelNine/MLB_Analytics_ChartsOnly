import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import base64

# Import header and HTML content sections
from doval_intro import (
    project_intro,
    section_purpose_overview,
    section_dashboard_insights,
    section_smart_framework,
    section_dev_process,
    section_tech_stack,
    section_mvp_scope,
    section_future_enhancements,
    section_about_creator,
    section_certifications_contact,
)

# Load and encode correct logo
def load_logo(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

base64_logo = load_logo("Next Level Nine Logo.png")

# Set Streamlit page configuration
st.set_page_config(page_title='📊 MLB Pitching Dashboard', page_icon='⚾', layout='wide')

# Display visual header (title + pink baseball image + subheader)
st.markdown(project_intro, unsafe_allow_html=True)
st.markdown('---')

# SECTION: Project Purpose + Overview
st.markdown(section_purpose_overview, unsafe_allow_html=True)
st.markdown('---')

# Load Statcast dataset
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
plt.title('Velocity & Spin Rate by Year')
plt.xlabel('Year')
plt.ylabel('Average')
plt.grid(True)
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
plt.title('Pitch Usage Percentages by Year')
plt.ylabel('Percentage (%)')
plt.xlabel('Year')
plt.legend(title='Pitch Type', bbox_to_anchor=(1.05, 1), loc='upper left')
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
plt.title('Release Extension by Year')
plt.ylabel('Feet')
plt.xlabel('Year')
plt.grid(True)
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
plt.title('Whiff Rate by Year')
plt.ylabel('Whiff Rate')
plt.xlabel('Year')
plt.grid(True)
st.pyplot(fig4)

# Divider
st.markdown('---')

# Remaining HTML sections
st.markdown(section_dashboard_insights, unsafe_allow_html=True)
st.markdown(section_smart_framework, unsafe_allow_html=True)
st.markdown(section_dev_process, unsafe_allow_html=True)
st.markdown(section_tech_stack, unsafe_allow_html=True)
st.markdown(section_mvp_scope, unsafe_allow_html=True)
st.markdown(section_future_enhancements, unsafe_allow_html=True)
st.markdown(section_about_creator, unsafe_allow_html=True)
st.markdown(section_certifications_contact, unsafe_allow_html=True)

# Footer
st.markdown('---')
st.markdown('<center>Designed by Liza Osterdock.</center>', unsafe_allow_html=True)
st.markdown('<center>© 2025 Next Level Nine. All rights reserved.</center>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)

if base64_logo:
    image_html = f"<div style='text-align: center; margin-top: 10px;'><img src='data:image/png;base64,{base64_logo}' width='200'/></div>"
    st.markdown(image_html, unsafe_allow_html=True)
