#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:15:48 2017

@author: gregor-linux
"""

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

        '''
        self.data = pd.read_csv(csv_data)
