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

    def add_game_cols(self):
        '''Add columns of total games

        For each arena (home, away) this method adds a column, which contains
        the past number of (home, away) games played until the game date.
        The data attribute of this class will then be updated with the pandas
        dataframe containing the new columns.

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

            # Calculate number of past home games of home team
            total_games_home = len(
                    data[0:index].loc[data['HomeTeam'] == home_team, :]
                    )

            # Calculate number of past away games of away team
            total_games_away = len(
                    data[0:index].loc[data['AwayTeam'] == away_team, :]
                    )

            # Update correct entry of new columns
            data.loc[index, 'home_games'] = total_games_home
            data.loc[index, 'away_games'] = total_games_away

        # Update data attribute
        self.data = data

    def add_win_cols(self):
        '''Add columns of total wins

        For each arena (home, away) this method adds a column, which contains
        the past number of (home, away) wins until the game date. The data
        attribute of this class will then be updated with the pandas
        dataframe containing the new columns.

        '''
        data = self.data

        # Initialize new columns with zeros
        data['home_wins'] = 0
        data['away_wins'] = 0

        # Loop through data
        for index, key in data.iterrows():

            # Find home and away team of current game
            home_team = key['HomeTeam']
            away_team = key['AwayTeam']

            # Calculate number of past home wins of home team
            total_wins_home = len(
                    data[0:index].loc[
                            (data['HomeTeam'] == home_team)
                            & (data['FTR'] == 'H'), :
                                ]
                    )

            # Calculate number of past away wins of away team
            total_wins_away = len(
                    data[0:index].loc[
                            (data['AwayTeam'] == away_team)
                            & (data['FTR'] == 'A'), :
                                ]
                    )

            # Update correct entry of new columns
            data.loc[index, 'home_wins'] = total_wins_home
            data.loc[index, 'away_wins'] = total_wins_away

        # Update data attribute
        self.data = data

    def add_perc_cols(self):
        '''Adds a column of win percentage

        For each arena (home, away) this method adds a column, which contains
        the win percentage (where home or away games are distinguished) until
        the game data. The data attribute of this class will then be updated
        with the pandas dataframe containing the new columns.

        '''
        data = self.data

        data['win_perc_home'] = data['home_wins']/data['home_games']*100
        data['win_perc_away'] = data['away_wins']/data['away_games']*100

        # Update data attribute
        self.data = data