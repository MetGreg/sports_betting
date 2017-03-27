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
import parameter as par
import os
import pandas as pd





########################################################################
### dicts, parameters ###
########################################################################

'''
define lists and parameters needed for the program.
'''

#parameters
l_bet_types 	= par.bet_types 	 #all types of bets considered
l_value_calcs 	= par.value_calcs 	 #all value calculations 
l_money_manages = par.money_manages  #all money managements
periods 	    = par.periods		 #all periods under consideration
period_weights  = par.period_weights #all weights of the periods
outcomes        = par.outcomes 		 #list of outcomes
leagues 	    = par.leagues		 #all leagues considered

#dict with assessment criteria for each strategy
assessment = {} 

#entry for each type of bet
for bet_type in l_bet_types:
	assessment[bet_type] = {}
	
	#entry for each of the value calculations
	for value_calc in l_value_calcs:
		assessment[bet_type][value_calc] = {}
		
		#entry for each money management
		for money_manage in l_money_manages:
			assessment[bet_type][value_calc][money_manage] 			= {}
			assessment[bet_type][value_calc][money_manage]['profit']= 0
			assessment[bet_type][value_calc][money_manage]['stake'] = 0
			assessment[bet_type][value_calc][money_manage]\
				['exp_profit'] 										= 0





########################################################################
### get data ###
########################################################################

'''
Get available data of all leagues considered (set in parameters) and
add this data to one pandas.DataFrame.
'''

#create DataFrame
data = pd.DataFrame()
list_ = []

#loop through all leagues considered
for league in leagues:
	
	#get the path to the league
	path = 'data/'+ league + '/'
	
	#find all data files for this league
	for file_name in os.listdir(path):
		
		#read data with pandas
		df = pd.read_csv(path + file_name)
		
		#append data to data list
		list_.append(df)
		
#merge all data to one pandas dataFrame		
data = pd.concat(list_)





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
					for game in data:
						
						#get profit etc for each outcome
						for outcome in outcomes:
							
							#get value
							value      = strategy.get_value()
							
							#get stake
							stake      = strategy.get_stake()
							
							#get profit
							profit     = strategy.get_profit()
							
							#get expected profit
							exp_profit = strategy.get_exp_profit()
							
							#save profit to dict
							assessment[bet_type][value_calc]\
								[money_manage]['profit'] \
								+= profit
							assessment[bet_type][value_calc]\
								[money_manage]['stake'] \
								+= stake
							assessment[bet_type][value_calc]\
								[money_manage]['exp_profit'] \
								+= exp_profit





########################################################################
### Output ###
########################################################################

'''
Creates output.
'''
