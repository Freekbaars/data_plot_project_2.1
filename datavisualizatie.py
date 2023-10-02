import pandas as pd
import matplotlib.pyplot as plt

# Stel de naam van je CSV-bestand in
csv_bestand = 'sensor_data_test_vin_3_1.csv'

# Lees het CSV-bestand in een DataFrame
df = pd.read_csv(csv_bestand)

##gemidelde van kolom bepalen
gemidelde_roll_1 = df['Pitch (graden)'].mean()
gemidelde_pitch_1 = df['Roll (graden)'].mean()

# afronden op 2 decimalen
gemidelde_roll = round(gemidelde_roll_1,2)
gemidelde_pitch = round(gemidelde_pitch_1,2)



## Maak een grafiek met matplotlib

# Plot de timestamp op de x-as, Roll op de y-as
plt.plot(df['Timestamp'],df['Roll (graden)'], label='Pitch (graden) '+str(gemidelde_pitch))
plt.plot(df['Timestamp'],df['Pitch (graden)'], label='Roll (graden)'+str(gemidelde_roll))

# Voeg een label toe aan de y-as
plt.ylabel('Roll (graden)')

# Voeg een legenda toe
plt.legend()

# Toon de grafiek
plt.show()

