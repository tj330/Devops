import requests

response = requests.get("https://example.com/")

print("Response Headers from example.com:\n")
print(f"Content-Type: {response.headers.get('Content-Type')}")
print(f"Server: {response.headers.get('Server')}")
print(f"All Headers:\n{response.headers}")
