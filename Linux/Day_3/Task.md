# Process Management & Monitoring

Start a background process to ping google.com

    $ ping google.com > ping_test.log &
    [1] 1703
    
    // & will start command as a background process

Use ps, top, and htop to monitor it.

    $ ps 
    PID TTY          TIME CMD
    1511 pts/0    00:00:00 bash
    1703 pts/0    00:00:00 ping
    1728 pts/0    00:00:00 ps

    $ ps -p 1703
    1703 pts/0    00:00:00 ping
      
    $ htop
    1703 root      20   0  4684  2560  2432 S  0.0  0.1   0:00.08 ping google.com

  Kill the process and verify it's gone.
     
    $ kill 1703

    $ ps -p 1703
    PID TTY          TIME CMD
    [1]+  Terminated              ping google.com > ping_test.log
