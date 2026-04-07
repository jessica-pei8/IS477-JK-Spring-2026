update on each of the tasks described on your project plan 
including references and links to specific artifacts in your repository (such as datasets, scripts, workflows, workflow diagrams, etc).
# Updates on Current Tasks
We were able to successfully download the three datasets from Chicago Data Portal. 

Obstacles found while cleaning the data that led us to removing the Speed Cameras dataset:
1. Lack of data for some of the earlier crashes (there isn't data of crashes at that location prior to cameras being added).
- would not be able to follow the original plan to compare and contrast the amount of traffic crashes before and after the cameras went live 
2. The original traffic crashes dataset is very large, with almost 1 million observations. In order to minimize waiting times working with the data, we attempted to
  filter the dataset by the location of the traffic crashes across all datasets within boundaries of Downtown Chicago (dataset size too small) and with a more
  lenient boundary (did not significantly remove enough).
3. Speed cameras in Chicago are located in "Children’s Safety Zones," which are within 1/8th of a mile of schools and parks. This
  is not helpful for our use, as we wanted to compare the locations of the traffic crashes with both
  red light and speed cameras, which clearly do not align with areas near schools and parks, which would likely not have traffic signals / red light cameras.
  






drop rows that are null for injuries
  no traffic signal

# Updated Timeline

| Week | Phase | Tasks | Responsible |
|-----|------|------|------|
| Week 4 | Analysis | Calculate crash counts before and after installation. Compare crash frequency near speed cameras and red-light cameras. | Karena: Red-light camera analysis<br>Jessica: Speed camera analysis<br>Both: Comparative analysis |
| Week 5 | Visualization & Interpretation | Create maps showing crash locations near cameras. Produce time-series plots of crash trends. Create bar charts comparing before vs. after crash counts. | Both collaborate |
| Week 6 | Final Report & Presentation | Summarize findings and conclusions. Discuss limitations and policy implications. Prepare final visualizations and presentation. | Both collaborate |



An updated timeline indicating the status of each task and when they will be completed.

A description of any changes to your project plan itself, in particular about your progress so far. Also include changes you made to your plan based on feedback you may have received for Milestone 2.

Summarize any challenges or problems you have encountered so far. For each issue, explain how you resolved it or describe your plan to address it in the near future.

Each team member has to write a short summary of their contributions to the current milestone. 
Each team member should add and commit their contribution summary themselves to the shared github repo.
