# ELON GOLF Data Analysis Interactive App
### **MGT 4250 COURSE PROJECT**
### *Juan Callejo Ropero*  (jcallejoropero@elon.edu)

[streamlit-Trackman-2024-05-03-00-05-58.webm](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/70b3bd9f-09f5-4655-b039-9af56052daed)


## Project Description
With the recent popularity increase of golf, new technologies have arrived to college golf. [Trackman technology](https://www.trackman.com/golf/launch-monitors/trackman-4) is a dual radar system that captures the trajectory and flight of the ball, as well as the swing path of the golfer. The parameters include ball speed, attack angle, club path, face angle, and spin rate among others. This technology gives instant feedback on each shot, helping players and coaches make data-driven decisions improving training and strategy.
- **Using this technology, how can [Elon Golf](https://elonphoenix.com/sports/mens-golf) improve its performance?**
  
[Worsley Golf Training Center](https://elonphoenix.com/facilities/w-cecil-worsley-iii-golf-training-center/20), (Elon Golf Facility) has two Trackman radars, where players from both Men’s and Women’s players hit and record their shots in their daily practices. There are more than 70,000 shots recorded between 2022 and 2024 in one single trackman radar. Taking in consideration the investment made to have this technology, a correct use of it should not only give immediate detailed feedback but also provide a more data-driven approach to the team practice schedule and routine.

For this project, data from each team player will be collected. After the collection of more than 300 shots, the data will be cleaned and organized to work with the relevant parameters. Finally, an [Interactive App](https://elongolftrackmandata.streamlit.app/) will show multiple visualizations that can help the players and coaches identify hitting patterns as well as emphasize areas for improvement.

![Trackman_Logo](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/bfc29e68-6726-4cac-b46c-e97b68aa4fee)


**Elon Golf Data:** [Interactive App](https://elongolftrackmandata.streamlit.app/)


### Questions of interest
I. What's the relationship between Club Speed and Carry Distance among the team?

II. How does Impact Height Position Affect Ball Speed with a Driver?

III. How accurate are Elon players regarding distance dispersion? What is the area each player has to improve?

IV. Driver Shot Carry Distance Predictor

## Data Description

For this project, every player recorded three different shots ten times:
- 100 yds 
- 175 yds 
- Driver

For accessing this data, a Trackman Radar recorded the multiple shots from the team members. Once recorded, the raw data was imported and then selected from the connected computer at Elon Golf facility. The initial file was the Trackman file which was converted to a excel file and then to csv file. Preprocessing and cleaning the dataset consisted in removing missing metrics of some shots and deleting outliers that where caused by wrecked golf balls or miscalculations.

### Column Descriptions:

| Data Type | Description |
| ----------- | ----------- |
| Date | Date the shot was recorded |
| Player |  Name of the Player |
| Club |  Golf Club used |
| Ball | Type of ball used |
| Club Speed | The speed of the center of the clubface at first contact with the ball |
| Attack Angle | Vertical (up/down) angle at which the club head is moving at impact |
| Club Path | The direction the club is moving (left or right) at the point of impact |
| Low Point |  The lowest point in the swing arc before the clubhead comes back up |
| Swing Direction | The overall direction the clubhead is moving through impact, relative to the target line |
| Dyn. Loft | The dynamic loft of the club at the point of impact |
| Face Angle | The angle of the clubface relative to the target line at the moment of impact |
| Face To Path  | The difference between where the clubface is pointing and the path it's on at impact |
| Ball Speed | The speed of the ball immediately after impact |
| Smash Factor | The ratio of ball speed to club speed |
| Launch Angle | The angle at which the ball takes off relative to the ground |
| Launch Direction | The direction the ball starts relative to the target line |
| Spin Rate | The amount of spin on the ball immediately after impact |
| Spin Axis | The tilt of the spin axis relative to the horizon |
| Impact Offset | Lateral distance from the center of the clubface at impact |
| Impact Height |  Vertical distance from the center of the clubface at impact |
| Curve |  The amount of curve on the ball's flight in feet |
| Carry (Sim) |  The simulated carry distance of the ball |
| Total (Sim) | The simulated total distance of the ball including roll |
| Email |  Contact email of the Player |
             
### Interpreting Visualizations

I. What's the relationship between Club Speed and Carry Distance among the team?

![newplot (1)](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/23bdeeff-b84b-4e97-aaf9-42c575cb2cc1)


II. How does Impact Height Position Affect Ball Speed with a Driver?

![newplot (2)](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/88c9a6f1-069e-4e06-80d8-44d8f855439b)


III. How accurate are Elon players regarding distance dispersion? What is the area each player has to improve?

![newplot (3)](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/3cf9aaed-7b7f-4884-ab4e-9828fe368f05)

![newplot (4)](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/df8adef2-3988-4b93-8e60-31f0da553d33)

![newplot (5)](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/1fe0ff79-d9e7-4cf1-bf70-2cdd0417cb0b)

IV. Driver Shot Carry Distance Predictor

![driverpredictor](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/83da0335-480d-40f8-9b2e-228f9c314c6f)


## Discussion and Summary

### Importance Statement


