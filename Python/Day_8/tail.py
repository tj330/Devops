import sys
import subprocess



try: 
    file = sys.argv[1]
    num = sys.argv[2]

    print(f"The last {num} lines of the log file is: ")

    subprocess.run(["tail",f"-{num}", file])

except Exception as e:
    print(f"Error occured: {e}")