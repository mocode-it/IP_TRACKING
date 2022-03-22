# ! --------------------
'''Coded By Mo Code '''
# ! -------------------

import requests
import os
import time
import webbrowser
# $$$$$$$$$$$$$
# The Code ... $
# $$$$$$$$$$$$$$
time.sleep(2)
print('\033[1;31mWait Please ...')
time.sleep(3)
os.system('clear')
print('''
\033[1;36m


 █ █▀▄   ▀█▀ █▀▄ ▄▀▄ ▄▀▀ █▄▀ █ █▄ █ ▄▀
 █ █▀     █  █▀▄ █▀█ ▀▄▄ █ █ █ █ ▀█ ▀▄█
                                    V.02
                Mo Code *_^


[1] Track IP Addrese ~


[2] About Coder _*

''')

print('\033[1;37m')

print('=====================')
co=int(input('Enter Your Choice :'))
print('=====================')
if co == 1:
    api ="http://ip-api.com/"
    print('')
           
    print('\033[1;31m===============================')
    mocode = input("\033[1;33m Enter IP Victim :\033[37m")
			     
    print('\033[1;31m===============================')
    result= requests.get(api+mocode)
    print(result.text)
    print('')
    print('===============================')
    print('\033[34mMore Information Go Here _* \n\033[32mhttps://www.infobyip.com/ip-'+mocode+".html")				    							          
     	   
  		    
						  
	    			    							        
    print('\033[1;37m===============================')
 	   
elif co == 2:
    time.sleep(1)
    print('\a\033[1;31mWait Please ...')
    time.sleep(2)
    os.system('clear')
    print('''\033[1;37m
!------------------------------!
     MokhtarAbdelkreem !>
!------------------------------!
 _ _ _ _                 _
| | | | |_ ___  __ _____|_|
| | | |   | . ||. |     | |
|_____|_|_|___|___|_|_|_|_|

!------------------------------!
   O N S O C I A L M E D I A
!------------------------------!
\033[1;32m

\033[1;31mFacebook Account !>>

\033[1;32mhttps://www.facebook.com/mokhtar.abdelkreem

\033[1;31mYoutube Channel   !>>

\033[1;32mhttps://cutt.us/mocode

\033[1;31mFacebook Page     !>>

\033[1;32mMo Code


!------------------------------!

\033[37m
''')
else:
    os.system(exit())

