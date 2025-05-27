class InvalidPortException(Exception):
    def __init__(self, port, msg="Port must be between 1 and 65535"):
        self.port = port
        self.msg = msg
        super().__init__(self.msg)
    

try:
    port = int(input("Enter the port no: "))

    if (port < 1 or port > 65535):
        raise InvalidPortException(port)
except InvalidPortException as e:
    print(e)
