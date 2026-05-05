# IS477-JK-Spring-2026: Impact of Red Light Cameras on Crash Injury
## Contributors
- Jessica Pei
- Karena Liang

## Summary
Traffic safety in a big city can be difficult with the large amount of people and vehicles that have to share space on the road. In larger cities like Chicago, this is something that is even more important to keep in mind and to enforce regulations that can ensure the safety of those who live in the area. In order to manage this, red light cameras were introduced to reduce risky driving behavior by targeting those who run red lights. The goal of this project is to evaluate the effectiveness of automated red light cameras in contributing to traffic safety in Chicago. By analyzing crash data in sections with and without red light camera installations, we will determine whether they are associated with significant reductions in traffic crashes by looking at the severity of the injuries caused by the crashes among intersections with and without red light cameras, instead of just analyzing crash frequency. Since many studies assess whether cameras reduce the number of crashes, we wanted to understand whether they reduce the severity of crashes to get more information from a public health and policy perspective. If red light cameras are helpful and effective, we would expect intersections equipped with cameras to have less severe injury outcomes in comparison to the intersections without the cameras.
    
The analysis will use two datasets from the Chicago Data Portal: Red Light Camera Locations, and Traffic Crashes - Crashes. The camera dataset provides geographic coordinates and operational details for red-light cameras across the city, while the crash dataset contains detailed information on individual crashes, including injury severity metrics such as total injuries, fatal injuries, and levels of incapacitation. In using these datasets together, we can compare crashes and the injury severity across locations with and without red light cameras.
    
After cleaning and filtering the data to include only signalized intersections within a defined geographic area, we used a spatial nearest-neighbor approach to match crashes to nearby camera locations and classify whether each crash occurred at a camera-equipped intersection. Our analysis compares injury severity outcomes including fatal, incapacitating, and non-incapacitating injuries between intersections with and without red-light cameras. The final results show that while intersections with cameras have slightly lower proportions of some non-fatal injury categories, the overall differences in injury severity between the two groups are not very large. Something particularly interesting was that the proportion of fatal crashes was actually marginally higher at camera-equipped intersections. However, this difference is also small and most likely influenced by other latent factors such as traffic volume and intersection characteristics.  

Overall, our final results show that red-light cameras may play a role in driver behavior. However, their impact on reducing crash injury severity seems to be limited. These results highlight the importance of considering broader contextual factors such as road design, traffic density, and camera placement when evaluating the effectiveness of traffic safety interventions. There could be a variety of other factors like the fact that many intersections may have red light cameras but drivers who may be a bit more reckless may not notice there is one present, poor intersection design such as the number of lanes and visibility conditions, and even the fact that intersections with cameras are often placed in already high-traffic or historically high-crash areas; all of which can all influence crash outcomes.

## Data profile: [max 2000 words] 
For each dataset used, describe its structure, content, and characteristics. Specify the location of the dataset files in your project repository. Discuss any ethical or legal constraints associated with the data and explain how the datasets relate to your questions

## Data quality: 
|  | Traffic Crashes | Red Light Cameras|
| -------- | -------- | -------- |
| Accuracy | Since approximately half of these reports are self-reported at police stations rather than at the scene, some of the crash parameters like weather/street conditions or posted speed limits rely on the memory of the reporting individual or the officer's best available info. The metadata notes that many of these may disagree with posted information or other assessments on road conditions. | The data is coming from a variety of city-managed hardware. Each entry includes precise geographical coordinates and the specific "approaches" (directions of travel) monitored. |
| Completeness | The data may not be fully complete in the sense that not every single crash in Chicago is included in the data, as a traffic crash within the city limits for which CPD is not the responding police agency, typically crashes on interstate highways, freeway ramps, and on local roads along the City boundary, are excluded from this dataset, among other requirements for crashes that can be reported as per Illinois statute. | After an initial analysis of the data, there is no reason to believe the data is not complete, with 300 active intersections listed. |
| Timeliness | Last updated May 5, 2026, updates daily | Last updated April 24, 2026, although metadata says it's updated daily, so there may be some delay though it may be due to no new information |
| Consistency | According to the metadata, the data follows the format specified in the Traffic Crash Report, SR1050, of the Illinois Department of Transportation. This makes it easier to combine with other traffic or crash related datasets from the Chicago Data Portal since it will have the same formatting and uses a unique crash record ID for each observation that can be used to merge with other datasets. | Follows the same format as the traffic crash data, can clearly see the intersection and location fields as well as the semantic styling are formatted to match. 

## Data cleaning: [max 1000 words] 
Summarize the data cleaning operations you performed and explain how each operation addressed specific data quality issues in your datasets.

## Findings: [~500 words] 
Description of any findings including numeric results and/or visualizations.

## Future work: [~500-1000 words] 
One lesson we definitely learned was that it’s important to highlight and/or consider the latent factors in a relationship between two variables and the extent to which we can associate the results of an analysis with the questions and/or relationship(s) we are focused on in the analysis. In our case, we realized that something to keep in mind with the red-light cameras and its relation to crash/injury severity is that some or maybe many of the cameras may have been placed there because of prior issues or influx of crashes in that intersection or location already as well as how exact the boundaries of the intersection should or could be with being able to detect whether crashes are happening (such as a crash happening 100 feet away from the camera could be due to a person seeing the camera and slamming on the brakes, but it could also be something completely unrelated like the driver seeing an animal on the road. 
  
There were also a lot of technical aspects of the data that we had trouble with in the beginning in terms of being able to align the dates of when cameras were installed with when the crash data recording started, which highlights the importance of the consistency aspect of data quality, in being able to combine data to analyze together not just merging the data together, but also being able to align the data in a way where the attributes and the observations still make sense in the context of the data and the domain. To build upon the findings we already have, we could focus more on environmental variables or some of those other external factors mentioned prior in this report that could be accounted for. 
  
We could potentially include a dataset that adds traffic volume at the certain date and time the crash happened, along with street visibility from time of day with the street lighting and pedestrian infrastructure. With the traffic data, it would be helpful to see if the crashes are happening due to the presence of cameras or due to high traffic at that given timestamp, or even due to holiday or special events like concerts or festivals that could drive in a lot more potential for crashes than normal.
  
We could also take a step back and try to include the speed cameras dataset as originally intended after finding the optimal point of time to have complete data at least within a certain time frame. That way, we could inspect and analyze the differences in crashes and severity of intersections before and after the two different types of cameras were installed. If possible, it may also be interesting to include some data from whether or not the cameras were identified on apps like Google maps, Apple Maps, or Waze, where drivers are notified in advance from other drivers that a speed camera, red light camera, or speed traps are located. With modeling, we could also build a machine learning model to predict future hotspots where cameras could help alleviate crashes by identifying potential high risk areas for crashes or even just other factors that could lead to crashes like high traffic spots, poor street design and/or infrastructure. 

## Challenges: [~500 words] 
Discuss the main challenges you encountered while working on the project.

## Reproducing: 
Sequence of steps required for someone else to reproduce your results.

## References: 
Formatted citations for any papers, datasets, or software used in your project.
### Data Licenses
**Traffic Crashes - Crashes**
- Source: Chicago Data Portal
- License: Public Domain
- Terms: Freely available for use and redistribution
- Required citation: United Nations, Department of Economic and Social Affairs, Population Division (2024)

**Red Light Camera Locations**
- Source: Chicago Data Portal
- License: Subject to City of Chicago Data Terms of Use
- Terms: Data is provided on an "as-is" basis; users must indemnify the City and include a mandatory disclaimer on any derivative applications.
- Required citation: City of Chicago, Chicago Police Department (2026). Red Light Camera Locations. Chicago Data Portal.

### Third-Party Software
- **pandas**: BSD 3-Clause License
- **numpy**: BSD License
- **matplotlib**: PSF License
- **seaborn**: BSD 3-Clause License
- **jupyter**: BSD License
- **folium**: MIT License (MIT)
