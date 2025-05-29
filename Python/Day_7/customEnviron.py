import os

os.environ['DB_ADMIN'] = os.environ.get('USER')

print("The DB_ADMIN is: ", os.environ.get('DB_ADMIN'))