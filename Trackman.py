import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

                 
st.title('Elon Golf Trackman Data Analysis')

st.image('Trackman_Logo.png', caption='')
st.image('Elon.jpg', caption='')

st.divider()

file_path = 'player_data.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

st.header('I. Club Speed vs. Carry Distance')


club_choice = st.selectbox('Select Club Type', ['Driver', '7 Iron', '54º Wedge'], index=0)

filtered_data = df[df['Club'] == club_choice] 

fig = px.scatter(
    filtered_data,
    x='Club Speed (mph)',
    y='Carry (yards)',
    color='Player',  # Differentiate players by color
    hover_data=['Ball Speed', 'Spin Rate', 'Smash Factor'],  # Additional data to show on hover
    labels={
        'Club Speed (mph)': 'Club Speed (mph)',
        'Carry (yards)': 'Carry Distance (yards)'
    },
    title=f'Relationship Between Club Speed and Carry Distance for {club_choice}',
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("This visualization plots the multiple data points and its distribution among the team with different clubs. There is an existent strong correlation between the speed and the carry distance with the 7 Iron and Driver. This output creates a better picture on how the team is standing from a hitting persepective. The Strenght Coach and Golf Coaches can utilize this chart to identify patterns among players and improve their performance from a physical and technical standpoint")

st.divider()


st.header('II. Impact Position vs. Ball Speed (Driver)')

#-----
import streamlit as st
import pandas as pd
import plotly.express as px


driver_data = df[(df['Club'] == 'Driver') & (df['Carry (yards)'] >= 240) &
                 (df['Smash Factor'] >= 1.435) & (df['Ball Speed'] >= 160)]

fig = px.scatter(driver_data, 
                 x='Impact Height (mm)', 
                 y='Ball Speed', 
                 color='Smash Factor', 
                 color_continuous_scale='Viridis',  # Using a Plotly supported colorscale
                 labels={'Impact Height (mm)': 'Impact Height (mm)', 'Ball Speed': 'Ball Speed (mph)','Spin Rate': 'Spin Rate'},
                 title='Impact Position vs. Ball Speed for Drivers')

fig.update_layout(coloraxis_colorbar=dict(
    title='Smash Factor',
    ticks='outside',
    tickvals=[driver_data['Smash Factor'].min(), driver_data['Smash Factor'].max()],
    ticktext=['Low', 'High']
))

st.plotly_chart(fig, use_container_width=True)

st.markdown("This visualization shows how when players make contact with the ball near the center or slightly above the center of the club face, the ball speed and smash factor increases. The lower ball speeds recorded have a lower smash factor (blue) and a negative impact height. This means that players that hit the ball shorter, hitting the ball higher in the face will optimize their distance by increasing the smash factor and ball speed.")

#-----

#----

#----

st.header('III. Distance Dispersion')

distance_choice = st.radio("Select Distance (Yards):", (100, 175))

if distance_choice == 100:
    min_yard, max_yard = 90, 110
    target_distance = 100
elif distance_choice == 175:
    min_yard, max_yard = 150, 200
    target_distance = 175

dispersion_data = df[(df['Carry (yards)'] >= min_yard) & (df['Carry (yards)'] <= max_yard)]

players = sorted(dispersion_data['Player'].unique())
players.insert(0, 'All Players') 

player_choice = st.selectbox('Select Player for more detailed Data', players)

if player_choice == 'All Players':
    plot_data = dispersion_data
    title = f'Carry Dispersion for {target_distance} yd Shots - All Players'
    points = None  # Hide data points for 'All Players'
else:
    plot_data = dispersion_data[dispersion_data['Player'] == player_choice]
    title = f'Carry Dispersion for {target_distance} yd Shots - {player_choice}'
    points = 'all'

fig = px.box(plot_data, x='Carry (yards)', y='Player', orientation='h', points=points,
             color='Player', title=title, notched=False)

fig.add_shape(
    type="line",
    x0=target_distance, y0=0, x1=target_distance, y1=1,
    line=dict(color="Red", width=4, dash="solid"),
    xref="x", yref="paper"
)

fig.update_layout(xaxis_title='Carry Distance (yards)', yaxis_title='')
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightBlue')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightBlue')
fig.update_layout(showlegend=True)

st.plotly_chart(fig, use_container_width=True)


st.markdown("This boxplot helps understand the accuracy in both 100 yd and 175 yd shots. In the 100 yd shots, Ollie Rotermund, Matt Doyle and Juan Callejo seem to be the most accurate, with medians right at the target line. Ollie Rotermund shows great consistency with a narrow box, while Jennings Glenn and Pedro Rabadan exhibit the most variability in their shot distances. Jack Wieler and Timmy Gannon have tendencies to overshoot the target, while Juan Callejo, Garret and Matt Doyle tend to undershoot bu are accurate in this shot.  Working in distance control is crucial to shoot good rounds, therefore having control of the carry distance is key. Players should consistently work in different distances to know their game and trend dispersion to adjust decisions on the course.")


import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


driver_data = df[(df['Club'] == 'Driver')]

features = driver_data[['Club Speed (mph)', 'Spin Rate',"Impact Height (mm)"]]
target = driver_data['Carry (yards)']
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

st.title('Driver Shot Carry Distance Predictor')

club_speed = st.number_input('Club Speed (mph)', value=120)
spin_rate = st.number_input('Spin Rate (rpm)', value=3000)
impact_height = st.number_input('Impact Height (mm)', value= 0)
input_data = {
    'Club Speed (mph)': [club_speed],
    'Spin Rate': [spin_rate],
    'Impact Height (mm)': [impact_height]
}
input_df = pd.DataFrame(input_data)

# Button to predict carry distance
if st.button('Predict Carry Distance '):
    prediction = model.predict(input_df)[0]  # Predict method expects a DataFrame
    st.write(f'Predicted Carry Distance:{prediction:.2f} yards')

st.header('Do Elon golf players and PGA Tour professionals differ significantly when driving the ball?')

#-----

df = pd.DataFrame({
    'Player': ['Juan Callejo', 'Matthew Doyle', 'Timmy Gannon','Jennings Glenn', 'Jack Wieler', 'Ollie Rotermund', 'Pedro Rabadan','Garret Risner'],
    'URL': ['https://elonphoenix.com/sports/mens-golf/roster/juan-callejo-ropero/9597', 'https://elonphoenix.com/sports/mens-golf/roster/matthew-doyle/9598', 'https://elonphoenix.com/sports/mens-golf/roster/timmy-gannon/9600','https://elonphoenix.com/roster.aspx?rp_id=9601','https://elonphoenix.com/sports/mens-golf/roster/jack-wieler/9606','https://elonphoenix.com/sports/mens-golf/roster/oliver-rotermund/9605', 'https://elonphoenix.com/roster.aspx?rp_id=9603', 'https://elonphoenix.com/sports/mens-golf/roster/garrett-risner/9604']
})

st.sidebar.image("elon-signature.png", use_column_width=True)
st.sidebar.title('Golf Roster')
for _, row in df.iterrows():
    url = row['URL']
    player_name = row['Player']
    st.sidebar.markdown(f"[{player_name}]({url})", unsafe_allow_html=True)

