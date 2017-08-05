Wrap a python script to .exe file and set it auto-run when PC logins in. It helps my parents to use their PC easier.

## Prerequisites: 
* PyInstaller
* pefile
* pywin32
* windows only

## Installing
* write the python code, named as "ADSL.py"; 
* save it to PyInstaller directory; run "python PyInstaller -F ADSL.py", so ADSL.exe will be generated; 
* win+R, run 'regedit', put the directory of your ADSL.exe into 'HKEY_CURRENT_USER\Software\Microsoft\ Windows\ CurrentVersion\ Run'; done.
