import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

traffic_matched_df = pd.read_csv('data/crashes_camera.csv')
red_light_df = pd.read_csv('data/cleaned_Red_Light.csv')

cam    = traffic_matched_df[traffic_matched_df['has_red_light'] == 1]
no_cam = traffic_matched_df[traffic_matched_df['has_red_light'] == 0]

injury_cols = {
    'Fatal'               : 'INJURIES_FATAL',
    'Incapacitating'      : 'INJURIES_INCAPACITATING',
    'Non-Incapacitating'  : 'INJURIES_NON_INCAPACITATING',
    'Reported/Not Evident': 'INJURIES_REPORTED_NOT_EVIDENT',
}

# Calculate proportions and counts for each injury type
rows = []
for label, col in injury_cols.items():
    rows.append({
        'Injury Type' : label,
        'Camera %'    : (cam[col] > 0).mean() * 100,
        'No Camera %' : (no_cam[col] > 0).mean() * 100,
        'Camera Count'    : (cam[col] > 0).sum(),
        'No Camera Count' : (no_cam[col] > 0).sum(),
    })
prop_df = pd.DataFrame(rows)
print(prop_df.to_string(index=False))

# % of crashes with any severe/fatal injury
traffic_matched_df['any_severe'] = ((traffic_matched_df['INJURIES_FATAL'] > 0) | (traffic_matched_df['INJURIES_INCAPACITATING'] > 0)).astype(int)
cam    = traffic_matched_df[traffic_matched_df['has_red_light'] == 1]
no_cam = traffic_matched_df[traffic_matched_df['has_red_light'] == 0]
cam_severe_pct   = cam['any_severe'].mean() * 100
nocam_severe_pct = no_cam['any_severe'].mean() * 100

# Setup for visualizations 
BLUE, RED = '#2563EB', '#DC2626'
fig, axes = plt.subplots(1, 2, figsize=(16, 5))
fig.suptitle('Injury Severity: Camera vs. Non-Camera Intersections',
             fontsize=14, fontweight='bold')

# Plot 1 — % of crashes with each injury type
ax = axes[0]
x, w = np.arange(len(prop_df)), 0.35
ax.bar(x - w/2, prop_df['Camera %'],    w, label='Camera',    color=BLUE, alpha=0.85)
ax.bar(x + w/2, prop_df['No Camera %'], w, label='No Camera', color=RED,  alpha=0.85)
ax.set_xticks(x)
ax.set_xticklabels(['Fatal', 'Incapacit.', 'Non-Incap.', 'Reported'], fontsize=9)
ax.set_ylabel('% of crashes')
ax.set_title('% of Crashes with Each Injury Type')
ax.legend()
ax.grid(axis='y', alpha=0.3)

# Plot 2 — Severe/fatal crash rate
ax = axes[1]
rates = [cam_severe_pct, nocam_severe_pct]
bars  = ax.bar(['Camera', 'No Camera'], rates, color=[BLUE, RED], alpha=0.85, width=0.5)
for bar, val in zip(bars, rates):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
            f'{val:.2f}%', ha='center', va='bottom', fontweight='bold', fontsize=11)
ax.set_ylabel('% of crashes')
ax.set_title('Severe or Fatal Crash Rate')
ax.set_ylim(0, max(rates) * 1.3)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('visualizations/injury_severity_analysis.png', dpi=150, bbox_inches='tight')

# Heatmap of crash locations with red light cameras overlaid
m = folium.Map(location=[41.85, -87.68], zoom_start=11)
heat_data = []

# Add crash locations to heatmap, weighted by severity
for _, row in traffic_matched_df.iterrows():
    lat = row['LATITUDE']
    lon = row['LONGITUDE']
    weight = 0
        
    if row['INJURIES_FATAL'] > 0:
        weight = 3    
    elif row['INJURIES_INCAPACITATING'] > 0:
        weight = 2
    elif row['INJURIES_NON_INCAPACITATING'] > 0:
        weight = 1
        
    if weight > 0:
        heat_data.append([lat, lon, weight])

HeatMap(heat_data, radius=15, blur=15, max_zoom=15).add_to(m)

# Add red light camera locations
for _, row in red_light_df.iterrows():
    folium.CircleMarker(location=[row['LATITUDE'], row['LONGITUDE']], radius=6, color='purple', fill=True, fill_opacity=0.7, popup="Red Light Camera").add_to(m)

m.save("visualizations/crash_heatmap.html")
