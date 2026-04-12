# Updates and Challenges with Current Tasks / Changes to Project Plan
We were able to successfully download the three datasets from Chicago Data Portal. 

**Issue: Speed Cameras Dataset not supporting our analysis goal.**

Obstacles found while cleaning the data that led us to removing the Speed Cameras dataset:
1. Lack of data for some of the earlier crashes (there isn't data of crashes at that location prior to cameras being added), which means that we would not be able to follow the original plan to compare and contrast the amount of traffic crashes before and after the cameras went live.
2. The original traffic crashes dataset is very large, with almost 1 million observations. In order to minimize waiting times working with the data, we attempted to filter the dataset by the location of the traffic crashes across all datasets within boundaries of Downtown Chicago (dataset size too small) and with a more lenient boundary (did not significantly remove enough).
3. Speed cameras in Chicago are located in "Children’s Safety Zones," which are within 1/8th of a mile of schools and parks. This is not helpful for our use, as we wanted to compare the locations of the traffic crashes with both red light and speed cameras, which clearly do not align with areas near schools and parks, which would likely not have traffic signals / red light cameras.
Resolution: we will no longer be incorporating speed cameras into our analysis.


**Data Cleaning Process**
- Removal of Speed Cameras dataset.
- Dropping rows that are null for injuries or have no traffic signal.
- Removing observations that include years from prior to when cameras were installed
- Clustering each crash observation into an intersection with a red light if applicable 
  - Creating separate column with a flag of whether or not there was an intersection identified
- Dropping columns irrelevant to our analysis to fit the Github file size limitation.

New goal: comparing injury severity of different intersections with and without cameras.

# Updated Timeline

| Week | Phase | Tasks | Responsible |
|-----|------|------|------|
| Week 4 | Analysis | Main current goal is to compare injury severity crash counts of intersections with versus without cameras. More analyses to come with understanding the data better once merged. | Both working on comparative analysis |
| Week 5 | Visualization & Interpretation | Create maps showing crash locations near cameras. Produce time-series plots of crash trends. Create visuals comparing injury severity in crashes with/without cameras. | Both collaborate |
| Week 6 | Final Report & Presentation | Summarize findings and conclusions. Discuss limitations and policy implications. Prepare final visualizations and presentation. | Both collaborate |

# Team Contributions
Karena: Write-up of current and in-progress project work on Status Report.     
Jessica:    
Discussed all steps together.
