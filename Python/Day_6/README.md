# Exception Handling 

Take user input for two integers and divide them. Handle: ValueError if input is not an integer, ZeroDivisionError for division by zero.

    $ python3 int.py
    Enter first number: 5
    Enter second number: 0
    Cannot divide by zero.
    
Try to open a file named important_config.txt. If it doesn’t exist, print "Config file not found!" instead of crashing.

    $ python3 openFile.py
    Config file not found!

Modify the previous task and add a finally block to print "Operation complete" no matter what happens.

    $ python3 Modified.py 
    Config file not found!
    Operation complete

Create a custom exception class InvalidPortException. Raise it if a given port number is not in the range 1-65535.

    $ python3 port.py
    Enter the port no: 43434343
    Port must be between 1 and 65535

Try to delete a file using os.remove() and handle PermissionError, FileNotFoundError, and generic OSError.

    $ python3 remove.py
    You did not have necessary permission to delete
