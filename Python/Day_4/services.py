svcs = ("nginx", "docker", "ssh")

print(f"second service name is {svcs[1]}")

services = list(svcs)

services.append("kubernetes")

print(f"All service running are {services}")