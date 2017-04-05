###class to define all soccer attributes

'''
Defines all attributes a soccer game has, such as full time score,
half time score, rates etc
'''





########################################################################
### modules ###
########################################################################

'''
Imports modules needed for this class.
'''





########################################################################
### Class SoccerAttributes ###
########################################################################
class SoccerAttributes(object):
    
    '''
    Defines all attributes for a soccer game. Attributes are:
    
    '''
    
    
    
    
    
    ####################################################################
    ### Initialization ###
    ####################################################################
    def __init__(self):
        
        '''
        Does nothing so far
        '''

        pass
        

        
                
       
    ####################################################################
    ### Home team ###
    ####################################################################
    @property
    def HomeTeam(self):
        
        '''
        Playing home team. Must be a string.
        '''
        
        try:
            return self._HomeTeam
        except AttributeError:
            return 0
            
    @HomeTeam.setter
    def HomeTeam(self,new_HomeTeam):
        assert isinstance(new_HomeTeam, str),\
            'new_HomeTeam not a string'
        self._HomeTeam = new_HomeTeam
        
        
        
        
       
    ####################################################################
    ### Away team ###
    ####################################################################
    @property
    def AwayTeam(self):
        
        '''
        Playing away team. Must be a string.
        '''
        
        try:
            return self._AwayTeam
        except AttributeError:
            return 0
            
    @AwayTeam.setter
    def AwayTeam(self,new_AwayTeam):
        assert isinstance(new_AwayTeam, str),\
            'new_AwayTeam not a string'
        self._AwayTeam = new_AwayTeam
        
        
        
        
     
    ####################################################################
    ### Full time home goals ###
    ####################################################################
    @property
    def FTHG(self):
        
        '''
        Full time home goals. Must be integer.
        '''
        
        try:
            return self._FTHG
        except AttributeError:
            return 0
            
    @FTHG.setter
    def FTHG(self,new_FTHG):
        assert isinstance(new_FTHG, int), 'new_FTHG not an integer'
        self._FTHG = new_FTHG
        
        
        
        
       
    ####################################################################
    ### Full time away goals ###
    ####################################################################
    @property
    def FTAG(self):
        
        '''
       d Full time away goals. Must be float.
        '''
        
        try:
            return self._FTAG
        except AttributeError:
            return 0
            
    @FTAG.setter
    def FTAG(self,new_FTAG):
        assert isinstance(new_FTAG, int), 'new_FTAG not an integer'
        self._FTAG = new_FTAG
        
        
        
        
        
    ####################################################################
    ### Bet365 home win odds ###
    ####################################################################
    @property
    def B365H(self):
        
        '''
        Bet365 home win odds. Must be float.
        '''
        
        try:
            return self._B365H
        except AttributeError:
            return 0
            
    @B365H.setter
    def B365H(self,new_B365H):
        assert isinstance(new_B365H, float), 'new_B365H not a float'
        self._B365H = new_B365H





    ####################################################################
    ### Bet365 draw odds ###
    ####################################################################
    @property
    def B365D(self):
        
        '''
        Bet365 draw odds. Must be float.
        '''
        
        try:
            return self._B365D
        except AttributeError:
            return 0
            
    @B365D.setter
    def B365D(self,new_B365D):
        assert isinstance(new_B365D, float), 'new_B365D not a float'
        self._B365D = new_B365D
    
    
    
    
    
    ####################################################################
    ### Bet365 away odds ###
    ####################################################################
    @property
    def B365A(self):
        
        '''
        Bet365 away odds. Must be float.
        '''
        
        try:
            return self._B365A
        except AttributeError:
            return 0
            
    @B365A.setter
    def B365A(self,new_B365A):
        assert isinstance(new_B365A, float), 'new_B365A not a float'
        self._B365A = new_B365A
        
        
        
        
        
    ####################################################################
    ### Blue Square home win odds ###
    ####################################################################
    @property
    def BSH(self):
        
        '''
        Blue Square home win odds. Must be float.
        '''
        
        try:
            return self._BSH
        except AttributeError:
            return 0
            
    @BSH.setter
    def BSH(self,new_BSH):
        assert isinstance(new_BSH, float), 'new_BSH not a float'
        self._BSH = new_BSH
        
        
    
    
    
    ####################################################################
    ### Blue Square draw odds ###
    ####################################################################
    @property
    def BSD(self):
        
        '''
        Blue Square home win odds. Must be float.
        '''
        
        try:
            return self._BSD
        except AttributeError:
            return 0
            
    @BSD.setter
    def BSD(self,new_BSD):
        assert isinstance(new_BSD, float), 'new_BSD not a float'
        self._BSD = new_BSD
        
    
    
    
    
    ####################################################################
    ### Blue Square away win odds ###
    ####################################################################
    @property
    def BSA(self):
        
        '''
        Blue Square away win odds. Must be float.
        '''
        
        try:
            return self._BSA
        except AttributeError:
            return 0
            
    @BSA.setter
    def BSA(self,new_BSA):
        assert isinstance(new_BSA, float), 'new_BSA not a float'
        self._BSA = new_BSA
                




    ####################################################################
    ### Bet&Win home win odds ###
    ####################################################################
    @property
    def BWH(self):
        
        '''
        Bet&Win home win odds. Must be float.
        '''
        
        try:
            return self._BWH
        except AttributeError:
            return 0
            
    @BWH.setter
    def BWH(self,new_BWH):
        assert isinstance(new_BWH, float), 'new_BWH not a float'
        self._BWH = new_BWH
    
    
    
    
        
    ####################################################################
    ### Bet$Win draw odds ###
    ####################################################################
    @property
    def BWD(self):
        
        '''
        Bet&Win draw odds. Must be float.
        '''
        
        try:
            return self._BWD
        except AttributeError:
            return 0
            
    @BWD.setter
    def BWD(self,new_BWD):
        assert isinstance(new_BWD, float), 'new_BWD not a float'
        self._BWD = new_BWD
    
    
    
    
    
    ####################################################################
    ### Bet$Win away win odds ###
    ####################################################################
    @property
    def BWA(self):
        
        '''
        Bet&Win away win odds. Must be float.
        '''
        
        try:
            return self._BWA
        except AttributeError:
            return 0
            
    @BWA.setter
    def BWA(self,new_BWA):
        assert isinstance(new_BWA, float), 'new_BWA not a float'
        self._BWA = new_BWA
        
    
    
    
    
    ####################################################################
    ### Gamebookers home win odds ###
    ####################################################################
    @property
    def GBH(self):
        
        '''
        Gamebookers home win odds. Must be float.
        '''
        
        try:
            return self._GBH
        except AttributeError:
            return 0
            
    @GBH.setter
    def GBH(self,new_GBH):
        assert isinstance(new_GBH, float), 'new_GBH not a float'
        self._GBH = new_GBH
        



    
    ####################################################################
    ### Gamebookers draw odds ###
    ####################################################################
    @property
    def GBD(self):
        
        '''
        Gamebookers draw odds. Must be float.
        '''
        
        try:
            return self._GBD
        except AttributeError:
            return 0
            
    @GBD.setter
    def GBD(self,new_GBD):
        assert isinstance(new_GBD, float), 'new_GBD not a float'
        self._GBD = new_GBD
    
    
    
    
    
    ####################################################################
    ### Gamebookers away win odds ###
    ####################################################################
    @property
    def GBA(self):
        
        '''
        Gamebookers away win odds. Must be float.
        '''
        
        try:
            return self._GBA
        except AttributeError:
            return 0
            
    @GBA.setter
    def GBA(self,new_GBA):
        assert isinstance(new_GBA, float), 'new_GBA not a float'
        self._GBA = new_GBA
            




    ####################################################################
    ### Interwetten home win odds ###
    ####################################################################
    @property
    def IWH(self):
        
        '''
        Interwetten home win odds. Must be float.
        '''
        
        try:
            return self._IWH
        except AttributeError:
            return 0
            
    @IWH.setter
    def IWH(self,new_IWH):
        assert isinstance(new_IWH, float), 'new_IWH not a float'
        self._IWH = new_IWH
        
    
    
    
    
    ####################################################################
    ### Interwetten draw odds ###
    ####################################################################
    @property
    def IWD(self):
        
        '''
        Interwetten draw odds. Must be float.
        '''
        
        try:
            return self._IWD
        except AttributeError:
            return 0
            
    @IWD.setter
    def IWD(self,new_IWD):
        assert isinstance(new_IWD, float), 'new_IWD not a float'
        self._IWD = new_IWD
        
    
    
    
    
    ####################################################################
    ### Interwetten away win odds ###
    ####################################################################
    @property
    def IWA(self):
        
        '''
        Interwetten away win odds. Must be float.
        '''
        
        try:
            return self._IWA
        except AttributeError:
            return 0
            
    @IWA.setter
    def IWA(self,new_IWA):
        assert isinstance(new_IWA, float), 'new_IWA not a float'
        self._IWA = new_IWA
        




    ####################################################################
    ### Ladbrokes home win odds ###
    ####################################################################
    @property
    def LBH(self):
        
        '''
        Ladbrokes home win odds. Must be float.
        '''
        
        try:
            return self._LBH
        except AttributeError:
            return 0
            
    @LBH.setter
    def LBH(self,new_LBH):
        assert isinstance(new_LBH, float), 'new_LBH not a float'
        self._LBH = new_LBH
        
        
        
        
        
    ####################################################################
    ### Ladbrokes draw odds ###
    ####################################################################
    @property
    def LBD(self):
        
        '''
        Ladbrokes draw odds. Must be float.
        '''
        
        try:
            return self._LBD
        except AttributeError:
            return 0
            
    @LBD.setter
    def LBD(self,new_LBD):
        assert isinstance(new_LBD, float), 'new_LBD not a float'
        self._LBD = new_LBD
        
        
        
        
        
    ####################################################################
    ### Ladbrokes away win odds ###
    ####################################################################
    @property
    def LBA(self):
        
        '''
        Ladbrokes away win odds. Must be float.
        '''
        
        try:
            return self._LBA
        except AttributeError:
            return 0
            
    @LBA.setter
    def LBA(self,new_LBA):
        assert isinstance(new_LBA, float), 'new_LBA not a float'
        self._LBA = new_LBA
        




    ####################################################################
    ### Pinnacle home win odds ###
    ####################################################################
    @property
    def PSH(self):
        
        '''
        Pinnacle home win odds. Must be float.
        '''
        
        try:
            return self._PSH
        except AttributeError:
            return 0
            
    @PSH.setter
    def PSH(self,new_PSH):
        assert isinstance(new_PSH, float), 'new_PSH not a float'
        self._PSH = new_PSH
        
    
    
    
    
    ####################################################################
    ### Pinnacle draw odds ###
    ####################################################################
    @property
    def PSD(self):
        
        '''
        Pinnacle draw odds. Must be float.
        '''
        
        try:
            return self._PSD
        except AttributeError:
            return 0
            
    @PSD.setter
    def PSD(self,new_PSD):
        assert isinstance(new_PSD, float), 'new_PSD not a float'
        self._PSD = new_PSD  
    
    
    
    
    
    ####################################################################
    ### Pinnacle away win odds ###
    ####################################################################
    @property
    def PSA(self):
        
        '''
        Pinnacle away win odds. Must be float.
        '''
        
        try:
            return self._PSA
        except AttributeError:
            return 0
            
    @PSA.setter
    def PSA(self,new_PSA):
        assert isinstance(new_PSA, float), 'new_PSA not a float'
        self._PSA = new_PSA      
    
    
    
    
    
    ####################################################################
    ### Sporting Odds home win odds ###
    ####################################################################
    @property
    def SOH(self):
        
        '''
        Sporting Odds home win odds. Must be float.
        '''
        
        try:
            return self._SOH
        except AttributeError:
            return 0
            
    @SOH.setter
    def SOH(self,new_SOH):
        assert isinstance(new_SOH, float), 'new_SOH not a float'
        self._SOH = new_SOH
    
    
    
    
    
    ####################################################################
    ### Sporting Odds draw odds ###
    ####################################################################
    @property
    def SOD(self):
        
        '''
        Sporting Odds draw odds. Must be float.
        '''
        
        try:
            return self._SOD
        except AttributeError:
            return 0
            
    @SOD.setter
    def SOD(self,new_SOD):
        assert isinstance(new_SOD, float), 'new_SOD not a float'
        self._SOD = new_SOD
        
        
        
        
        
    ####################################################################
    ### Sporting Odds away win odds ###
    ####################################################################
    @property
    def SOA(self):
        
        '''
        Sporting Odds away win odds. Must be float.
        '''
        
        try:
            return self._SOA
        except AttributeError:
            return 0
            
    @SOA.setter
    def SOA(self,new_SOA):
        assert isinstance(new_SOA, float), 'new_SOA not a float'
        self._SOA = new_SOA
    
    
    
    
    
    ####################################################################
    ### Sportingbet home win odds ###
    ####################################################################
    @property
    def SBH(self):
        
        '''
        Sportingbet home win odds. Must be float.
        '''
        
        try:
            return self._SBH
        except AttributeError:
            return 0
            
    @SBH.setter
    def SBH(self,new_SBH):
        assert isinstance(new_SBH, float), 'new_SBH not a float'
        self._SBH = new_SBH
        
        
        
        
        
    ####################################################################
    ### Sportingbet draw odds ###
    ####################################################################
    @property
    def SBD(self):
        
        '''
        Sportingbet draw odds. Must be float.
        '''
        
        try:
            return self._SBD
        except AttributeError:
            return 0
            
    @SBD.setter
    def SBD(self,new_SBD):
        assert isinstance(new_SBD, float), 'new_SBD not a float'
        self._SBD = new_SBD
    
    
    
    
    
    ####################################################################
    ### Sportingbet away win odds ###
    ####################################################################
    @property
    def SBA(self):
        
        '''
        Sportingbet away win odds. Must be float.
        '''
        
        try:
            return self._SBA
        except AttributeError:
            return 0
            
    @SBA.setter
    def SBA(self,new_SBA):
        assert isinstance(new_SBA, float), 'new_SBA not a float'
        self._SBA = new_SBA
    
    
    
    
    
    ####################################################################
    ### Stan James home win odds ###
    ####################################################################
    @property
    def SJH(self):
        
        '''
        Stan James home win odds. Must be float.
        '''
        
        try:
            return self._SJH
        except AttributeError:
            return 0
            
    @SJH.setter
    def SJH(self,new_SJH):
        assert isinstance(new_SJH, float), 'new_SJH not a float'
        self._SJH = new_SJH 
    
    
    
    
    
    ####################################################################
    ### Stan James draw odds ###
    ####################################################################
    @property
    def SJD(self):
        
        '''
        Stan James draw odds. Must be float.
        '''
        
        try:
            return self._SJD
        except AttributeError:
            return 0
            
    @SJD.setter
    def SJD(self,new_SJD):
        assert isinstance(new_SJD, float), 'new_SJD not a float'
        self._SJD = new_SJD  





    ####################################################################
    ### Stan James away win odds ###
    ####################################################################
    @property
    def SJA(self):
        
        '''
        Stan James away win odds. Must be float.
        '''
        
        try:
            return self._SJA
        except AttributeError:
            return 0
            
    @SJA.setter
    def SJA(self,new_SJA):
        assert isinstance(new_SJA, float), 'new_SJA not a float'
        self._SJA = new_SJA  
    




    ####################################################################
    ### Stanleybet home win odds ###
    ####################################################################
    @property
    def SYH(self):
        
        '''
        Stanleybet home win odds. Must be float.
        '''
        
        try:
            return self._SYH
        except AttributeError:
            return 0
            
    @SYH.setter
    def SYH(self,new_SYH):
        assert isinstance(new_SYH, float), 'new_SYH not a float'
        self._SYH = new_SYH
        
        
        
        
    
    ####################################################################
    ### Stanleybet draw odds ###
    ####################################################################
    @property
    def SYD(self):
        
        '''
        Stanleybet draw odds. Must be float.
        '''
        
        try:
            return self._SYD
        except AttributeError:
            return 0
            
    @SYD.setter
    def SYD(self,new_SYD):
        assert isinstance(new_SYD, float), 'new_SYD not a float'
        self._SYD = new_SYD
        
        
        
        
        
    ####################################################################
    ### Stanleybet away win odds ###
    ####################################################################
    @property
    def SYA(self):
        
        '''
        Stanleybet away win odds. Must be float.
        '''
        
        try:
            return self._SYA
        except AttributeError:
            return 0
            
    @SYA.setter
    def SYA(self,new_SYA):
        assert isinstance(new_SYA, float), 'new_SYA not a float'
        self._SYA = new_SYA
        




    ####################################################################
    ### VC Bet home win odds ###
    ####################################################################
    @property
    def VCH(self):
        
        '''
        VC Bet home win odds. Must be float.
        '''
        
        try:
            return self._VCH
        except AttributeError:
            return 0
            
    @VCH.setter
    def VCH(self,new_VCH):
        assert isinstance(new_VCH, float), 'new_VCH not a float'
        self._VCH = new_VCH
        
        
        
        
    
    ####################################################################
    ### VC Bet draw odds ###
    ####################################################################
    @property
    def VCD(self):
        
        '''
        VC Bet draw odds. Must be float.
        '''
        
        try:
            return self._VCD
        except AttributeError:
            return 0
            
    @VCD.setter
    def VCD(self,new_VCD):
        assert isinstance(new_VCD, float), 'new_VCD not a float'
        self._VCD = new_VCD
    
    
    
    
    
    ####################################################################
    ### VC Bet away win odds ###
    ####################################################################
    @property
    def VCA(self):
        
        '''
        VC Bet away win odds. Must be float.
        '''
        
        try:
            return self._VCA
        except AttributeError:
            return 0
            
    @VCA.setter
    def VCA(self,new_VCA):
        assert isinstance(new_VCA, float), 'new_VCA not a float'
        self._VCA = new_VCA
        
    
    
    
    
    ####################################################################
    ### William Hill home win odds ###
    ####################################################################
    @property
    def WHH(self):
        
        '''
        William Hill home win odds. Must be float.
        '''
        
        try:
            return self._WHH
        except AttributeError:
            return 0
            
    @WHH.setter
    def WHH(self,new_WHH):
        assert isinstance(new_WHH, float), 'new_WHH not a float'
        self._WHH = new_WHH
    
    
    
    
    
    ####################################################################
    ### William Hill draw odds ###
    ####################################################################
    @property
    def WHD(self):
        
        '''
        William Hill draw odds. Must be float.
        '''
        
        try:
            return self._WHD
        except AttributeError:
            return 0
            
    @WHD.setter
    def WHD(self,new_WHD):
        assert isinstance(new_WHD, float), 'new_WHD not a float'
        self._WHD = new_WHD
    
    
    
    
    
    ####################################################################
    ### William Hill away win odds ###
    ####################################################################
    @property
    def WHA(self):
        
        '''
        William Hill away win odds. Must be float.
        '''
        
        try:
            return self._WHA
        except AttributeError:
            return 0
            
    @WHA.setter
    def WHA(self,new_WHA):
        assert isinstance(new_WHA, float), 'new_WHA not a float'
        self._WHA = new_WHA





    ####################################################################
    ### Betbrain maximum home win odds ###
    ####################################################################
    @property
    def BbMxH(self):
        
        '''
        Betbrain maximum home win odds. Must be float.
        '''
        
        try:
            return self._BbMxH
        except AttributeError:
            return 0
    
    @BbMxH.setter
    def BbMxH(self,new_BbMxH):
        assert isinstance(new_BbMxH, float), 'new_BbMxH not a float'
        self._BbMxH = new_BbMxH





    ####################################################################
    ### Betbrain maximum draw odds ###
    ####################################################################
    @property
    def BbMxD(self):
        
        '''
        Betbrain maximum draw odds. Must be float.
        '''
        
        try:
            return self._BbMxD
        except AttributeError:
            return 0
    
    @BbMxD.setter
    def BbMxD(self,new_BbMxD):
        assert isinstance(new_BbMxD, float), 'new_BbMxD not a float'
        self._BbMxD = new_BbMxD





    ####################################################################
    ### Betbrain maximum away win odds ###
    ####################################################################
    @property
    def BbMxA(self):
        
        '''
        Betbrain maximum away win odds. Must be float.
        '''
        
        try:
            return self._BbMxA
        except AttributeError:
            return 0
    
    @BbMxA.setter
    def BbMxA(self,new_BbMxA):
        assert isinstance(new_BbMxA, float), 'new_BbMxA not a float'
        self._BbMxA = new_BbMxA





    ####################################################################
    ### Betbrain average home win odds ###
    ####################################################################
    @property
    def BbAvH(self):
        
        '''
        Betbrain average home win odds. Must be float.
        '''
        
        try:
            return self._BbAvH
        except AttributeError:
            return 0
    
    @BbAvH.setter
    def BbAvH(self,new_BbAvH):
        assert isinstance(new_BbAvH, float), 'new_BbAvH not a float'
        self._BbAvH = new_BbAvH





    ####################################################################
    ### Betbrain average draw odds ###
    ####################################################################
    @property
    def BbAvD(self):
        
        '''
        Betbrain average draw odds. Must be float.
        '''
        
        try:
            return self._BbAvD
        except AttributeError:
            return 0
    
    @BbAvD.setter
    def BbAvD(self,new_BbAvD):
        assert isinstance(new_BbAvD, float), 'new_BbAvD not a float'
        self._BbAvD = new_BbAvD





    ####################################################################
    ### Betbrain average away win odds ###
    ####################################################################
    @property
    def BbAvA(self):
        
        '''
        Betbrain average away win odds. Must be float.
        '''
        
        try:
            return self._BbAvA
        except AttributeError:
            return 0
    
    @BbAvA.setter
    def BbAvA(self,new_BbAvA):
        assert isinstance(new_BbAvA, float), 'new_BbAvA not a float'
        self._BbAvA = new_BbAvA
