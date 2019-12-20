from cloudeos import API


cloudeos = API("username", "password")

ssh_keys = cloudeos.get_sshkeys()

print(ssh_keys)