from cloudeos import API


cloudeos = API("username", "password")

name = "MySSHKey"
public_key = "public_key" #direkt yazilabilir veya varsa dosyadan okutulabilir

ssh_key = cloudeos.create_sshKey(name, public_key)

print(ssh_key)