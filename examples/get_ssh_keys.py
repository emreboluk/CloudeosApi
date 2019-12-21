import sys
# Asagidaki islem cloudeos.py ust dizinde oldugundan,
# buradan direkt olarak ice aktarabilmek icindir.
sys.path.append("..")

from cloudeos import API


cloudeos = API("username", "password")

ssh_keys = cloudeos.get_sshkeys()

print(ssh_keys)