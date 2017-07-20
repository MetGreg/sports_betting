'''This script uses linear regression on input soccer data'''

# SoccerModule
from soccer_data import SoccerData

data_file = '../data/SC3_16_17.csv'

soccer_data = SoccerData()

df = soccer_data.csv2pandas(data_file)

xarray = soccer_data.add_team_dim(df)
