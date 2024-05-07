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


## Questions of interest
I. What's the relationship between Club Speed and Carry Distance among the team?

II. How does Impact Height Position Affect Ball Speed with a Driver?

III. How accurate are Elon players regarding distance dispersion? What is the area each player has to improve?

IV. Driver Shot Carry Distance Predictor

## Data Description

For this project, every player recorded three different shots ten times:
- 100 yds 
- 175 yds 
- Driver

For accessing the [Player Data](https://github.com/JUAN-CALLEJO/mgt4250spring2024/blob/main/player_data.csv), a Trackman Radar recorded the multiple shots from the team members. Once recorded, the raw data was imported and selected from the Elon Golf facility's connected computer. The initial file was the Trackman file which was converted to a Excel file and then to csv file. Preprocessing and cleaning the dataset consisted in removing missing metrics of some shots and deleting outliers that were caused by wrecked golf balls or miscalculations.

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

**I. What's the relationship between Club Speed and Carry Distance among the team?**

![newplot (1)](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/23bdeeff-b84b-4e97-aaf9-42c575cb2cc1)

This visualization plots the data points in a club speed range between 103-124 mph, showing an existent strong correlation between the club speed (mph) and the carry distance (yards). It is an interactive scatter plot that allows one to select players in the team, giving a better perspective of how the players are distributed in distance and club speed. It is strongly correlated, players with a higher club speed drive the ball further, giving them an advantage while making courses easier. The boxplot shows the team distribution, with players with a slower club speed in the range of 105-110 mph and other players with a 120+ mph Club Head Speed driving the ball 310+ Yards of Carry distance.

**II. How does Impact Height Position Affect Ball Speed with a Driver?**

![newplot (2)](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/88c9a6f1-069e-4e06-80d8-44d8f855439b)

This visualization shows how when players  contact the ball near the center or slightly above the center of the club face, the ball speed and smash factor increase. The lower ball speeds recorded have a lower smash factor (blue) and a negative impact height while the higher ball speeds are located on the positive side of the chart, having a higher ball speed and higher smash factor (yellow). The players that hit the ball shorter (low ball speed), trying to hit the ball higher in the face will optimize their distance by increasing the smash factor and ball speed. The sweet spot of the driver's face is 2mm above the center of the face. The sweet spot is the impact zone of the club face where the most ball speed and smash factor are generated. Higher impacts in the face tend to generate higher ball speed than lower impacts in the club face with a driver.

**III. How accurate are Elon players regarding distance dispersion? What is the area each player has to improve?**

![newplot (3)](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/3cf9aaed-7b7f-4884-ab4e-9828fe368f05)


This boxplot helps understand the accuracy in a 100-yard shot: Ollie Rotermund, Matt Doyle, and Juan Callejo seem to be the most accurate, with medians right at the target line. Ollie Rotermund shows great consistency with a narrow box, while Jennings Glenn and Pedro Rabadan exhibit the most variability in their shot distances. Jack Wieler and Timmy Gannon have tendencies to overshoot the target, while Juan Callejo, Garret, and Matt Doyle tend to undershoot but are accurate in this shot. Working in distance control is crucial to shoot good rounds, therefore having control of the carry distance is key. Players should consistently work at different distances to know their game and trend dispersion to adjust decisions on the course. 

![newplot (5)](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/1fe0ff79-d9e7-4cf1-bf70-2cdd0417cb0b)

The visualization above shows a more detailed boxplot of Ollie Rotermund's distance dispersion in a 100-yard shot.


**IV. Driver Shot Carry Distance Predictor**

![driverpredictor](https://github.com/JUAN-CALLEJO/mgt4250spring2024/assets/81531257/83da0335-480d-40f8-9b2e-228f9c314c6f)

This is a model to predict the carry distance of a Driver in yards by selecting Club Speed (mph) and Spin rate of a golf shot. It is helpful to set objectives for training. For example, a player wants to hit it 300 yards. This Prediction model will help the player know at which speed needs to swing the club for achieving the goal carry distance in yards.


## Discussion and Summary

[This Article](https://www.sportperformanceanalysis.com/article/increasing-presence-of-data-analytics-in-golf)
highlights how technology, such as ShotLink and smart equipment like swing sensors and rangefinders, revolutionizes player training, strategy, and performance evaluation. It also explores the huge impact of data analytics in golf. In order to assist golfers and broadcasters, the PGA Tour has developed sophisticated systems that analyze large amounts of data, improving both player performance and audience engagement. Additionally, golf course management uses data analytics to optimize course design and maintenance based on comprehensive play data.

What would an AI answer to the same questions?

*ChatGPT:*

*I. What's the relationship between Club Speed and Carry Distance among the team?*

*The relationship between club speed and carry distance among a team can be quite significant. Generally, as club speed increases, so does the potential for greater carry distance. This is because a higher club speed typically results in more energy transferred to the ball, leading to increased ball speed and thus longer distances. However, it's crucial to note that other factors like launch angle, spin rate, and angle of attack also play vital roles in determining the final carry distance.*

*II. How does Impact Height Position Affect Ball Speed with a Driver?*

*Impact height position can significantly affect ball speed with a driver. Ideally, a golfer wants to strike the ball with a slightly upward angle of attack ("hitting up" on the ball) to maximize distance with a driver. This is because hitting up on the ball can reduce backspin and increase launch angle, leading to a longer carry and overall distance. If the impact height position is too low (hitting down on the ball), it can result in higher backspin, lower launch, and decreased ball speed.*

*III. How accurate are Elon players regarding distance dispersion? What is the area each player has to improve?*

*Assessing the accuracy of Elon players regarding distance dispersion would require looking at their performance data, such as shot tracking information. Each player's distance dispersion accuracy can vary based on factors like swing consistency, club selection, and course conditions. Areas for improvement may include enhancing shot consistency, optimizing club selection for different distances, and refining course management strategies to minimize dispersion and improve overall accuracy.*

Does the AI align with my answers?

All of the answers are correct but lack some detail because the AI does not have the visualizations or the data. Still, all the objections made about club dynamics and the effect on the ball are correct. It is interesting to see how it develops a good answer and puts examples from different perspectives. The article emphasizes how important data is for golf and the growth of the game. 
