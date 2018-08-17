@ECHO OFF 
REM Execution of sys-mon project.
SETLOCAL


REM Set the absolute full path to the executable python.exe file on the system. 
SET python_dir="D:\Program Files (x86)\Python37-32\python.exe"

REM Set the absolute full path with filename for sysmonitoring.py.
SET monitoring_file="D:\Git_Repos\sys-mon\sysmonitoring.py"

REM execution of the sysmonitoring.py file.
%python_dir% %monitoring_file%
PAUSE