#! /usr/bin/env python3
#py.py - Insecure local password locker program
PASSWORDS = {'gmail': 'gmail password', 
'facebook': 'fb password', 
'linkedin':'lI password'}

import sys
import pyperclip as ppc
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()
account = sys.argv[1] #first cmd line arg is the account name

if account in PASSWORDS:
	pas = PASSWORDS[account]
	ppc.copy(pas)
else:
	print('There is no account named' + account)

