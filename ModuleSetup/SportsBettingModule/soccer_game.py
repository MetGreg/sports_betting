###class for a soccer game

'''
Class for a soccer game. Will save all attributes, such as game_score
or rates.
'''





########################################################################
### modules ###
########################################################################

'''
Import modules needed for this class.
'''

from SportsBettingModule.soccer_attributes import SoccerAttributes
from datetime import datetime as dt
import numpy as np





########################################################################
### SoccerGame class ###
########################################################################
class SoccerGame(object):
    
    '''
    '''
    
    ####################################################################
    ### Initialization method ###
    ####################################################################
    def __init__(self):
        
        '''
        Does nothing so far.
        '''
        
        soccer_attr = SoccerAttributes()
        self.attr   = soccer_attr
        
        
        
        
        
    ####################################################################
    ### Get game attributes ###
    ####################################################################
    def get_attributes(self,game):
        
        '''
        '''
        
        
        
        
        
        ################################################################
        ### dictionaries ###
        ################################################################
        
        '''
        define all dictionaries used later.
        '''
        
        #dicts
        d_odds     = {} #dict for all odds
        d_max_odds = {} #dict for maximum odds
        d_avg_odds = {} #dict for average odds
        
        
        
        
        
        ################################################################
        ### get attributes ###
        ################################################################
        
        '''
        get all game attributes needed for the module.
        '''
        
        #get date of game and transform it to Datetime-object
        self.attr.date     = dt.strptime(game['Date'],'%d/%m/%y')
        
        #playing teams
        self.attr.HomeTeam = game['HomeTeam']
        self.attr.AwayTeam = game['AwayTeam']
        
        #full time scores
        self.attr.FTHG = game['FTHG']
        self.attr.FTAG = game['FTAG']
        
        #betting odds
        self.attr.B365H    = game['B365H']
        self.attr.B365D    = game['B365D']
        self.attr.B365A    = game['B365A']
        self.attr.BSH      = game['BSH']
        self.attr.BSD      = game['BSD']
        self.attr.BSA      = game['BSA']    
        self.attr.BWH      = game['BWH']
        self.attr.BWD      = game['BWD']
        self.attr.BWA      = game['BWA']
        self.attr.GBH      = game['GBH']
        self.attr.GBD      = game['GBD']
        self.attr.GBA      = game['GBA']
        self.attr.IWH      = game['IWH']
        self.attr.IWD      = game['IWD']
        self.attr.IWA      = game['IWA']
        self.attr.LBH      = game['LBH']
        self.attr.LBD      = game['LBD']
        self.attr.LBA      = game['LBA']
        self.attr.PSH      = game['PSH']
        self.attr.PSD      = game['PSD']
        self.attr.PSA      = game['PSA']
        self.attr.SOH      = game['SOH']
        self.attr.SOD      = game['SOD']
        self.attr.SOA      = game['SOA']
        self.attr.SBH      = game['SBH']
        self.attr.SBD      = game['SBD']
        self.attr.SBA      = game['SBA']
        self.attr.SJH      = game['SJH']
        self.attr.SJD      = game['SJD']
        self.attr.SJA      = game['SJA']
        self.attr.SYH      = game['SYH']
        self.attr.SYD      = game['SYD']
        self.attr.SYA      = game['SYA']
        self.attr.VCH      = game['VCH']
        self.attr.VCD      = game['VCD']
        self.attr.VCA      = game['VCA']
        self.attr.WHH      = game['WHH']
        self.attr.WHD      = game['WHD']
        self.attr.WHA      = game['WHA']
        
 
        #create list of all home win odds
        d_odds['home'] = [
            game['B365H'], game['BSH'], game['BWH'], game['GBH'],
            game['IWH']  , game['LBH'], game['PSH'], game['SOH'],
            game['SBH']  , game['SJH'], game['SYH'], game['VCH'],
            game['BSH']
            ]
            
        #create list of all draw odds
        d_odds['draw'] = [
            game['B365D'], game['BSD'], game['BWD'], game['GBD'],
            game['IWD']  , game['LBD'], game['PSD'], game['SOD'],
            game['SBD']  , game['SJD'], game['SYD'], game['VCD'],
            game['BSD']
            ]
        
        #create list of all away win odds
        d_odds['away'] = [
            game['B365A'], game['BSA'], game['BWA'], game['GBA'],
            game['IWA']  , game['LBA'], game['PSA'], game['SOA'],
            game['SBA']  , game['SJA'], game['SYA'], game['VCA'],
            game['BSA']
            ]
        
        #calculate max and average odds    
        d_max_odds['home'] = max(d_odds['home'])
        d_max_odds['draw'] = max(d_odds['draw'])
        d_max_odds['away'] = max(d_odds['away'])
        d_avg_odds['home'] = np.mean(d_odds['home'])
        d_avg_odds['draw'] = np.mean(d_odds['draw'])
        d_avg_odds['away'] = np.mean(d_odds['away'])
        
        #save all odds, max and average odds to object
        self.attr.odds     = d_odds
        self.attr.max_odds = d_max_odds
        self.attr.avg_odds = d_avg_odds
        
        #bookmaker average and maximum odds
        self.attr.BbMxH = game['BbMxH']
        self.attr.BbMxD = game['BbMxD']
        self.attr.BbMxA = game['BbMxA']
        self.attr.BbMxH = game['BbMxH']
        self.attr.BbAvH = game['BbAvH']
        self.attr.BbAvD = game['BbAvD']
        self.attr.BbAvA = game['BbAvA']
      
