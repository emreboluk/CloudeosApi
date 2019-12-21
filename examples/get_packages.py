import sys
# Asagidaki islem cloudeos.py ust dizinde oldugundan,
# buradan direkt olarak ice aktarabilmek icindir.
sys.path.append("..")

from cloudeos import API

# Api Token gerekmez
packages = API.get_packages()

for package in packages:
	print(package) #Json Format
