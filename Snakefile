rule all:
    input:
        "visualizations/injury_severity_analysis.png",
        "visualizations/crash_heatmap.html"

rule hashing:
    input:
        traffic = "data/Traffic_Crashes.csv",
        redlight = "data/Red_Light.csv"
    output:
        provenance = "data/processed/cleaning_provenance.json"
    script:
        "scripts/hashing.py"

rule clean_and_match:
    input:
        traffic = "data/Traffic_Crashes.csv",
        redlight = "data/Red_Light.csv"
        provenance = "data/processed/cleaning_provenance.json" 
    output:
        traffic_cleaned = "data/cleaned_Traffic_Crashes.csv",
        redlight_cleaned = "data/cleaned_Red_Light.csv",
        crashes_camera = "data/crashes_camera.csv"
    script:
        "scripts/cleaning.py"

rule analyze_and_visualize:
    input:
        crashes_camera = "data/crashes_camera.csv",
        redlight_cleaned = "data/cleaned_Red_Light.csv"
    output:
        severity_plot = "visualizations/injury_severity_analysis.png",
        heatmap = "visualizations/crash_heatmap.html"
    script:
        "scripts/analysis_visualization.py"
