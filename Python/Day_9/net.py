import psutil

net_io = psutil.net_io_counters()

print("Network I/O Stats:")
print(f"Bytes Sent     : {net_io.bytes_sent / (1024 ** 2):.2f} MB")
print(f"Bytes Received : {net_io.bytes_recv / (1024 ** 2):.2f} MB")
print(f"Packets Sent   : {net_io.packets_sent}")
print(f"Packets Recv   : {net_io.packets_recv}")
