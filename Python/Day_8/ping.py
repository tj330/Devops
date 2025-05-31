import subprocess

res = subprocess.check_output(["ping", "-c", "4", "google.com"])

try:
    with open("ping_log.txt", "wb") as f:
        f.write(res)
        print("Ping result successfully saved to ping_log.txt")
        
except Exception as e:
    print(f"Error occured: {e}")