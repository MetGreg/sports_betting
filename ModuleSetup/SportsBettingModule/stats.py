###object for sport statistics

'''
'''

########################################################################
### modules ###
########################################################################

'''
import modules needed for this program.
'''

from datetime import datetime as dt, timedelta
from dateutil.relativedelta import relativedelta
from SportsBettingModule.soccer_game import SoccerGame




########################################################################
### statistic-object ###
########################################################################
class Stats(object):
    
    '''
    '''
    
    
    
    
    
    ####################################################################
    ### Initialization ###
    ####################################################################
    def __init__(self,data):
        
        '''
        '''
        
        #all data available
        self.data = data
        
        
        
        
        
    ####################################################################
    ### get soccer stats ###
    ####################################################################
    def same_weight(self,game,period,period_type):
        
        '''
        '''
        
        
        
        
        
        ################################################################
        ### dicts, lists etc ###
        ################################################################
        
        '''
        define and initialize all dicts and lists used in this program.
        '''
        
        #lists
        places   = ['home','away'] #for easy loops
        
        #dicts
        static   = {} #will be filled with all static stats
        data     = {} #will contain entry for home and away data each
        res_prob = {} #will be filled with probabilities for each result
        
        #set all static stat counter to zero
        for place in places:
            static[place]           = {}
            static[place]['games']  = 0
            static[place]['wins']   = 0
            static[place]['draws']  = 0
            static[place]['losses'] = 0
        
    
        
        
        
        ################################################################
        ### prepare stat calculation ###
        ################################################################
        
        '''
        Find all information needed to calculate statistics, such as
        playing teams, game_date, all data of playing teams and the 
        earliest date to be considered.
        '''
        
        
        #create game objective for current game
        current_game = SoccerGame()
        current_game.get_attributes(game)
       
        #get playing teams
        home_team = current_game.attr.HomeTeam
        away_team = current_game.attr.AwayTeam
        
        #get data from playing teams
        data_away = self.data.ix[(self.data['AwayTeam'] == away_team)]
        data_home = self.data.ix[(self.data['HomeTeam'] == home_team)]
       
        #get date of game
        game_date = current_game.attr.date

        #get start date (first season/gameday considering in stats)
        if period_type == 'year':
            start_date = game_date - relativedelta(years = period)
        
        
        
        
        
        ################################################################
        ### get home team stats ###
        ################################################################
        
        '''
        Loop through data in considered period of time to get stats,
        such as number of wins, losses and draws of home team.
        '''
        
        #get home team stats
        for index, game in data_home.iterrows():
            
            #create soccer game objective and read all attrs
            home_game = SoccerGame()
            home_game.get_attributes(game)
            
            #get date of game
            home_game_date = home_game.attr.date
            
            #check, if game is within period of time to be considered
            if home_game_date >= start_date:
                
                static['home']['games'] += 1
                if home_game.attr.FTHG > home_game.attr.FTAG:
                    static['home']['wins'] += 1
                elif home_game.attr.FTHG == home_game.attr.FTAG:
                    static['home']['draws'] += 1
                elif home_game.attr.FTHG < home_game.attr.FTAG:
                    static['home']['losses'] += 1
            
        
        
        
        
        ################################################################
        ### get away team stats ###
        ################################################################
        
        '''
        Loop through data in considered period of time to get stats,
        such as number of wins, losses and draws of away team.
        ''' 
        
        #get away team stats
        for index, game in data_away.iterrows():
            
            #create soccer game objective and read all attrs
            away_game = SoccerGame()
            away_game.get_attributes(game)
            
            #get date of game
            away_game_date = away_game.attr.date
            
            #check, if game is within period of time to be considered
            if away_game_date >= start_date:
                
                static['away']['games'] += 1
                if away_game.attr.FTAG > away_game.attr.FTHG:
                    static['away']['wins'] += 1
                elif away_game.attr.FTAG == away_game.attr.FTHG:
                    static['away']['draws'] += 1
                elif away_game.attr.FTAG < away_game.attr.FTHG:
                    static['away']['losses'] += 1
        
        
        
        
        
        ################################################################
        ### calculate result probabilities ###
        ################################################################
        
        '''
        Calculate probability for each result over the period of time 
        considered, by dividing for example the number of wins by
        the total number of games to get the probability for a win.
        '''
        
        #calculate probabilities for each result
        for place in places:
            res_prob[place] = {}
            res_prob[place]['home_win'] = static[place]['wins']\
                /static[place]['games']
            res_prob[place]['draw'] = static[place]['draws']\
                /static[place]['games']
            res_prob[place]['away_win'] = static[place]['losses']\
                /static[place]['games']
        
        #save probabilities to object
        self.res_prob = res_prob
        
