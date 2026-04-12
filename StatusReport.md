# Updates and Challenges with Current Tasks / Changes to Project Plan
We were able to successfully download the three datasets from Chicago Data Portal. 

**Issue 1: Speed Cameras Dataset not supporting our analysis goal.**

Obstacles found while cleaning the data that led us to removing the Speed Cameras dataset:
1. Lack of data for some of the earlier crashes (there isn't data of crashes at that location prior to cameras being added), which means that we would not be able to follow the original plan to compare and contrast the amount of traffic crashes before and after the cameras went live.
2. The original traffic crashes dataset is very large, with almost 1 million observations. In order to minimize waiting times working with the data, we attempted to filter the dataset by the location of the traffic crashes across all datasets within boundaries of Downtown Chicago (dataset size too small) and with a more lenient boundary (did not significantly remove enough).
3. Speed cameras in Chicago are located in "Children’s Safety Zones," which are within 1/8th of a mile of schools and parks. This is not helpful for our use, as we wanted to compare the locations of the traffic crashes with both red light and speed cameras, which clearly do not align with areas near schools and parks, which would likely not have traffic signals / red light cameras.
Resolution: we will no longer be incorporating speed cameras into our analysis.


**Issue 2: Data file size larger than Github file size limitation.**
Our data file post-cleaning and merging was too large for Github's file limitation of 100 MB. 
Resolution: removing columns irrelevant to the analysis, since we only really need the red-light data in order to identify whether there is a camera present at a given intersection.


**Data Cleaning Process**
First step included removing the Speed Cameras dataset, as mentioned for a resolution to our first issue. We also dropped rows that had missing values for injuries or that did not include a traffic signal. In addition, we removed observations from years prior to when speed cameras were installed. Each crash observation was clustered into an intersection with a red light when applicable, and we created a separate column indicating whether an intersection was successfully identified. Finally, we dropped columns that were not relevant to our analysis in order to meet GitHub file size limitations.

New goal: comparing injury severity of different intersections with and without cameras.

**Data Merging Process**
The traffic crash and red-light camera datasets were loaded and filtered to remove records with missing latitude and longitude values to ensure valid spatial analysis. The crash data was further restricted to intersection-related traffic control devices and constrained to a defined geographic bounding box. A BallTree (for nearest-neighbor searches) with haversine distance was used to match each crash to its nearest red-light camera and compute distances in meters. A binary indicator for proximity within 50 meters of a camera was created, and a final merged dataset containing key crash and spatial features was saved for analysis.

# Updated Research/Buisness Questions
1. How does injury severity at intersections with red-light cameras compare to intersections without red-light cameras?
2. Are crashes at intersections with red-light cameras less severe than those at intersections without red-light cameras?
3. Do intersections with red-light cameras experience a lower proportion of severe or fatal injuries compared to intersections without red-light cameras?
   
# Updated Timeline

| Week | Phase | Tasks | Responsible |
|-----|------|------|------|
| Week 4 | Analysis | Main current goal is to compare injury severity crash counts of intersections with versus without cameras. More analyses to come with understanding the data better once merged. | Both working on comparative analysis |
| Week 5 | Visualization & Interpretation | Create maps showing crash locations near cameras. Produce time-series plots of crash trends. Create visuals comparing injury severity in crashes with/without cameras. | Both collaborate |
| Week 6 | Final Report & Presentation | Summarize findings and conclusions. Discuss limitations and policy implications. Prepare final visualizations and presentation. | Both collaborate |

# Team Contributions
Karena: Write-up of current and in-progress project work on Status Report.     
Jessica: Cleaning of datasets and merging based on crash and red-light camera coordinate location.    
Discussed all steps together.
