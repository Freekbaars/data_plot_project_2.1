import pandas as pd
import numpy as np
import plotly as px
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

csv_bestand_vin_1= 'sensor_data_test_vin_1_1.csv'
csv_bestand_vin_2= 'sensor_data_test_vin_2_1.csv'
csv_bestand_vin_3= 'sensor_data_test_vin_3_1.csv'

csv_bestand_vin_1_2= 'sensor_data_test_vin_1_2.csv'
csv_bestand_vin_2_2= 'sensor_data_test_vin_2_2.csv'
csv_bestand_vin_3_2= 'sensor_data_test_vin_3_2.csv'

csv_bestand_vin_3_3= 'sensor_data_test_vin_3_3_snelheid_300.csv'
csv_bestand_vin_3_4= 'sensor_data_test_vin_3_4_snelheid_300.csv'

#vin 1
df_vin_1 = pd.read_csv(csv_bestand_vin_1)
df_vin_1_2 = pd.read_csv(csv_bestand_vin_1_2)

#vin 2
df_vin_2 = pd.read_csv(csv_bestand_vin_2)
df_vin_2_2 = pd.read_csv(csv_bestand_vin_2_2)

#vin 3
df_vin_3 = pd.read_csv(csv_bestand_vin_3)
df_vin_3_2 = pd.read_csv(csv_bestand_vin_3_2)

#vin 3 snelheid 300
df_vin_3_3 = pd.read_csv(csv_bestand_vin_3_3)
df_vin_3_4 = pd.read_csv(csv_bestand_vin_3_4)

gemidelde_roll_1= round(df_vin_1['Pitch (graden)'].mean(),2)
gemidelde_pitch_1= round(df_vin_1['Roll (graden)'].mean(),2)
gemidelde_roll_1_2= round(df_vin_1_2['Pitch (graden)'].mean(),2)
gemidelde_pitch_1_2= round(df_vin_1_2['Roll (graden)'].mean(),2)


gemidelde_roll_2= round(df_vin_2['Pitch (graden)'].mean(),2)
gemidelde_pitch_2= round(df_vin_2['Roll (graden)'].mean(),2)
gemidelde_roll_2_2= round(df_vin_2_2['Pitch (graden)'].mean(),2)
gemidelde_pitch_2_2= round(df_vin_2_2['Roll (graden)'].mean(),2)



gemidelde_roll_3= round(df_vin_3['Pitch (graden)'].mean(),2)
gemidelde_pitch_3= round(df_vin_3['Roll (graden)'].mean(),2)
gemidelde_roll_3_2= round(df_vin_3_2['Pitch (graden)'].mean(),2)
gemidelde_pitch_3_2= round(df_vin_3_2['Roll (graden)'].mean(),2)

gemidelde_roll_3_3= round(df_vin_3_3['Pitch (graden)'].mean(),2)
gemidelde_pitch_3_3= round(df_vin_3_3['Roll (graden)'].mean(),2)

print('Gemiddelde roll vin 1: ', gemidelde_roll_1)
print('Gemiddelde pitch vin 1: ', gemidelde_pitch_1)
print('Gemiddelde roll vin 1_2: ', gemidelde_roll_1_2)
print('Gemiddelde pitch vin 1_2: ', gemidelde_pitch_1_2)
print('')
print('Gemiddelde roll vin 2: ', gemidelde_roll_2)
print('Gemiddelde pitch vin 2: ', gemidelde_pitch_2)
print('Gemiddelde roll vin 2_2: ', gemidelde_roll_2_2)
print('Gemiddelde pitch vin 2_2: ', gemidelde_pitch_2_2)
print('')
print('Gemiddelde roll vin 3: ', gemidelde_roll_3)
print('Gemiddelde pitch vin 3: ', gemidelde_pitch_3)
print('Gemiddelde roll vin 3_2: ', gemidelde_roll_3_2)
print('Gemiddelde pitch vin 3_2: ', gemidelde_pitch_3_2)
print('')
print('Gemiddelde vin 3 snelheid 300')
print('Gemiddelde roll vin 3_3: ', gemidelde_roll_3_3)
print('Gemiddelde pitch vin 3_3: ', gemidelde_pitch_3_3)

fig = make_subplots(
    rows=4, cols=2,
    specs=[[{}, {}],
           [{}, {}],
           [{}, {}],
           [{"colspan": 2}, None]],
)



# data plots maken
fig.add_trace(
    go.Scatter(x=df_vin_1['Timestamp'], y=df_vin_1['Pitch (graden)'], name=f'Roll vin 1: {gemidelde_roll_1:.2f}'),
    row=1, col=1)

fig.add_trace(
    go.Scatter(x=df_vin_1_2['Timestamp'], y=df_vin_1['Pitch (graden)'], name=f'Roll vin 1_2: {gemidelde_roll_1_2:.2f}'),
    row=1, col=2)

fig.add_trace(
    go.Scatter(x=df_vin_2['Timestamp'], y=df_vin_2['Pitch (graden)'], name=f'Roll vin 2: {gemidelde_roll_2:.2f}'),
    row=2, col=1)

fig.add_trace(
    go.Scatter(x=df_vin_2_2['Timestamp'], y=df_vin_2_2['Pitch (graden)'], name=f'Roll vin 2_2: {gemidelde_roll_2_2:.2f}'),
    row=2, col=2)

fig.add_trace(
    go.Scatter(x=df_vin_3['Timestamp'], y=df_vin_3['Pitch (graden)'], name=f'Roll vin 3: {gemidelde_roll_3:.2f}'),
    row=3, col=1)

fig.add_trace(
    go.Scatter(x=df_vin_3_2['Timestamp'], y=df_vin_3_2['Pitch (graden)'], name=f'Roll vin 3_2: {gemidelde_roll_3_2:.2f}'),
    row=3, col=2)


# bar plot maken gemidelde roll
fig.add_trace(
    go.Bar(x=['vin 1', 'vin 1 test 2', 'vin 2', 'vin 2 test 2', 'vin 3', 'vin 3 test 2'], 
           y=[gemidelde_roll_1, gemidelde_roll_1_2, gemidelde_roll_2, gemidelde_roll_2_2, gemidelde_roll_3, gemidelde_roll_3_2],name='gemidelde roll van alle testen',
           marker=dict(color=[gemidelde_roll_1,gemidelde_roll_1_2,gemidelde_roll_2,gemidelde_roll_2_2,gemidelde_roll_3,gemidelde_roll_3_2], coloraxis="coloraxis",)),        
        row=4, col=1)

fig.update_yaxes(range=[3.6, 4.2], row=4, col=1)
fig.update_layout(coloraxis=dict(colorscale='Bluered_r'))
fig.update_coloraxes(colorbar={'orientation':'v', 'thickness':20 ,'y': 0.1,'len':0.3})

# opmaak

# titel
fig.update_layout(title_text="hoek van boot bijn verschilende vleugel standen", height=1000, width=1000)







# schaal verdeling op de x as verwijderen
fig.update_xaxes(showticklabels=False,row=1,col=1)
fig.update_xaxes(showticklabels=False,row=1,col=2)
fig.update_xaxes(showticklabels=False,row=2,col=1)
fig.update_xaxes(showticklabels=False,row=2,col=2)
fig.update_xaxes(showticklabels=False,row=3,col=1)
fig.update_xaxes(showticklabels=False,row=3,col=2)


# gemidelde lijn toevoegen
fig.add_hline(gemidelde_roll_1,row=1,col=1)
fig.add_hline(gemidelde_roll_1_2,row=1,col=2)
fig.add_hline(gemidelde_roll_2,row=2,col=1)
fig.add_hline(gemidelde_roll_2_2,row=2,col=2)
fig.add_hline(gemidelde_roll_3,row=3,col=1)
fig.add_hline(gemidelde_roll_3_2,row=3,col=2)

# formaat van plot
fig.update_layout(
    width=1800,  # Breedte van de uitvoerfiguur in pixels
    height=1800  # Hoogte van de uitvoerfiguur in pixels
)

#laat plot zien
fig.show()