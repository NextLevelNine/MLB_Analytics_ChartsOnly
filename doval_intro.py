# Header title and image (shown at the top of the dashboard)
project_intro = """
<div style='text-align: center;'>
    <h3 style='margin-top: 0;'>MLB Pitching Analysis Dashboard</h3>
    <img src='https://raw.githubusercontent.com/NextLevelNine/NextLevelNine-MLB_Analytics_Dashboard/main/Pink%20Baseball.jpeg' alt='Pink Baseball' width='450' style='margin: 10px 0;' />
    <p style='font-style: italic; margin-bottom: 0;'>Scouting & Player Development Insights Through a Woman’s Lens</p>
</div>
"""

# Section: Project Purpose & Overview
section_purpose_overview = """
<h4>Project Purpose</h4>
<p>As a bilingual, purpose-driven professional aspiring to transition into a Major League Baseball position, I built this dashboard to merge scouting instincts with modern analytics—through the lens of leadership, player development, and human performance. This project reflects my unique ability to translate data into meaningful, player-focused insight, shaped by over 20 years in business strategy, technology, and mental performance.</p>
<p>My goal was to design a tool that not only visualizes performance metrics, but also mirrors the decision-making needs of today’s MLB front offices. With a strong foundation in baseball analytics, scouting, and player development, this project demonstrates my ability to communicate insights clearly, build scalable systems, and align data storytelling with long-term athlete growth.</p>
<p>This dashboard is more than a coding exercise—it’s a practical demonstration of how I think, analyze, and lead through baseball intelligence. My work blends emotional intelligence, analytical rigor, and high-performance leadership, offering a versatile perspective to teams seeking resilient, player-centric environments.</p>

<h4>Project Overview</h4>
<p>I created this dashboard using Python to evaluate the past five seasons of an MLB pitcher’s performance. For this case study, I selected San Francisco Giants reliever Camilo Doval and pulled Statcast data covering 2020–2025.</p>
<p>Before scripting, I reviewed Doval’s pitch arsenal, usage trends, and public scouting reports to ensure alignment between raw data and real-world insights. I then used tools like pybaseball, pandas, and matplotlib to extract, clean, and visualize performance patterns.</p>
<p>The final result is a public-facing, interactive dashboard hosted via Streamlit Cloud—designed to help scouts, analysts, and player development staff interpret pitching trends clearly and efficiently.</p>
"""

# Section: What the Dashboard Displays
section_dashboard_insights = """
<h4>What the Dashboard Displays</h4>
<ol>
  <li><b>Velocity & Spin Rate</b><br>
  <b>What it shows:</b> Yearly averages for pitch velocity and spin rate.<br>
  <b>Why it matters:</b> Reflects Doval’s raw arm strength and ability to generate movement. His velocity peaked in 2023 (95.26 mph), and spin rate rebounded to elite levels in 2025 (2555.13 rpm), suggesting sustained pitch effectiveness.</li>

  <li><b>Pitch Usage Breakdown</b><br>
  <b>What it shows:</b> Percentage of each pitch type thrown annually.<br>
  <b>Why it matters:</b> Reveals strategic evolution. Doval increased his slider usage dramatically (58.1% in 2025) while phasing out the sinker—indicating adjustments in pitch sequencing and role clarity.</li>

  <li><b>Release Extension</b><br>
  <b>What it shows:</b> How far off the mound the ball is released.<br>
  <b>Why it matters:</b> Impacts perceived velocity and deception. Doval averaged 6.3–6.6 feet, with a slight dip in 2024 and recovery in 2025—highlighting mechanical stability and durability.</li>

  <li><b>Whiff Rate</b><br>
  <b>What it shows:</b> Swing-and-miss rate across all pitches.<br>
  <b>Why it matters:</b> A direct measure of dominance. Doval posted elite whiff rates (0.928–0.978) across all seasons, maintaining effectiveness even when velocity slightly dipped.</li>
</ol>
"""

# Section: SMART Framework
section_smart_framework = """
<h4>Project Framework Using S.M.A.R.T.</h4>
<ul>
  <li><b>Specific:</b> Analyze Doval’s pitching trends (2020–2025)</li>
  <li><b>Measurable:</b> Four core metrics across five seasons</li>
  <li><b>Achievable:</b> Built with Python, PyBaseball, Pandas, Matplotlib, and Streamlit</li>
  <li><b>Relevant:</b> Key pitching metrics drive modern player development decisions</li>
  <li><b>Time-bound:</b> Completed within one week as a capstone MVP</li>
</ul>
"""

# Section: Development Process
section_dev_process = """
<h4>Development Process</h4>
<ul>
  <li><b>pull_doval_data.py</b>: Used pybaseball to retrieve Statcast pitch-level data (2020–2025). Output: <code>camilo_doval_5yr_statcast.csv</code>.</li>
  <li><b>doval_pitching_analysis.py</b>: Calculated four core metrics:
    <ul>
      <li>Avg. velocity & spin rate by year</li>
      <li>Pitch usage breakdown</li>
      <li>Avg. release extension</li>
      <li>Whiff rate (swing-and-miss ratio)</li>
    </ul>
    Saved each to its own CSV file.
  </li>
  <li><b>doval_charts.py</b>: Created clean PNG visualizations using matplotlib.</li>
  <li><b>pull_doval_advanced.py</b>: Generated placeholder advanced metrics file: <code>doval_advanced_stats.csv</code>.</li>
  <li><b>merge_doval_data.py</b>: Merged advanced and Statcast summaries into: <code>doval_complete_profile.csv</code>.</li>
</ul>
"""

# Section: Tech Stack
section_tech_stack = """
<h4>Technical Stack</h4>
<ul>
  <li><b>Data Sources:</b> Statcast (via PyBaseball), FanGraphs (CSV)</li>
  <li><b>Languages & Libraries:</b> Python, pandas, matplotlib, pybaseball</li>
  <li><b>Dashboard & Hosting:</b> Streamlit Cloud (Free Tier)</li>
  <li><b>Deployment:</b> GitHub repository + public Streamlit app</li>
</ul>
"""

# Section: MVP Scope
section_mvp_scope = """
<h4>Version 1: MVP Scope</h4>
<ul>
  <li>Pulls, cleans, and analyzes 5-year Statcast data</li>
  <li>Visualizes velocity, pitch usage, extension, and whiff rate</li>
  <li>Fully functional dashboard with branded layout</li>
  <li>Lightweight and scalable for future enhancements</li>
</ul>
"""

# Section: Future Enhancements
section_future_enhancements = """
<h4>Version 2: Future Enhancements & Implementation</h4>
<ul>
  <li>Add advanced metrics: WAR, FIP, xFIP, K/9, WPA</li>
  <li>Enable player-to-player comparisons</li>
  <li>Introduce pitch movement charts and zone heatmaps</li>
  <li>Add PDF/CSV export options</li>
  <li>Optimize for mobile and tablet use</li>
</ul>
"""

# Section: About the Creator
section_about_creator = """
<h4>About the Creator – Liza Osterdock</h4>
<p>Hi, I’m <b>Liza Osterdock</b>—a bilingual (English/Spanish), purpose-driven professional pivoting into Major League Baseball after 20+ years in high-tech, data analysis, and business strategy. I specialize in bridging the gap between analytics and athlete development through thoughtful leadership, mental skills coaching, and strategic programming.</p>
<p>With a “Play Big” mindset, I help players and organizations unlock high-performance environments rooted in emotional intelligence, preparation, and resilience. I’m passionate about blending data and human insight to support long-term growth for both individuals and teams.</p>
"""

# Section: Certifications & Contact
section_certifications_contact = """
<h4>🎓 Baseball & Analytics Certifications</h4>
<ul>
  <li><b>Baseball GM & Scouting</b> – SMWW, Dec. 2024</li>
  <li><b>Baseball Player Development</b> – SMWW, Mar. 2025</li>
  <li><b>Baseball Analytics</b> – SMWW, Mar. 2025</li>
  <li><b>Analytics & Critical Thinking in Baseball (Level I)</b> – SABR, Apr. 2025</li>
</ul>
<p><b>Currently enrolled (expected completion by July 2025):</b></p>
<ul>
  <li>Advanced Analytics in Baseball (Level II) – SABR</li>
  <li>Python Programming – Stanford Continuing Education</li>
  <li>Baseball Agent Certification – SMWW</li>
</ul>

<h4>📬 Let’s Connect</h4>
<ul>
  <li><b>LinkedIn:</b> <a href="https://www.linkedin.com/in/lizaosterdock/" target="_blank">linkedin.com/in/lizaosterdock</a></li>
  <li><b>Email:</b> liza@allysixconsulting.com</li>
  <li><b>Website:</b> <a href="https://nextlevelnine.com" target="_blank">nextlevelnine.com</a> <i>(Coming Soon)</i></li>
</ul>
"""

# Footer section
footer_content = """
<hr>
<p style='text-align: center; font-size: 14px;'>
    © 2025 Next Level Nine. All rights reserved.<br>
    Designed & built by <b>Liza Osterdock</b>
</p>
"""
