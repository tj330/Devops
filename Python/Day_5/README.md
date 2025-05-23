# File Handling

Create a script that writes the following lines to a file named log.txt<br>
Server started at 10:00 AM<br>
Health check passed<br>
Backup completed<br>

    $ python3 python3 logWrite.py
    Contents are written to log.txt

Read the contents of log.txt and print each line with line numbers prefixed like:<br>
1: Server started at 10:00 AM

    $ python3 logRead.py
    Server started at 10:00 AM

    Health check passed
    
    Backup completed

Append a new entry like "Deployment completed at 11:00 AM" to log.txt.

    $ python3 logAppend.py
    Line appended

Check if a file named config.ini exists. If not, create it and write default content:<br>
[server]<br>
port=8080<br>

    $ python3 file.py
    Default content written

Read the config.ini file and extract the port number using Python.

    $ python3 configPort.py
    Port no. is 8080

Write a script that deletes a file temp.txt only if it exists. If it doesn’t, print a warning.

    $ python3 deleteTemp.py
    Successfully deleted file temp.txt
