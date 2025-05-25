# Automate Backups with Shell Scripting

Write a shell script to back up /devopsworkspace as backup$(date +%F).tar.gz.
Make the script display a success message in green text using echo -e.

    #!/bin/bash

    tar -czvf /backups/backup$(date +%F).tar.gz /devopsworkspace
    
    echo -e "\e[32mBackup Successful\e[0m"
    
Save it in /backups and schedule it using cron.

    Edit cron jobs using:
    $ crontabe -e

    Add the following line to backup everyday at 5'o clock

    0 5 * * * /backupScript.sh

    
