import sys
# Asagidaki islem cloudeos.py ust dizinde oldugundan,
# buradan direkt olarak ice aktarabilmek icindir.
sys.path.append("..")

from cloudeos import API


cloudeos = API("username", "password")

id = "12231" # ornek

destroy = cloudeos.destroy_server(id)

print(destroy)