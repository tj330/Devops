# Daily Tasks

Collect all platform info like OS name, release, version, machine type,  hostname and architecture.Save it in system_info.txt.

    $ python3 platfm.py
    Platform information successfully saved in system_info.txt
      
Ping google.com and save the output to ping_log.txt.

    $ python3 ping.py
    Ping result successfully saved to ping_log.txt

Check the running process and parse output to find if nginx, python, or mysqld is running.

    $ python3 processes.py
    nginx is not running
    python is running
    mysqld is running

Write a script that accepts two numbers as arguments and prints their sum.

    $ python3 sum.py 1 2
    Sum is 3

Pass log file path and number of lines to read from end: 
        
    $ python3 tail.py my_app.log 10 
    The last 10 lines of the log file is: 
    2025-06-01 09:31:20,015 - my_service - INFO - [PID 2345] Task heartbeat: OK
    2025-06-01 09:31:30,030 - my_service - ERROR - [PID 2345] Task heartbeat failed: TimeoutError
    2025-06-01 09:31:30,031 - my_service - DEBUG - [PID 2345] Stack trace: TimeoutError: No response from server in 5s
    2025-06-01 09:31:30,032 - my_service - INFO - [PID 2345] Retrying task in 10s...
    2025-06-01 09:31:40,000 - my_service - INFO - [PID 2345] Task heartbeat: OK
    2025-06-01 09:31:50,004 - my_service - INFO - [PID 2345] Task heartbeat: OK
    2025-06-01 09:32:00,100 - my_service - INFO - [PID 2345] Running system check
    2025-06-01 09:32:00,104 - my_service - INFO - [PID 2345] System check: all dependencies OK
    2025-06-01 09:32:10,004 - my_service - INFO - [PID 2345] Task heartbeat: OK
    2025-06-01 09:32:20,005 - my_service - INFO - [PID 2345] Task heartbeat: OK
