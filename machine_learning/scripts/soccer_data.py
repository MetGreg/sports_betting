'''Class for soccer data'''

# Python modules
import pandas as pd
import numpy as np
import xarray as xr


class SoccerData(object):
    '''soccer data class

    Using this class, soccer data can be read in.

    Attributes:
        teams (:any:`numpy.ndarray`): Names of all teams in league.
        df (:any:`Pandas.DataFrame`): Soccer data in Pandas dataframe format.
        data_3D (:any:`xarray.DataArray`): Team specific three dimensional
            soccer data.

    '''

    def __init__(self):
        ''' Initialization

        Does nothing so far.

        '''
        pass

    def get_teams(self, df):
        '''Find all teams in the league

        Use built-in function to find all unique teams of league.

        Args:
            df (Pandas.DataFrame): Soccer data.

        '''
        # Get all teams in HomeTeam column (should equal all teams)
        teams = df['HomeTeam'].unique()

        # Save teams to object
        self.teams = teams

    def csv2pandas(self, data_file):
        ''' Create pandas dataframe

        Creates a pandas data_frame out of a csv data_file.

        Args:
            data_file (str): Input soccer data in csv format.

        '''
        df = pd.read_csv(data_file)

        # Save data to object
        self.df = df

    def add_team_dim(self):
        '''Adds 3rd dimension for teams

        Transforms 2D pandas dataframe to 3D xarray, by adding a team
        dimension. Thus, data will be team specific.

        '''
        # Get team names, games per team and header entries
        teams = self.get_teams(self.df)
        games_per_team = int(2*len(self.df)/len(teams))
        header = list(self.df)

        # Create empty 3 dim. numpy array to be filled with new 3D data
        input_data = np.empty(
                [len(teams), games_per_team, len(header)], dtype=object
                )

        # Loop through teams and filter data
        for team_index in range(len(teams)):
            team_data = self.df[
                    (self.df['HomeTeam'] == teams[team_index]) |
                    (self.df['AwayTeam'] == teams[team_index])
                    ]

            # Loop through game numbers and headers to fill input_data
            for game_index in range(games_per_team):
                for header_index in range(len(header)):
                    input_data[team_index, game_index, header_index] =\
                        team_data.iloc[game_index, header_index]

        # Create list for game_number dimension of xarray
        game_numbers = [x for x in range(games_per_team)]

        # Create xarray with 3D input_data array
        array_3D = xr.DataArray(input_data,
                                coords=[
                                        ('teams', teams),
                                        ('game_number', game_numbers),
                                        ('header', header)
                                        ],
                                dims=['teams', 'game_number', 'header']
                                )

        # Save xarray data to object
        self.data_3D = array_3D

        def calc_win_perc(self):

            for team in self.teams:

                results = {}
                results['wins'] = 0
                results['losses'] = 0
                results['draws'] = 0

                team_data = self.data_3D(teams = team)
                for line in team_data:
                    results = self.update_results(results)


                    if team_data['HomeTeam'] == team:
                        if team_data['FTR'] == 'H':
                            wins += 1
                        elif team_data['FTR'] == 'D':