This is a practice to wrap a python script to .exe file and set it auto-run when PC logins in. 

Required: 
1. PyInstaller
2. pefile
3. pywin32
4. windows only

Steps:
1. Write the python code, named as "ADSL.py"; 
2. save it to PyInstaller directory; run "python PyInstaller -F ADSL.py", so ADSL.exe will be generated; 
3. win+R, run 'regedit', put the directory of your ADSL.exe into 'HKEY_CURRENT_USER\Software\Microsoft\ Windows\ CurrentVersion\ Run'; done.
