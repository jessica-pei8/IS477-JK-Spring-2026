# Project Plan

## Overview
Traffic safety in a big city can be difficult with the large amount of people and vehicles that have to share space on the road. The goal of this project is to evaluate and compare the effectiveness of automated speed cameras and red-light cameras in contributing to traffic safety in Chicago. Both are designed to reduce risky driving behavior, as speed cameras aim to reduce speeding, while red-light cameras target drivers who run red lights. By analyzing crash data before and after camera installation, this project will determine whether these technologies are associated with significant reductions in traffic crashes and whether one seems to be more effective than the other.

The analysis will use three datasets from the Chicago Data Portal: Speed Camera Locations, Red Light Camera Locations, and Traffic Crashes - Crashes. The camera datasets include location coordinates and when the camera was first installed, which we can utilize to compare crashes before and after installation.

We plan to clean and merge the datasets, mapping crash locations relative to camera sites, and measuring crash frequency within a certain distance of each camera, which will be used to compare the before and after of camera usage. To identify trends and whether one equipment show a larger impact on reducing crashes, we will use comparisons and visualizations such as maps, time-series plots, and bar charts.

## Team
Karena: data focus is on the dataset with red light.     
Jessica: data focus is on the dataset with speed cameras.    
We will each do the data cleaning, preprocessing, integration, and analysis for the respective datasets.    
We will work on combining analyses from our respective data focuses, and then further modeling with the crash details together in terms of schema integration, data processing, and workflows.      
More details added in the timeline.   

## Research/Business Questions
1. Do speed cameras and red-light individually reduce traffic crashes after installation?
2. Does one of speed cameras and red-light reduce traffic crashes more than the other after installation (in general and relative to original respective performance)?
3. How does crash severity change after camera installation?

## Datasets
Red Light Camera Locations and Speed Camera Locations: includes directions of the vehicles, location coordinates, and when the equipment went live.   
Traffic Crashes - Crash: includes details about the where, what, and how of crashes.

[Speed Camera Locations](https://data.cityofchicago.org/Transportation/Speed-Camera-Locations/4i42-qv3h/about_data ) (Chicago Data Portal)    
[Red Light Camera Locations](https://data.cityofchicago.org/Transportation/Red-Light-Camera-Locations/thvf-6diy/about_data) (Chicago Data Portal)        
[Traffic Crashes - Crashes](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/about_data) (Chicago Data Portal)   

The datasets will be integrated using geographic coordinates (latitude&longitude), allowing crashes to be associated with nearby spped and red camera locations.

## Timeline

| Week | Phase | Tasks | Responsible |
|-----|------|------|------|
| Week 1 | Data Collection & Exploration | Download datasets from Chicago Data Portal. Explore dataset structures, column names, and formats. Identify key variables such as camera installation dates, crash dates, longitude, latitude, and severity. | Karena: Red Light Camera dataset<br>Jessica: Speed Camera dataset<br>Both: Traffic Crashes dataset |
| Week 2 | Data Cleaning & Preparation | Remove incomplete or duplicate records. Standardize latitude/longitude formats. Convert date columns into usable formats. Filter crashes within a chosen radius of camera locations. | Karena: Clean Red Light Camera dataset<br>Jessica: Clean Speed Camera dataset<br>Both: Crash dataset preparation and spatial filtering |
| Week 3 | Data Integration | Merge crash data with camera location datasets. Identify crashes occurring before and after camera installation. Create time window variables (ex one year before vs. after). | Both collaborate on merging and validation |
| Week 4 | Analysis | Calculate crash counts before and after installation. Compare crash frequency near speed cameras and red-light cameras. | Karena: Red-light camera analysis<br>Jessica: Speed camera analysis<br>Both: Comparative analysis |
| Week 5 | Visualization & Interpretation | Create maps showing crash locations near cameras. Produce time-series plots of crash trends. Create bar charts comparing before vs. after crash counts. | Both collaborate |
| Week 6 | Final Report & Presentation | Summarize findings and conclusions. Discuss limitations and policy implications. Prepare final visualizations and presentation. | Both collaborate |


## Constraints

**Spatial Accuracy**  
Although the camera datasets provide geographic coordinates (longitude&latitude), crash locations may not always correspond to the exact location of the camera or the intersection it monitors. Due to this we must define a distance threshold to determine whether a crash occurred “near” a speed or red light camera. The choice of this distance threshold may affect the results. A smaller radius might miss relevant crashes while a larger radius may include crashes unrelated to the camera location.

**Causality Limitations**  
Even if the analysis shows a decrease in crashes after a camera is installed, this does not necessarily mean that the camera directly caused the reduction. Other factors could influence crash rates during the same time period, such as road redesigns, new traffic signals, increased police enforcement, etc. 

**Temporal Differences**  
Camera installations do not occur at the same time across all locations. Some cameras may have been installed many years earlier than others. This means the available time periods for analyzing “before” and “after” crashes will vary, leading to inconsistencies in the amount of data used for each camera location. 


## Gaps

**Distance Threshold Selection**  
We may need to experiment with several distance values and evaluate which threshold produces the most reasonable representation of the camera’s influence area since different thresholds could significantly change the number of crashes included in the analysis. 

**Time Window Definition**  
A shorter time window may better isolate the impact of the camera but could produce less data for analysis, while a longer window may provide more data but introduce additional confounding factors such as population growth or changes in traffic patterns. Need to find a right balence between isolating the camera’s direct impact by limiting the influence of long-term changes in traffic conditions and having enough observations to detect statistical patterns harder to detect.

**External Factors**  
Although the datasets include camera locations and crash records, they do not capture all contextual factors that may influence crash rates. For example, weather conditions or traffic changes may affect crash frequency and severity. These variables could act as confounders and they may influence crash rates independently of camera installation. To account for external factors that may influence crash rates, we will examine overall crash trends across multiple years to determine whether changes occurred specifically after camera installation or were part of broader trends affecting the entire area. We will also compare intersections with cameras to similar intersections without cameras to provide a control group. 
