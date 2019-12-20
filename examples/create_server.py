from cloudeos import API


cloudeos = API("username", "password")

name	 = "MyServer"
region	 = "ist1"
package  = "eos1"
image	 = "ubuntu 16.04 LTS"
ssh_keys = "MySSHKey" #key olusturulmussa veya istege bagli

create   = cloudeos.create_server(name, region, package, image, ssh_keys=ssh_keys)

print(create)