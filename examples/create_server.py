import sys
# Asagidaki islem cloudeos.py ust dizinde oldugundan,
# buradan direkt olarak ice aktarabilmek icindir.
sys.path.append("..")

from cloudeos import API


cloudeos = API("username", "password")

name	 = "MyServer"
region	 = "ist2"
package  = "eos1"
image	 = "ubuntu-16-04-x64"
ssh_keys = "MySSHKey" #key olusturulmussa veya istege bagli

create   = cloudeos.create_server(name, region, package, image, ssh_keys=ssh_keys)

print(create)