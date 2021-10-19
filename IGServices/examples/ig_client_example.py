# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:19:32 2021
Author: Shamaz Khan
Organisation: Quantl AI Ltd
"""

from rest import IGService


# Required User details
userName = 'shamazkhan86'
secureWord = 'A330airbus?'
APIKey = '3dffcba4bd2570d8b36c204ecc92554cc1d11eb4'

#Establish Connection to IG Trade
ig_trade = IGService(userName,
                       secureWord,
                       APIKey)
currentSession = ig_trade.create_session()
print(currentSession,'\n')
print('Account owned by user', userName)
userAccounts = ig_trade.fetch_accounts()
print(userAccounts)
