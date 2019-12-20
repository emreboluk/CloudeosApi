from cloudeos import API


cloudeos = API("username", "password")

servers = cloudeos.list_all_servers()

print(servers)