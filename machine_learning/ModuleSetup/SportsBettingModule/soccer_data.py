#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:15:48 2017

@author: gregor-linux
"""
# Import python modules
import pandas as pd


class SoccerData(object):
    '''Store and process soccer data

    Using this class, soccer data can be processed and stored.

    Args:
        data ()

    '''

    def __init__(self, csv_data):
        '''Initialization

        Reads input data and saves data as attribute.

        Args:
            csv_data (str): Input data. Must be in csv format.

        '''
        self.data = pd.read_csv(csv_data)
        self.teams = self.data['HomeTeam'].unique()

    def add_win_col(self):
        '''Add column of accumulated wins

        Adds a column of accumulated wins to data. That means, the new column
        will contain the past number of wins.

        '''
        data = self.data

        # Loop through whole data
        for index, key in data.iterrows():
            home_team = key['HomeTeam']
            away_team = key['AwayTeam']

    def add_game_col(self):
        '''Add columns of total games

        For each arena (home, away) this method adds a column, which contains
        the past number of games played until the game date.

        Returns:
            (pandas.core.frame.DataFrame): Data with two added columns,
            containing past number of home or away games.

        '''
        data = self.data

        # Initialize new columns with zeros
        data['home_games'] = 0
        data['away_games'] = 0

        # Loop through data
        for index, key in data.iterrows():

            # Find home and away team of current game
            home_team = key['HomeTeam']
            away_team = key['AwayTeam']

            # Calculate number of past games of home team
            total_games_home = len(
                    data[0:index].loc[
                            data[0:index].loc[:, 'HomeTeam'] == home_team, :
                                ]
                        )

            # Calculate number of past games of away team
            total_games_away = len(
                    data[0:index].loc[
                            data[0:index].loc[:, 'AwayTeam'] == away_team, :
                                ]
                        )

            # Update correct entry of new columns
            data.loc[index, 'home_games'] = total_games_home
            data.loc[index, 'away_games'] = total_games_away

        # Return data with added columns
        return data
