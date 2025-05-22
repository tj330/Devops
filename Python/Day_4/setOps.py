web_servers = {
    "web1.company.com",
    "web2.company.com",
    "web3.company.com",
    "shared-server.company.com"
}

db_servers = {
    "db1.company.com",
    "db2.company.com",
    "shared-server.company.com"
}

common_servers = list(set(web_servers) & set(db_servers))

print(f"Common servers: {common_servers}")

only_web_server=set(web_servers)-set(db_servers)

print(f"Servers only in web are: {only_web_server}")

unique_servers = list(set(web_servers) | set(db_servers))
print(f"Unique servers are: {unique_servers}")