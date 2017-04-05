########################################################################
### program to find the best strategy for sports betting ###
########################################################################

'''
This program will compare different sports betting strategies in terms
of profit.
'''





########################################################################
### modules ###
########################################################################

'''
Import all modules needed.
'''

from SportsBettingModule.bet_strategy import BetStrategy
from SportsBettingModule.stats import Stats
from SportsBettingModule.soccer_game import SoccerGame
import parameter as par
import pandas as pd
import os






########################################################################
### dicts, parameters ###
########################################################################

'''
define lists and parameters needed for the program.
'''

#parameters
l_bet_types     = par.bet_types      #all types of bets considered
l_value_calcs   = par.value_calcs    #all value calculations 
l_money_manages = par.money_manages  #all money managements
periods         = par.periods        #all periods under consideration
period_weights  = par.period_weights #all weights of the periods
outcomes        = par.outcomes       #list of outcomes
leagues         = par.leagues        #all leagues considered
period_type 	= par.period_type	 #consider past seasons or years
flat_stake		= par.flat_stake	 #stake for a bet

#dict with assessment criteria for each strategy
assessment = {} 

#fill assessment dict with entry for each strategy-component
#entries for periods under consideration
for period in periods:
    assessment[period] = {}
    
    #entries for weights of data
    for period_weight in period_weights:
        assessment[period][period_weight] = {}
    
        #entry for each type of bet
        for bet_type in l_bet_types:
            assessment[period][period_weight][bet_type] = {}
            
            #entry for each of the value calculations
            for value_calc in l_value_calcs:
                assessment[period][period_weight][bet_type]\
                    [value_calc] = {}
                
                #entry for each money management
                for money_manage in l_money_manages:
                    assessment[period][period_weight][bet_type]\
                        [value_calc][money_manage]               = {}
                    assessment[period][period_weight][bet_type]\
                        [value_calc][money_manage]['profit']     = 0
                    assessment[period][period_weight][bet_type]\
                        [value_calc][money_manage]['stake']      = 0
                    assessment[period][period_weight][bet_type]\
                        [value_calc][money_manage]['exp_profit'] = 0

#lists
l_data             = [] #will be appended with all data available





########################################################################
### get data ###
########################################################################

'''
Get available data of all leagues considered (set in parameters) and
add this data to one pandas.DataFrame.
'''

#create DataFrame
data   = pd.DataFrame()

#loop through all leagues considered
for league in leagues:
    
    #get the path to the league
    path = 'data/processed/'+ league + '/'
    
    #find all data files for this league
    for file_name in os.listdir(path):

        #read data with pandas
        df = pd.read_csv(path + file_name,delimiter = ',')
        
        #append list with data (to use pd.concat later on)
        l_data.append(df)
        
#add all dataframes to one pandas dataframe
data = pd.concat(l_data)

#create stats objective
stats = Stats(data)





########################################################################
### Assessment of strategies ###
########################################################################

'''
This part loops through all possible combinations of the strategy-parts.
For each combination, a strategy object is created and the profit of
this strategy is calculated.
'''

#loop through periods under consideration
for period in periods:
    
    #loop through weights of data
    for period_weight in period_weights:
        
        #loops through type of bets
        for bet_type in l_bet_types:
            
            #loop through value calculation strategies
            for value_calc in l_value_calcs:
                
                #loop through money management strategies
                for money_manage in l_money_manages:
                    
                    #create Bet strategy objective
                    strategy = BetStrategy(bet_type,value_calc,
                        money_manage
                        )
                    
                    #loop through data and get profit of strategy
                    for index,game in data.iterrows():
                         
                        #calculate stats
                        getattr(stats,period_weight)(
                            game,period,period_type
                            )
                        
                    
                        #get value
                       # value = strategy.get_value(
                            #stats.home_win_perc[outcome],
                            #stats.away_win_perc[outcome]
                            #)
                        
                        #check, if there's value on this bet
                        #if value > 1/rate:
                        
                            ##get stake
                            #stake      = strategy.get_stake(
                                #flat_stake,rate,value
                                #)
                            
                            ##get profit
                            #profit     = strategy.get_profit()
                            
                            ##get expected profit
                            #exp_profit = strategy.get_exp_profit()
                            
                            ##save profit to dict
                            #assessment[period][period_weight]\
                                #[bet_type][value_calc]       \
                                #[money_manage]['profit']     \
                                #+= profit
                                
                            #assessment[period][period_weight]\
                                #[bet_type][value_calc]       \
                                #[money_manage]['stake']      \
                                #+= stake
                                
                            #assessment[period][period_weight]\
                                #[bet_type][value_calc]       \
                                #[money_manage]['exp_profit'] \
                                #+= exp_profit





########################################################################
### Output ###
########################################################################

'''
Creates output.
'''
