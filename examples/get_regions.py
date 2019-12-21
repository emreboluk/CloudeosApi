import sys
# Asagidaki islem cloudeos.py ust dizinde oldugundan,
# buradan direkt olarak ice aktarabilmek icindir.
sys.path.append("..")

from cloudeos import API

# Api Token gerekmez
regions = API.get_regions()

for region in regions:
	if region["status"]: # Kullanimda olanlari listelemek icindir
		print("Name: {}\nCountry: {}\nslug: {}\n\n".format(
			region["name"], region["country"], region["slug"]
		))
