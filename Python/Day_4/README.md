# Basic Data Structures

Create a list of server names (e.g., "web1", "db1", "cache1"). Loop through the list and print a message like: "Pinging web1... OK"

    $ python 3 servers.py  
    Pinging web1... OK
    Pinging db1... OK
    Pinging cache1... OK

Given a list of disk usages [40, 70, 90, 55] (in %), write a script that checks each and prints whether it’s under or over the threshold (e.g., 80%).

    $ python 3 disk.py                              
    disk usage 40% is under threshold
    disk usage 70% is under threshold
    disk usage 90% is over threshold
    disk usage 55% is under threshold

Store a tuple of running service names (e.g., ("nginx", "docker", "ssh")). Print the second service and convert it to a list to add service "kubernetes".

    $ python 3 services.py
    second service name is docker
    All service running are ['nginx', 'docker', 'ssh', 'kubernetes']

Create a dictionary "config" that holds a server's configurations:  hostname = web1, ip = 192.168.1.10, port =  80. Print each key and value in a readable format.

    $ python 3 host.py
    The key and values are: 
    hostname is web1
    ip is 192.168.1.10
    port is 80

You have a list of IP addresses with duplicates. Display the unique IP's (Hint: You can use set).

    $ python 3 ip.py
    Unique ip's are:
    {'172.16.0.5', '10.0.0.1', '192.168.1.10', '192.168.0.2', '192.168.1.15'}

Define two sets: web_servers and db_servers. Perform and print: Servers common to both, Servers only in web, All unique servers.

    $ python 3 setOps.py
    Common servers: ['shared-server.company.com']
    Servers only in web are: {'web3.company.com', 'web1.company.com', 'web2.company.com'}
    Unique servers are: ['web3.company.com', 'web1.company.com', 'shared-server.company.com', 'db2.company.com', 'web2.company.com', 'db1.company.com']
