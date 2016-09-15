import os

connect_name = 'ADSL' #your ADSL connection name
acct = '' #account
psw = '' #password
cmd_str = 'rasdial ' + connect_name + ' ' + acct + ' ' + psw
not_found = os.system(cmd_str)
