########################################################################
### Class for sports betting strategies ###
########################################################################

'''
This class is designed for sports betting strategies. 
Each strategy contains of a method to calculate the value for a given
game as well as a method to calculate the stake, depending on the value. 
Also, it is possible to calculate the profit for a given game.
'''





########################################################################
### modules ###
########################################################################

'''
Import modules needed.
'''

from .ValueCalc import ValueCalc
from .MoneyManagement import MoneyManage





########################################################################
### Class BetStrategy ###
########################################################################
class BetStrategy:
	
	
	
	
	
	
	####################################################################
	### Initialization ###
	####################################################################
	def __init__(self,bet_type,value_calc,money_manage):
		
		'''
		Method to initialize class. Saves names: Type of bet,
		calculation of value, money management
		'''
		
		self.bet_type     = bet_type
		self.value_calc   = value_calc
		self.money_manage = money_manage
		
		
		
		
		
	####################################################################
	### Find value of a game ###
	####################################################################
	def get_value(self):
		
		'''
		Finds value of a given game, by calling a method of the
		ValueCalc - object. The information, which method of ValueCalc 
		is called, is given to the strategy - object when initialized
		and saved to self.value_calc.
		--> This method checks self.value_calc to decide which 
		ValueCalc method to call.
		'''
		
		#create value-calculation object
		value_strat = ValueCalc()
		
		#calculate win percentage with the correct method
		win_perc = getattr(value_strat,self.value_calc)()
		
		#check if win_perc was calculated correctly
		assert isinstance(win_perc,float), 'win_perc not a float'
		assert (win_perc >= 0 and win_perc <= 1),\
			'win_perc not between 0 and 1'
				
		#return the win percentage calculated
		return win_perc
		
		
		
		
		
	####################################################################
	### Find stake for the bet ###
	####################################################################
	def get_stake(self):
		
		'''
		Finds stake for a given bet. Uses a money management method. 
		Which method is used is decided when initializing the strategy 
		object. Input is the game with the rates of the bookmakers as 
		well as the calculated win percentage.
		'''
		
		#create money management object
		money_strat= MoneyManage()
		
		#calculate stake with the correct method
		stake = getattr(money_strat,self.money_manage)()
		
		#check if stake was calculated correctly
		assert isinstance(stake, float), 'stake not a float'
		
		#return calculated stake
		return stake

	
	
	
	
	####################################################################
	### get profit for a bet ###
	####################################################################
	def get_profit(self):
		
		'''
		'''
		
		pass

	
	
	
	####################################################################
	### get expected profit for a bet ###
	####################################################################
	def get_exp_profit(self):
		'''
		'''
	
		pass
